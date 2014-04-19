from celery import Celery

app = Celery('first_to_tasks', backend='amqp', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
