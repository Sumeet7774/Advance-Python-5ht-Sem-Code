from time import sleep
from threading import Thread

def task1(sleep_time,message):
    for i in range(10):
        sleep(sleep_time)
        print("Thread1: " + message,i)
        
def task2(sleep_time,message):
    for i in range(10):
        sleep(sleep_time)
        print("Thread2: " + message,i)        

thread1 = Thread(target=task1, args=[1.5, "Hello"])
thread2 = Thread(target=task2, args=[3,"Hi"])
thread1.start()
thread2.start()

print("Waiting for the thread...")
thread1.join()
thread2.join()
print("Thread completed")