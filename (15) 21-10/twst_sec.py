import queue
from threading import Thread

def foo(bar):
    print('hello {0}'.format(bar))
    return 'foo'

queue = queue.Queue()

t = Thread(target=lambda q, arg1: q.put(foo(arg1)), args=(que, 'world!'))
t.start()
t.join()
result = que.get()
print(result)
