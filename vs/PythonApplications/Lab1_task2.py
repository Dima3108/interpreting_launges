# coding=Latin-1
#https://habr.com/ru/articles/556230/
#������� 10
import array
import locale,pprint,time,os
from xml.etree.ElementTree import tostring
import clr
pathDLL = os.getcwd() + "\\Debug\\netstandard2.0\\ForPython.dll"
clr.AddReference(pathDLL)
import ForPython
from ForPython import HelpFunctions
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#print(locale.getlocale(),"\n")
s="###"
HelpFunctions.CPrint(s)
HelpFunctions.CPrint("\n")
atasks_=[4,11,15]
def task_manager_get_task():
   # print("�������� ������, ������� ������ ������\n")
    HelpFunctions.CPrintRusWord(int(0))
    HelpFunctions.CPrint("\n")
    global atasks_
    i=0
    while(i<atasks_.__len__()):
        #print("� ������ ",atasks_[i]," ��� �����",i,"\n")
        #sar=["� ������ ",atasks_[i]," ��� �����",i,"\n"]
        HelpFunctions.CPrintRusWord(int(1))
        HelpFunctions.CPrint(str(atasks_[i]))
        HelpFunctions.CPrintRusWord(int(2))
        HelpFunctions.CPrint(str(i))
        HelpFunctions.CPrint("\n")
        i=i+1
    numt=-1
    while(numt<0 or numt>=atasks_.__len__()):
          #print("������� ��� ������")
          HelpFunctions.CPrintRusWord(int(3))
          HelpFunctions.CPrint("\n")
          numt=HelpFunctions.CGetInt()
    return atasks_[numt]
_task=task_manager_get_task()

    