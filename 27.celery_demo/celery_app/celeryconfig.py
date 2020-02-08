from datetime import timedelta
from celery.schedules import crontab


BROKER_URL = 'redis://127.0.0.1:6379'               # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  # 指定 Backend

CELERY_TIMEZONE='Asia/Shanghai'                     # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'

CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'celery_app.task1',
    'celery_app.task2'
)

CELERYBEAT_SCHEDULE = {
    "add-every-30-seconds":{
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=30),
        'args': (5, 8)
    },
    "multiply-at-some-time": {
        'task': "celery_app.task2.multiply",
        'schedule': crontab(hour=9, minute=50),
        'args': (3,7)
    }
}


"""
celery -A celery_app worker --loglevel=info --beat
celery -A celery_app worker --loglevel=info   
celery beat -A celery_app
"""