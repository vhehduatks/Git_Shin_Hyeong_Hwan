import sys
read=sys.stdin.readline


def tiling(size):
    if size==0:
        return 1
    if cache[size]:
        return cache[size] 
    ret=0
    for i in range(1,3):
        if size-i>=0:
            ret+=tiling(size-i)
    cache[size]=ret
    return ret

def asymtiling(size):
    if size%2==1:
        return tiling(size)-tiling(int(size/2))
    
    return tiling(size)-tiling(int(size/2)-1)-tiling(int(size/2))


case_num=int(read())
for _ in range(case_num):
    size=int(read())
    cache=[None]*(size+1)
    # print(cache)
    print(asymtiling(size)%1000000007)