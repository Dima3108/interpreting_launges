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



