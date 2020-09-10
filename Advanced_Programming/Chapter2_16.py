import cmath
import math

class Rotate:
    def __init__(self,coordinate):
        self.coordinate=coordinate
    
    def rotate(self,angle):
        tri=complex(math.cos(math.radians(angle)),(math.sin(math.radians(angle))))
       
        if isinstance(self.coordinate,list) and len(self.coordinate)==2:
            temp=complex(self.coordinate[0],self.coordinate[1])
            return temp*tri
        elif isinstance(self.coordinate,complex):
            return self.coordinate*tri
        else:
            print("wrong value")
            return -1
    
    def print_convert(self,angle):
        print("Before Rotate :",end='')
        print(self.coordinate)
        print("After (",angle,")Rotate :",end='')
        print(self.rotate(angle))

if __name__ == "__main__":
    Coordinate_a=1+2j
    Coordinate_b=[1,2]
    Rotate_func=Rotate(Coordinate_a)
    Rotate_func.print_convert(90)
    Rotate_func=Rotate(Coordinate_b)
    Rotate_func.print_convert(30)