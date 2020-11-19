import math as m
class Circle:
    PI=3.14
    def __init__(self,x,y,radius):
        self.__x=x
        self.__y=y
        self.__radius=radius
    
    def __str__(self):
        string="Circle : ( x="+str(self.__x)+", y="+str(self.__y)+", r="+str(self.__radius)+"), 면적:"
        string+=str(self.area())
        return string
    
    def set_x(self,new_x):
        self.__x=new_x
    
    def set_y(self,new_y):
        self.__y=new_y
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def set_radius(self,new_rad):
        self.__radius=new_rad

    def get_radius(self):
        return self.__radius
    
    def area(self):
        return (self.__radius)*(self.__radius)*self.PI
    #클래스에서 다른 클래스변수를 호출하기 위해선 그냥 매개변듯에 해당 클래스 변수를 호출하면 되는듯
    def overlaps(self,other):
        dx=(self.__x-other.__x)**2+(self.__y-other.__y)**2
        rdx=(self.__radius+other.__radius)**2
        return True if rdx-dx>0 else False

    def contains(self,other):
        dx=(self.__x-other.__x)**2+(self.__y-other.__y)**2
        return True if self.__radius>(other.__radius+m.sqrt(dx)) else False

c1= Circle(0,0,100)
c2= Circle(0,-10,10)
c3= Circle(-100,0,120)

print("C1:",c1)
print("C2:",c2)
print("C3:",c3)

print("c1 contaions c2:",c1.contains(c2))
print("c1 contaions c3:",c1.contains(c3))
print("c1 overlaps c2:",c1.overlaps(c2))
print("c1 overlaps c3:",c1.overlaps(c3))