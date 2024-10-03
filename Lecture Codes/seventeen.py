#Execute tasks

#Execute task every 2 sec
#Execute for every 5 sec
#Execute for everday at 8 am

import time
import schedule

def task1():
    print("Task 1 is executed")

def task2():
    print("Task 2 is executed")

def task3():
    print("Task 3 is executed")

schedule.every(2).seconds.do(task1)
schedule.every(5).seconds.do(task2)
schedule.every().day.at("13:42").do(task3)

while True:
    schedule.run_pending()
    time.sleep(1)
