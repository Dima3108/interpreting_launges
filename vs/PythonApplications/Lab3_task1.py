#https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D1%81%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BF%D1%80%D1%8F%D0%BC%D1%8B%D1%85
#https://programmersforum.ru/showthread.php?t=47317
'''
x1'=Rcos(a) + x0;
y1'=Rsin(a)+y0;
'''
import math
class Point2D:
   def __init__(self,x,y):
     self.x=float(x)
     self.y=float(y)
   def equal_points(self,point2):
      return bool(self.x==point2.x) and bool(self.y==point2.y)
def is_intersection_of_lines(point1l1,point2l1,point1l2,point2l2):
   p1=point1l1.x-point2l1.x
   p2=point1l2.y-point2l2.y
   p3=point1l1.y-point2l2.y
   p4=point1l1.x-point2l2.x
   if((p1*p2)-(p3*p4)==0):
      return False
   else:
      return True
class Triangle:
   def __init__(self,point1,point2,point3):
      self.point1=Point2D(point1.x,point1.y)
      self.point2=Point2D(point2.x,point2.y)
      self.point3=Point2D(point3.x,point3.y)
   def  is_intersect(self,trin):
     points_a=[self.point1,self.point2,self.point3]
     points_b=[self.point1,self.point2,self.point3]
     trpoint_a=[trin.point1,trin.point2,trin.point3]
     trpoint_b=[trin.point1,trin.point2,trin.point3]
     i=0
     j=0
     k=0
     h=0
     while(i<len(points_a)):
        j=0
        while(j<len(points_b)):
           k=0
           while(k<len(trpoint_a)):
              h=0
              while(h<len(trpoint_b)):
                 if((i!=j)and(k!=h)):
                    if(is_intersection_of_lines(points_a[i],points_b[j],trpoint_a[k],trpoint_b[h])):
                       return True
                 h=h+1
              k=k+1
           j=j+1
        i=i+1
     return False  
   def move(self,gradus,point_O):
      R1=math.sqrt(pow(self.point1.x-point_O.x,2)+pow(self.point1.y-point_O.y,2))
      R2=math.sqrt(pow(self.point2.x-point_O,2)+pow(self.point2.y-point_O.y,2))
      R3=math.sqrt(pow(pow(self.point1.x-point_O.x,2)+pow(self.point1.y-point_O.y,2)))
      a=float(float((math.pi*gradus))/float(180.0))
      cos_a=math.cos(a)
      sin_a=math.sin(a)
      self.point1.x=R1*cos_a+self.point1.x
      self.point1.y=R1*sin_a+self.point1.y
      self.point2.x=R2*cos_a+self.point2.x
      self.point2.y=R2*sin_a+self.point2.y
      self.point3.x=R3*cos_a+self.point3.x
      self.point3.y=R3*sin_a+self.point3.y