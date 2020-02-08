import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C


class ResultCallback(CallbackBase):
    """
    用于执行操作的示例回调插件作为结果进入
    如果要将所有结果收集到单个对象中以进行处理
    执行结束，考虑使用``json``回调插件
    或编写自己的自定义回调插件
    """

    def v2_runner_on_ok(self, result, **kwargs):
        """
        打印结果的json表示
        此方法可以将结果存储在实例属性中以便稍后检索
        :param result:
        :return:
        """
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))


Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# 初始化所需的对象
loader = DataLoader()
passwords = dict(vault_pass='secret')


# 实例化我们的ResultCallback以便在它们进入时处理结果.Ansible希望这是它的主要显示器出口之一
results_callback = ResultCallback()

# 创建库存，使用路径将主机配置文件作为源或托管在逗号分隔的字符串中
inventory = InventoryManager(loader=loader, sources='localhost')

# 变量管理器负责合并所有不同的源，为您提供每个上下文中可用变量的统一视图
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 创建代表我们游戏的数据结构，包括任务，这基本上是我们的YAML加载器在内部执行的操作。
play_source = dict(
    name = "Ansible Play",
    hosts='localhost',
    gather_facts='no',
    tasks=[
        dict(action=dict(module='shell', args='ls'), register='shell_out'),
        dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
    ]
)


# 创建播放对象，playbook对象使用.load而不是init或new方法， ＃这也将自动从play_source中提供的信息创建任务对象
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# 运行它 - 实例化任务队列管理器，它负责分叉和设置所有对象以迭代主机列表和任务
tqm = None
try:
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords,
        # 使用我们的自定义回调而不是``default``回调插件，它打印到stdout
        stdout_callback=results_callback,
    )
    # 戏剧中最有趣的数据实际上是发送给回调的方法
    result = tqm.run(play)
finally:
    # 我们总是需要清理子进程和我们用来与它们通信的结构
    if tqm is not None:
        tqm.cleanup()

    # 删除ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

