
from celery_app import task2
from celery_app import task1

task1.add.apply_async(args=[2, 8])
task2.multiply.apply_async(args=[3, 8])

print("hello world")
