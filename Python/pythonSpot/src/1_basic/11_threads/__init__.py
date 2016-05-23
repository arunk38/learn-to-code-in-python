import time
import threading
from threading import *


class MyThread(threading.Thread):  # simple threading
    def __init__(self, x):
        self.__x = x
        threading.Thread.__init__(self)

    def run(self):
        print(str(self.__x))


for x in range(10):
    MyThread(x).start()


# timed threads

def hello():
    print("Hello World!!")


t = Timer(10.0, hello)  # calls hello after 10 secs

t.start()


def handleClient1():
    while (True):
        print("Waiting for client 1...")
        time.sleep(5)  # wait for 5 secs


def handleClient2():
    while (True):
        print("Waiting for client 2...")
        time.sleep(5)  # wait for 5 secs

t1 = Timer(5.0, handleClient1)
t2 = Timer(3.0, handleClient2)


t1.start()
t2.start()
