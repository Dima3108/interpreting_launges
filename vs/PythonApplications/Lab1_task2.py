# -*- coding: utf-8 -*-

'''s="###"
HelpFunctions.CPrint(s)
HelpFunctions.CPrint("\n")'''
atasks_=[4,11,15]
def task_manager_get_task():
   
    print("Выберите задачу, которую хотите решить\n")
    
    print("\n")
    global atasks_
    i=0
    while(i<atasks_.__len__()):
        
        print("у задачи")
        
        print(atasks_[i])
        
        print(" код равен")
        
        print(str(i))
        
        print("\n")
        i=i+1
    numt=-1
    while(numt<0 or numt>=atasks_.__len__()):
          
         print("Введите код задачи\n")
        
         numt=int(input())
    return atasks_[numt]
def task_4(s):
    _len=len(s)
    i=0
    while (i<_len//2):
        if(s[i]!=s[_len-i-1]):
            return False
        i+=1
    return True 
def task_11(s):
    count_=s.split(" ").__len__()
    
    print(count_)
    print("\n")
def task_15(s):
    count_=0
    i=0
    while(i<len(s)):
        j=i-1
        stat=True
        while(j>=0):
            if(s[j]==s[i]):
                stat=False
            j=j-1
        if(stat==True):
             count_=count_+1
        if(count_>=10):
            break
        i=i+1
    return count_
_task=task_manager_get_task()
if(_task==4):
   
   print("Введите строку для проверки на полиндром\n")
   
   _str=str(input())
   _stat=task_4(_str)
   if(_stat==True):
       
       print("Строка является полиндромом")
   else:
       
       print("Строка не является полиндромом")
elif (_task==11):
     
     print("Введите слова через пробел\n")
     
     _str=str(input())
     _stat=task_11(_str)
else:
    
    print("Введите натуральное число для" +
                                                   " подсчета различных цифр" +
                                                   " в его десятичной записи\n" )
    
    _count=task_15(str(input()))
    
    print(_count)
 