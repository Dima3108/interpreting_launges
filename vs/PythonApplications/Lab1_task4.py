#1,5,9,10
tableg = "aeiuoаюэуеыояи"
tablesg = "qwrtpsdfghjklzxcvbnmйцкнгшщзхъфвпрлджэчсмтьб"
#В порядке увеличения разницы между количеством согласных и
#количеством гласных букв в строке.
def task_1(str):
    strlow=str.low()
    sarray=strlow.split('\n')
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
   if(len(str)<=0):
      return ""
   char_table=[str[0]]
   i=1
   while(i<len(str)):
       j=0
       stat=-1
       while(j<len(char_table)):
            if(char_table[j]==str[i]):
                 stat=1
                 break
            j=j+1
       if(stat==-1):
           char_table.append(str[i])
       i=i+1
   j=0
   #Подсчет частот
   glob_freqs=[]
   while(j<len(char_table)):
        count=0
        i=0
        while(i<len(str)):
            if(str[i]==char_table[j]):
                count=count+1
            i=i+1
        j=j+1
        glob_freqs.append(count)
    #разбиение на строки
   strings_=str.split('\n')
   def compute_freq_in_string(string_,gl_ch,gl_fr):
       local_chars=[string_[0]]
       i=1
       while(i<len(string_)):
           s=1
           j=0
           while(j<len(local_chars)):
               if(local_chars[j]==string_[i]):
                   s=-1
                   break
               j=j+1
           if(s==1):
               local_chars.append(string_[i])
           i=i+1
       local_freqs=[]
       j=0
       while(j<len(local_chars)):
           lcount=0
           i=0
           while(i<len(string_)):
               if(string_[i]==local_chars[j]):
                   count=count+1
               i=i+1
           j=j+1
           local_freqs.append(count)
       max_freq=local_freqs[0]
       max_freq_indecs=0
       i=0
       while(i<len(local_freqs)):
           if(max_freq<local_freqs[i]):
               max_freq=local_freqs[i]
               max_freq_indecs=i
           i=i+1
       j=0
       while(gl_ch[j]!=local_chars[max_freq_indecs]):
           j=j+1
       return (gl_fr[j]-local_freqs[max_freq_indecs])*(gl_fr[j]-local_freqs[max_freq_indecs])
   deltas=[]
   i=0
   while(i<len(strings_)):
       deltas.append(compute_freq_in_string(strings_[i]))
       i=i+1
   new_str=[]
   count=0
   l=len(strings_)
   while(count<l):
       max=deltas[0]
       i=0
       max_pos=0
       while(i<len(strings_)):
           if(max<deltas[i]):
               max=deltas[i]
               max_pos=i
           i=i+1
       new_str.append(strings_[max_pos])
       strings_.pop(max_pos)
       deltas.pop(i)
       l=l+1
   return new_str   

   
   
