from time import sleep
from threading import Thread

def task(sleep_time, message):
    sleep(sleep_time)
    print(message)
    
thread = Thread(target=task, args=[1.5, "New Message"])
thread.start()
print("Waiting for the thread...")
thread.join()