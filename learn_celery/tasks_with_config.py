from celery import Celery

app = Celery(__file__[:-len('.py')])
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y
