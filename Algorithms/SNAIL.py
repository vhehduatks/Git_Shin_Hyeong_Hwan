import sys
read=sys.stdin.readline


def climb(days,climed):
    # global cache
    if days==m:
        return 1 if climed>=n else 0
    
    if cache[days][climed]:
        return cache[days][climed]
    
    ret=0

    ret+=0.25*climb(days+1,climed+1)
    ret+=0.75*climb(days+1,climed+2)
    
    cache[days][climed]=ret

    return ret
    
case_num=int(read())

for _ in range(case_num):
    n,m=map(int,read().split())
    cache=[[None]*(m*2+1) for _ in range(m+1)]
    print(climb(0,0))
    print(cache)
    

###### sol by mathematical

# import math
 
 
# def snail(height, day):  # 비오면(75%) 1미터 안오면 0미터
#     if height <= 0:  # height = 올라가야하는 높이 day=날 수
#         return 1
#     if height > day:  # 탈출이 불가능한 경우
#         return 0
#     prop = 0  # 확률
#     for o in range(height,day+1):
#         prop += (0.75**o)*(0.25**(day-o))*(math.factorial(day)/(math.factorial(o)*math.factorial(day-o)))
#     return prop
 
 
# case = int(input())
# for i in range(case):
#     n,m=map(int, input().split())  # n=높이,m=비오는날
#     result = snail(n - m, m)  # 미리 빼준다
#     print("%.10f"%result)
