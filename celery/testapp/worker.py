import time

from celery import Celery, chord
import celery.bin.worker


app = Celery(
    'tasks',
    backend='db+postgresql://postgres@test-celery-psql/celery',
    broker='pyamqp://guest@test-celery-rabbitmq//',
)

@app.task
def add(x, y):
    return x + y


@app.task
def sub(x, y):
    raise ValueError('blurp')


@app.task
def chord_callback(*args, **kwargs):
    print ('>>>>', args, kwargs)
    return 'chord callback result'

@app.task(bind=True)
def chord_callback_error(self, task_id):
    task = app.AsyncResult(task_id, app=app, backend=self.backend)
    while not task.ready():
        self.retry(countdown=1)

    print ('>>>', task, task.result)



def main():
    worker = celery.bin.worker.worker(app=app)
    worker.run(
        traceback=True,
        loglevel='INFO',
        debug=True,
    )
