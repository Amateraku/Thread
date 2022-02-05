
from threading import Thread


def second():
    print(6543)
    print(83724)


def thirds():
    print(4865)
    print(46754)


for i in range(100):
    th = Thread(target=second(), args=(i, ))
    th.start()
    print(16534)
