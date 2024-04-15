# -*- coding: utf-8 -*-

import array
import locale,pprint,time,os
import string

from xml.etree.ElementTree import tostring
from xml.etree.ElementTree import tostring

atasks_=[4,11,15]
def task_manager_get_task():
   
    print("Выберите задачу, которую хотите решить\n")
    global atasks_
    i=0
    while(i<atasks_.__len__()):
        
        print("у задачи ")
        
        print(atasks_[i])
        
        print(" код равен")
        
        print(i)
        print("\n")
        i=i+1
    numt=-1
    while(numt<0 or numt>=atasks_.__len__()):
          
          print("Введите код задачи\n")
          
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
   
   print("Дана строка. Необходимо подсчитать" +
                                                   " количество чисел в этой строке," +
                                                   " \r\nзначение которых меньше 5\n")
   
   _str=input()
   _stat=task_4(_str)
   
   print(_stat)
   print("\n")
  
elif (_task==11):
     
     print(" Дана строка. Необходимо найти все " +
                                                   " незадействованные символы " +
                                                   "\r\nлатиницы в этой строке.\r\n")
     
     _str=str(input())
     _stat=task_11(_str)
     
     print(_stat)
     print("\n")
else:
    
    print("Дана строка. Необходимо подсчитать" +
                                                   " количество цифр в этой строке," +
                                                   " \r\nзначение которых больше 5\n")
    
    _count=task_15(str(input()))
   
    print(_count)
