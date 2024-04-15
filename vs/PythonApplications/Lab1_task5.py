# -*- coding: utf-8 -*-
# 10, 22, 34, 46, 58
import random
atasks_=[10,22,34,46,58]
def task_manager_get_task():
   
    print("Выберите задачу, которую хотите решить\n")
    global atasks_
    i=0
    while(i<atasks_.__len__()):
        
        print("у задачи ")
        
        print(atasks_[i])
        
        print(" код равен")
        
        print(i)
        print("\n")
        i=i+1
    numt=-1
    while(numt<0 or numt>=atasks_.__len__()):
          
          print("Введите код задачи\n")
          
          numt=int(input())
    return atasks_[numt]
def task_10(array1,array2):
     '''Даны два массива. Необходимо найти количество совпадающих по 
значению элементов'''
     count=0
     i=0
     j=0
     while(i<len(array1)):
          j=0
          while(j<len(array2)):
               if(array1[i]==array2[j]):
                    count=count+1
               j=j+1
          i=i+1
     return count
def task_22(array1,a,b):
     _start=min(a,b)
     _stop=max(a,b)
     i=_start
     min_v=array1[_start]
     while(i<_stop):
          if(min_v>array1[i]):
               min_v=array1[i]
          i=i+1
     i=_start
     _count=0
     while(i<_stop):
          if(array1[i]==min_v):
               _count=_count+1
          i=i+1
     return _count
def task_34(array1,a,b):
     '''Дан целочисленный массив и отрезок a..b. Необходимо найти 
элементы, значение которых принадлежит этому отрезку'''
     i=0
     indexces_=[]
     while(i<len(array1)):
          if(array1[i]>=a and array1[i]<=b):
               indexces_.append(i)
          i=i+1
     return indexces_
def task_46(array1):
     '''Дан целочисленный массив. Необходимо вывести вначале его 
положительные элементы, а затем – отрицательные.
'''
     new_array=[]
     i=0
     while(i<len(array1)):
          if(array1[i]>=0):
               new_array.append(array1[i])
          i=i+1
     i=0
     while(i<len(array1)):
          if(array1[i]<0):
               new_array.append(array1[i])
          i=i+1
     return array1
def task_58(array1):
     '''Для введенного списка вывести количество элементов, которые могут 
быть получены как сумма двух любых других элементов списка'''
     count=0
     i=0
     while(i<len(array1)):
          j=0
          while(j<len(array1)):
               t=0
               while(t<len(array1)):
                    if(i!=j and j!=t and t!=i):
                         if(array1[i]==(array1[j]+array1[t])):
                              count=count+1
                    t=t+1
               j=j+1
          i=i+1
     return count
def get_random_array():
    array = [0] * 1024
    for i in range(len(array)):
        array[i] = random.randint(0, 255)
    return array
def print_array(array):
    for i, num in enumerate(array):
        print(str(num) + " ", end="")
        if (i + 1) % 32 == 0:
            print()

task_=task_manager_get_task()
if(task_==10):
    array1=get_random_array()
    array2=get_random_array()
    print("array1:\n")
    print_array(array1)
    print("\narray2:\n")
    print(array2)
    count=task_10(array1,array2)
    print("количество совпадающих по значению элнментов:")
    print(str(count))
    print("\n")
elif(task_==22):
     array1=get_random_array()
     a=int(input("Введите a(нижнея граница интервала - целое число):\n"))
     b=int(input("Введите b(верхнея граница интервала - целое число):\n"))
     print("array1:\n")
     print_array(array1)
     count_=task_22(array1,a,b)
     print("Количество элементов с минимальным значением на интервале:")
     print(str(count_)+"\n")
elif(task_==34):
     array1=get_random_array()
     a=int(input("Введите a(нижнея граница интервала - целое число):\n"))
     b=int(input("Введите b(верхнея граница интервала - целое число):\n"))
     print("array1:\n")
     print_array(array1)
     elements_=task_34(array1,a,b)
     print("Элементы значение которых принадлежит интервалу:\n")
     print_array(elements_)
elif(task_==46):
     array1=get_random_array()
     print("array1:\n")
     print_array(array1)
     array2=task_46(array1)
     print("\nnew array:\n")
     print_array(array2)
else:
     vector_=[]
     print("Введите целочисленные элементы списка (-1 признак конца)")
     value=int(input())
     while(value!=-1):
          vector_.append(value)
          value=int(input("\n"))
     print_array(vector_)
     count=task_58(vector_)
     print("количество элементов:")
     print(str(count)+"\n")

     
