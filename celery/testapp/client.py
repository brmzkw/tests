import time

from celery import chord

from .worker import *



def main():
    task = chord([
        add.s(3, 4),
        sub.s(10, 9)
    ])(chord_callback.s().on_error(chord_callback_error.s()))

#    import pdb
#    pdb.set_trace()

    return

    time.sleep(.5)

    print ('Ready? %s' % task.ready())
    print ('Result: %s' % task.result)
