import turtle as t
import random as rd

height=300  
width=300

def draw_screen():
    screen=t.Turtle(visible=False)
    screen.speed("fastest")
    screen.penup()
    screen.goto(-width,-height)
    p=screen.pos()
    screen.write(str(p),False)
    screen.pendown()
    screen.goto(width,-height)
    p=screen.pos()
    screen.write(str(p),False)
    screen.goto(width,height)
    p=screen.pos()
    screen.write(str(p),False)
    screen.goto(-width,height)
    p=screen.pos()
    screen.write(str(p),False)
    screen.goto(-width,-height)
    
#https://m.blog.naver.com/PostView.nhn?blogId=mk1017sh&logNo=221593855270&proxyReferer=https:%2F%2Fwww.google.com%2F 터틀연습
class Turtle():
    MAX=100
    MIN=1

    
    def __init__(self,color,num,shape='classic'):
       self.color=color
       self.num=num
       self.T=t.Turtle()
       self.shape=shape
       self.T.turtlesize(0.5,0.5)
       self.T.shape(self.shape)
       self.T.pencolor(self.color)
       self.T.speed('fastest')
       self.T.fillcolor(self.color)

    #https://stackoverflow.com/questions/14713037/python-turtle-set-start-position 시작위치
    def __set_pos(self):
        self.T.penup()
        self.T.goto(rd.randint(-width/2,width/2),rd.randint(-height/2,height/2))
        self.T.pendown()

    
    #https://wikidocs.net/20396 터틀연습
    #https://stackoverflow.com/questions/48123809/how-to-display-turtle-coordinates-on-the-canvas 좌표그리기
    def draw(self,strmp=False,penup=False):
        self.__set_pos()
         

        for _ in range(self.num):
            if penup==True:
                self.T.penup()
            if strmp==True:
                self.T.stamp()    
            move=rd.randint(self.MIN,self.MAX)
            angle=rd.randint(0,360)
            self.T.right(angle)
            self.T.forward(move)
            x,y=self.T.position()
            if abs(x)>=width-100 or abs(y)>=height-100:
                self.T.goto(rd.randint(-width/2,width/2),rd.randint(-height/2,height/2))
            coordinate="("+str('%.1f'%x)+","+str('%.1f'%y)+")"
            self.T.write(coordinate,False)
          
            

        
if __name__ == "__main__":
    draw_screen()
    color_list=["black","red","blue","green","gray","pink"]

    for i in color_list:
        TT=Turtle(i,20,"turtle")
        TT.draw(True,True)
    t.done()    


