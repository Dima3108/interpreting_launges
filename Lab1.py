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

3