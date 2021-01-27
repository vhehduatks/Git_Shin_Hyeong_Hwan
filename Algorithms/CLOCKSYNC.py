#시간초과됨

import sys
read=sys.stdin.readline

switch=[
[0,1,2],
[3,7,9,11],
[4,10,14,15],
[0,4,5,6,7],
[6,7,8,10,12],
[0,2,14,15],
[3,14,15],
[4,5,7,14,15],
[1,2,3,4,5],
[3,4,5,9,13]
]
INF=float('inf')
case_num=int(read())

def push(time_now,switch_num):
   for clock in switch[switch_num]:
       time_now[clock]+=3
       if time_now[clock]==15:
           time_now[clock]=3

def is_sort(time_now):
    for time in time_now:
        if not(time==12):
            return False
    return True


def recur(time_now,switch_num):

    if switch_num==len(switch):
        return 0 if is_sort(time_now) else INF

    ret=INF
    for i in range(4):
        temp_ret=(i+recur(time_now,switch_num+1))
        ret=min(temp_ret,ret)
        push(time_now,switch_num)
    
    return ret
    
for _ in range(case_num):
    time_now=list(map(int,read().strip().split()))
    result=recur(time_now,0)
    print(result if result<INF else -1)
