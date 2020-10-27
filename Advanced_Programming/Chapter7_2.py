import time

def sum1to1000000(num): 
    SUM=0
    while(num>=0):
        MAX=1000000
        MIN=1
        SUM=(MIN+MAX)*(MAX-MIN+1)//2
        num-=1
    print("sum1to1000000 :",SUM) 
    return SUM

start=time.time()
#100번실행하면 시간이 안찍힘
sum1to1000000(10000) 
print("코드의 실행속도 :",'%.8f'%(time.time()-start),"초")
   
  
    