# coding=Latin-1
#https://habr.com/ru/articles/556230/
#Âàðèàíò 10
import array
import locale,pprint,time,os
from xml.etree.ElementTree import tostring
import clr
pathDLL = os.getcwd() + "\\ForPython.dll"
clr.AddReference(pathDLL)
import ForPython
from ForPython import HelpFunctions
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#print(locale.getlocale(),"\n")
s="###"
HelpFunctions.CPrint(s)
atasks_=[4,11,15]
def task_manager_get_task():
   # print("Âûáåðèòå çàäà÷ó, êîòîðóþ õîòèòå ðåøèòü\n")
    HelpFunctions.CPrint("Âûáåðèòå çàäà÷ó, êîòîðóþ õîòèòå ðåøèòü\n")
    global atasks_
    i=0
    while(i<atasks_.__len__()):
        #print("ó çàäà÷è ",atasks_[i]," êîä ðàâåí",i,"\n")
        sar=["ó çàäà÷è ",atasks_[i]," êîä ðàâåí",i,"\n"]
        HelpFunctions.CPrintArray(sar)
        i=i+1
    numt=-1
    while(numt<0 or numt>=atasks_.count()):
          print("Ââåäèòå êîä çàäà÷è")
          numt=int(input())
    return atasks_[numt]
_task=task_manager_get_task()

    