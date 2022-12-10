from threading import Thread


def func(name):
    for i in range(1000):
        print(name, i)


t1 = Thread(target=func, args=("线程1",))
t2 = Thread(target=func, args=("线程2",))
t1.start()
t2.start()