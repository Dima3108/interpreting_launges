# coding=Latin-1
#https://habr.com/ru/articles/556230/
#Êîìïèëÿöèÿ â exe 
#https://habr.com/ru/companies/vdsina/articles/557316/
#Âàðèàíò 10
import array
import locale,pprint,time,os
from xml.etree.ElementTree import tostring
#import clr
#pathDLL = os.getcwd() + "\\Debug\\netstandard2.0\\ForPython.dll"
#clr.AddReference(pathDLL)
#import ForPython
from ForPython import HelpFunctions
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#print(locale.getlocale(),"\n")
'''s="###"
HelpFunctions.CPrint(s)
HelpFunctions.CPrint("\n")'''
atasks_=[4,11,15]
def task_manager_get_task():
   # print("Âûáåðèòå çàäà÷ó, êîòîðóþ õîòèòå ðåøèòü\n")
    #HelpFunctions.CPrintRusWord(int(0))
    print("Âûáåðèòå çàäà÷ó, êîòîðóþ õîòèòå ðåøèòü\n")
    #HelpFunctions.CPrint("\n")
    print("\n")
    global atasks_
    i=0
    while(i<atasks_.__len__()):
        #print("ó çàäà÷è ",atasks_[i]," êîä ðàâåí",i,"\n")
        #sar=["ó çàäà÷è ",atasks_[i]," êîä ðàâåí",i,"\n"]
        #HelpFunctions.CPrintRusWord(int(1))
        print("ó çàäà÷è")
        #HelpFunctions.CPrint(str(atasks_[i]))
        print(atasks_[i])
        #HelpFunctions.CPrintRusWord(int(2))
        print(" êîä ðàâåí")
        #HelpFunctions.CPrint(str(i))
        print(str(i))
        #HelpFunctions.CPrint("\n")
        print("\n")
        i=i+1
    numt=-1
    while(numt<0 or numt>=atasks_.__len__()):
          #print("Ââåäèòå êîä çàäà÷è")
         # HelpFunctions.CPrintRusWord(int(3))
         print("Ââåäèòå êîä çàäà÷è\n")
         # HelpFunctions.CPrint("\n")
          #numt=HelpFunctions.CGetInt()
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
    #HelpFunctions.CPrint(count_)
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
   #HelpFunctions.CPrintRusWord(int(4))
   print("Ââåäèòå ñòðîêó äëÿ ïðîâåðêè íà ïîëèíäðîì\n")
   #_str=str(HelpFunctions.GGetString())
   _str=str(input())
   _stat=task_4(_str)
   if(_stat==True):
       #HelpFunctions.CPrintRusWord(int(5))
       print("Ñòðîêà ÿâëÿåòñÿ ïîëèíäðîìîì")
   else:
       #HelpFunctions.CPrintRusWord(int(6))
       print("Ñòðîêà íå ÿâëÿåòñÿ ïîëèíäðîìîì")
elif (_task==11):
     #HelpFunctions.CPrintRusWord(int(7))
     print("Ââåäèòå ñëîâà ÷åðåç ïðîáåë\n")
     #_str=str(HelpFunctions.GGetString())
     _str=str(input())
     _stat=task_11(_str)
else:
    #HelpFunctions.CPrintRusWord(int(8))
    print("Ââåäèòå íàòóðàëüíîå ÷èñëî äëÿ" +
                                                   " ïîäñ÷åòà ðàçëè÷íûõ öèôð" +
                                                   " â åãî äåñÿòè÷íîé çàïèñè\n" )
    #_count= task_15(str(HelpFunctions.CGetInt()))
    _count=task_15(str(input()))
    #HelpFunctions.CPrint(int(_count))
    print(_count)
HelpFunctions.Exit()  