from time import sleep
from threading import Thread
thread = Thread(target=lambda:sleep(1))
print(thread.is_alive())
thread.start()
print(thread.is_alive())
thread.join()
print(thread.is_alive())