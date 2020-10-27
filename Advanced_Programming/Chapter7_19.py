from tkinter import *

Msec =0
Sec=0
Min=0
b_working=False
Reset=False
#전역변수는 스코프관계상 함수안에서 읽을수만 있고 변경하려면 global 선언하여야 함
def increase_time():
    global Msec
    global Sec
    global Min
    global b_working
    global Reset
    #.after 함수가 루프를 도는게 아님 함수가 완료된 이후 일정시간 후에 다시 실행시키는듯
    #https://www.tutorialspoint.com/after-method-in-python-tkinter
    label.after(10,increase_time)
    if b_working==True:
        Msec+=1
        Sec +=(Msec//100)
        Msec%=100
        Min +=(Sec//60)
        Sec %=60

    if Reset==True:
        Msec=Sec=Min=0
        Reset=False
#정수형 자릿수표현
    text_input=str('%02d'%Min)+":"+str('%02d'%Sec)+":"+str('%02d'%Msec)
    label.config(text=text_input)

def Toggling():
    global b_working
    if b_working==False:
        b_working=True
    else:
        b_working=False

def Reseting():
    global Reset
    Reset=True          

#https://pythonexamples.org/python-tkinter-set-window-size/
window =Tk()
window.title("Timer")
window.geometry("700x300")

label=Label(window, text="0",fg="black",font="Arial 120 bold")
label.pack()

button1 = Button(window, text="Toggle", command=Toggling)
button1.pack()
button2 = Button(window, text="Reset", command=Reseting)
button2.pack()

increase_time()
window.mainloop()