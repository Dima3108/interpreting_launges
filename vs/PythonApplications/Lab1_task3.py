def task_4(str):
    count=0
    i=0
    while(i<len(str)):
        if(str[i]>='0'and str[i]<='4'):
            count=count+1
         i=i+1
    return  count


