user=""
tovar=""
count=int(0)
endchar="-1"
users=[]
tovars=[]
counts=[]
print("введите -1 для завершения")
s=input("Введте имя пользователя\n")
while(s!=endchar):
    user=s
    tovar=""
    s=input("Введите название товара\n")
    if(s==endchar):
        break

    tovar=s
    count=int(0)
    s=input("Введите количество товаров\n")
    if(s==endchar):
        break
    count=int(s)
    if(user!="" and tovar != ""):
        users.append(user)
        tovars.append(tovar)
        counts.append(count)
    user=""
    s=input("Введте имя пользователя\n")
if(user!="" and tovar != ""):
        users.append(user)
        tovars.append(tovar)
        counts.append(count)
if(len(users)>0):
     start_count=int(len(users))
     end_count=int(len(users))
     delete_position=[]
     i=0
     j=0
     while(i<len(users)):
          j=i+1
          stat=-1
          for el in delete_position:
               if(el==j):
                    stat=1
                    break
          if(stat==-1):
            while(j<len(users)):
               if(users[i]==users[j] and tovars[i]==tovars[j]):
                    counts[i]=counts[i]+counts[j]
                    delete_position.append(j)
               j=j+1
          i=i+1
     for pos in delete_position:
      users.pop(pos)
      tovars.pop(pos)
      counts.pop(pos)
     end_count=int(len(users))
     while(start_count!=end_count):
            start_count=end_count
            delete_position=[]
            i=0
            j=0
            while(i<len(users)):
               j=i+1
               stat=-1
               for el in delete_position:
                 if(el==j):
                    stat=1
                    break
               if(stat==-1):
                 while(j<len(users)):
                   if(users[i]==users[j] and tovars[i]==tovars[j]):
                     counts[i]=counts[i]+counts[j]
                     delete_position.append(j)
                   j=j+1
               i=i+1
            for pos in delete_position:
              users.pop(pos)
              tovars.pop(pos)
              counts.pop(pos)
            end_count=int(len(users))
     i=0
     while(i<len(users)):
         print(str(users[i])+" "+str(tovars[i])+" "+str(counts[i]))
         i=i+1   
else:
     print("Пользователи отсутсвуют")