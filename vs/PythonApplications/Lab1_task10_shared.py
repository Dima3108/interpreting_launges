'''
 Дан список строк с клавиатуры. Упорядочить по количеству 
слов в строке.
'''
lines=[]
line=str(input("Введите строку (-1 признак окончания)\n"))
length_lines=[]
while(line!="-1"):
    lines.append(line)
    if(len(lines)>0):
        length_lines.append(len(line.split()))
    else:
        length_lines.append(0)
    line=input()
if(len(lines)>0):
    i=0
    while(i<len(lines)):
        cesh_length=length_lines[i]
        cesh_val=lines[i]
        j=i+1
        while(j<len(lines)):
            if(length_lines[j]>length_lines[i]):
                length_lines[i]=length_lines[j]
                length_lines[j]=cesh_length
                cesh_length=length_lines[i]
                lines[i]=lines[j]
                lines[j]=cesh_val
                cesh_val=lines[i]
            j=j+1
        i=i+1
print(lines)