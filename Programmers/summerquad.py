import math
w=100000000
h=1
def solution(w,h):
    total=w*h
    count=0
    bf_y=0
    for i in range(w+1):
        x=i
        y=(h/w)*x
        count+=math.ceil(y)-math.floor(bf_y)
        print(count)       
        bf_y=y

    
    return total-count
print(solution(w,h))

