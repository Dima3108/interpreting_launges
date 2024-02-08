N = 12
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
def ND(x): #Наименьший делитель не равный 1
    min = -1
    val = x-1
    while val > 1 :
        if( x % val == 0):
            min = val
        val=val-1
    return min
def ChifSum(x): #Сумма цифр < 5
    sum =0
    tmp=x
    while tmp > 0:
        if (tmp % 10) < 5 :
            sum = sum + (tmp % 10)
        tmp=int(tmp/10)
    return sum
def Proizv(x):
    #ran1=range(1,x)
    max = -1
    nd= ND(x)

    i=1
    while i<x:
        if (i % nd !=0) or (nd % i !=0):
            max=i
        i=i+1 
    return max *ChifSum(x)
val=int(input())
r=Proizv(val)
if r <0 :
    print("отсутсвует подходящие число")
else :
    print(r)