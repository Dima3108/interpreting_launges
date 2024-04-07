import array
#import threading
N = 12
thread_count=1
print(((N-1)%12)-1)
#Вариан 10
#Номер 1
def isProst(x,y):
    if x%y==0:
        return  False
    else:
        return  True
def getCount(x):
    count=0
    y=range(2,x,2)
    for i in y:
        if isProst(x,i)==False:
            count+=1
    return  count
val=int(input())
print(getCount(val))
#Задание 2
def GetMaxNumber(x):
    tmp=int(x)
    v=-1
    while tmp>0 :
        l = tmp % 10
        if l % 3 !=0:
            if l > v :
                v=l
        tmp=int(tmp/10)
    return  v
val = int(input())
res = GetMaxNumber(val)
if res != -1 :
    print(res)
else:
    print("подходящие цифры отсутсвуют")
#Задание 3
cesh_nd=[0,1]
def ND_thread(i,x):
    val=i+2
    min=-1
    while val<x:
         if( x % val == 0):
            min = val
            break
         val=val+1
    global  cesh_nd
    cesh_nd[i]=min
def ND(x): #Наименьший делитель не равный 1
    #min = -1
    #val = x-1
    #while val > 1 :
       
        #val=val-1
    #th1=threading.Thread(target=ND_thread,args=(0,x))
    #th1.start()
    #th2=threading.Thread(target=ND_thread,args=(1,x))
    #th2.start()
    #th1.join()
    #th2.join()
    ND_thread(0,x)
    #if (cesh_nd[0] < cesh_nd[1]) and (cesh_nd[0]>0) :
    #    return cesh_nd[0]
    return cesh_nd[0]
def ChifSum(x): #Сумма цифр < 5
    sum =0
    tmp=x
    while tmp > 0:
        if (tmp % 10) < 5 :
            sum = sum + (tmp % 10)
        tmp=int(tmp/10)
    return sum

cesh_th=[0,1]
def Proizv_thread(id,value,nd):
    i=value-id-1
    global cesh_th
    cesh_th[id]=-1
    while i>1:
        if (i % nd !=0) or (nd % i !=0):
           cesh_th[id]=i
           break
        i=i-thread_count
    

def Proizv(x):
    #ran1=range(1,x)
   
    max = -1
    
    nd= ND(x)
    #th1=threading.Thread(target=Proizv_thread,args=(0,x,nd))
    #th1.start()
    #th2=threading.Thread(target=Proizv_thread,args=(1,x,nd))
    #th2.start()
   
    
    #i=1
    #while i<x:
    #    
    #    i=i+1 
    Proizv_thread(0,x,nd)
    sum=ChifSum(x)
    #th1.join()
    #th2.join()
    global cesh_th
    res=cesh_th[0]
    #if cesh_th[0]>cesh_th[1]:
    #    res=cesh_th[0]
    #else :
    #    res=cesh_th[1]
    return res*sum
val=int(input())
r=Proizv(val)
if r <0 :
    print("отсутсвует подходящие число")
else :
    print(r)