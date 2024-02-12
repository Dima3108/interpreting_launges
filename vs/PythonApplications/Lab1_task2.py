#Вариант 10

import array
from locale import setlocale
setlocale("Rus")
atasks_=[4,11,15]
def task_manager_get_task():
    print("Выберите задачу, которую хотите решить\n")
    global atasks_
    i=0
    while(i<atasks_.count()):
        print("у задачи ",atasks_[i]," код равен",i,"\n")
        i=i+1
    numt=-1
    while(numt<0 or numt>=atasks_.count()):
          print("Введите код задачи")
          numt=int(input())
    return atasks_[numt]
_task=task_manager_get_task()

    