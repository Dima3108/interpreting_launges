#������� 10

import array
from locale import setlocale
setlocale("Rus")
atasks_=[4,11,15]
def task_manager_get_task():
    print("�������� ������, ������� ������ ������\n")
    global atasks_
    i=0
    while(i<atasks_.count()):
        print("� ������ ",atasks_[i]," ��� �����",i,"\n")
        i=i+1
    numt=-1
    while(numt<0 or numt>=atasks_.count()):
          print("������� ��� ������")
          numt=int(input())
    return atasks_[numt]
_task=task_manager_get_task()

    