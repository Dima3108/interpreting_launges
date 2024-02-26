#1,5,9,10
tableg = "aeiuoаюэуеыояи"
tablesg = "qwrtpsdfghjklzxcvbnmйцкнгшщзхъфвпрлджэчсмтьб"
#В порядке увеличения разницы между количеством согласных и
#количеством гласных букв в строке.
def task_1(str):
    strlow=str.low()
    sarray=strlow.split(' ')
    delta_a=[]
    for s in sarray :
        countq=0
        countsq=0
        i=0
        while(i<len(s)):
            if(tableg.__contains__(s[i])):
                countq=countq+1
            elif(tablesg.__contains__(s[i])):
                countsq=countsq+1
            i=i+1
        delta_a.append(countq-countsq)
    l=0
    sortsarray=[]
    while(l<len(sarray)):
        val=sarray[l]
        j=l+1
        while(j<len(sarray)):
            if(delta_a[j]<delta_a[l]):
                tmp=delta_a[j]
                delta_a[j]=delta_a[l]
                delta_a[l]=tmp
                sarray[l]=sarray[j]
                sarray[j]=val
                val=sarray[l]
            j=j+1
        sortsarray.append(val)
        l=l+1
    result = ""
    for s in sortsarray:
        result=result+s+" "
    return  result
#В порядке увеличения квадратичного отклонения частоты
#встречаемости самого часто встречаемого в строке символа от частоты его
#встречаемости в текстах на этом алфавите.
def task_5(str):
