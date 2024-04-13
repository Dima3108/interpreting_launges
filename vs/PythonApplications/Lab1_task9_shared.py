'''
Прочитать список строк с клавиатуры. Упорядочить по длине 
строки.
'''
lines=[]
line=str(input("Введите строку (-1 признак окончания)\n"))
while(line!="-1"):
    lines.append(line)
    line=input()
if(len(lines)>0):
    ceshl=lines[0]
    i=0
    while(i<len(lines)):
       ceshl=lines[i]
       j=i+1
       while(j<len(lines)):
           if(len(lines[i])<len(lines[j])):
               lines[i]=lines[j]
               lines[j]=ceshl
               ceshl=lines[i]
           j=j+1
       i=i+1
print(lines)


