from celery.task import task


@task()
def add_sum(y):
    a = 0
    for x in range(y, 10000):
        a += x
    return a
