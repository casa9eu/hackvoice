import time
from multiprocessing import Process

def speak():
    print("1")
    time.sleep(5)
    print("5")

def listen():
    print("*")
    time.sleep(4)
    print("*")

if __name__ == '__main__':
    while True:
        p1 = Process(target=speak)
        p1.start()
        p2 = Process(target=listen)
        p2.start()
        p1.join()
        p2.join()