# -*- coding: utf-8 -*-
#https://habr.com/ru/articles/556230/
#���������� � exe 
#https://habr.com/ru/companies/vdsina/articles/557316/
#������� 10
import array
import locale,pprint,time,os
import string
#import array
from xml.etree.ElementTree import tostring
from xml.etree.ElementTree import tostring
#import clr
#pathDLL = os.getcwd() + "\\Debug\\netstandard2.0\\ForPython.dll"
#clr.AddReference(pathDLL)
#import ForPython
#from ForPython import HelpFunctions
#locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#print(locale.getlocale(),"\n")
s="###"
#HelpFunctions.CPrint(s)
#HelpFunctions.CPrint("\n")
atasks_=[4,11,15]
def task_manager_get_task():
   # print("�������� ������, ������� ������ ������\n")
    #HelpFunctions.CPrintRusWord(int(0))
    #HelpFunctions.CPrint("\n")
    print("Выберите задачу, которую хотите решить\n")
    global atasks_
    i=0
    while(i<atasks_.__len__()):
        #print("� ������ ",atasks_[i]," ��� �����",i,"\n")
        #sar=["� ������ ",atasks_[i]," ��� �����",i,"\n"]
        #HelpFunctions.CPrintRusWord(int(1))
        print("у задачи ")
        #HelpFunctions.CPrint(str(atasks_[i]))
        print(atasks_[i])
        #HelpFunctions.CPrintRusWord(int(2))
        print(" код равен")
        #HelpFunctions.CPrint(str(i))
        #HelpFunctions.CPrint("\n")
        print(i)
        print("\n")
        i=i+1
    numt=-1
    while(numt<0 or numt>=atasks_.__len__()):
          #print("������� ��� ������")
          #HelpFunctions.CPrintRusWord(int(3))
          #HelpFunctions.CPrint("\n")
          print("Введите код задачи\n")
          #numt=HelpFunctions.CGetInt()
          numt=int(input())
    return atasks_[numt]

def task_4(str):
    count=0
    i=0
    while(i<len(str)):
        if(str[i]>='0'and str[i]<='4'):
            count=count+1
        i=i+1
    return  count

def task_15(str):
    count = 0
    i = 0
    while (i < len(str)):
        if (str[i] >= '6' and str[i] <= '9'):
            count = count + 1
        i = i + 1
    return count
def task_11(st):
    #���� ������ , ��������� ���������������� ������� ��������
    str2=st.lower()
    cesh_str=""
    i=0
    while(i<len(str2)):
        c=str2[i]
        j=0
        suc=True
        while(j<len(cesh_str)):
            if(c==cesh_str[j]):
                suc=False
                break
            j=j+1
        if(suc):
            cesh_str=cesh_str+c
        i=i+1
    table="qwertyuiopasdfghjklzxcvbnm".lower()
    stat=[]
    i=0
    while(i<len(table)):
        stat.append(-1)
        i=i+1
    i=0
    while(i<len(cesh_str)):
        j=0
        while(j<len(table)):
            if(table[j]==cesh_str[i]):
                stat[1]=True
                break
            j=j+1
        i=i+1
    count=0
    i=0
    while(i<len(table)):
        if(stat[j]==-1):
            count=count+1
        i=i+1
    return count
_task=task_manager_get_task()
if(_task==4):
   #HelpFunctions.CPrintRusWord(int(9))
   print("Дана строка. Необходимо подсчитать" +
                                                   " количество чисел в этой строке," +
                                                   " \r\nзначение которых меньше 5\n")
   #_str=str(HelpFunctions.GGetString())
   _str=input()
   _stat=task_4(_str)
   #HelpFunctions.CPrint(int(_stat))
   print(_stat)
   print("\n")
  # if(_stat==True):
  #     HelpFunctions.CPrintRusWord(int(5))
  # else:
  #     HelpFunctions.CPrintRusWord(int(6))
elif (_task==11):
     #HelpFunctions.CPrintRusWord(int(10))
     print(" Дана строка. Необходимо найти все " +
                                                   " незадействованные символы " +
                                                   "\r\nлатиницы в этой строке.\r\n")
     #_str=str(HelpFunctions.GGetString())
     _str=str(input())
     _stat=task_11(_str)
     #HelpFunctions.CPrint(int(_stat))
     print(_stat)
     print("\n")
else:
    #HelpFunctions.CPrintRusWord(int(11))
    print("Дана строка. Необходимо подсчитать" +
                                                   " количество цифр в этой строке," +
                                                   " \r\nзначение которых больше 5\n")
    #_count= task_15(tostring(HelpFunctions.GGetString()))
    _count=task_15(str(input()))
    #HelpFunctions.CPrint(int(_count))
    print(_count)
#HelpFunctions.Exit()  