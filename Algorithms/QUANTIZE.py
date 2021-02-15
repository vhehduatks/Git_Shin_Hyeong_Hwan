import sys
read=sys.stdin.readline

INF=float('inf')
def error(start,size):
    global S
    global SS
    m=(S[start-1+size]-S[start-1])/size
    ret=SS[start-1+size]-SS[start-1]+size*m-2*(S[start-1+size]-S[start-1])*m

    return int(ret)

def partsum(nums):
    S=list()
    SS=list()
    sum=0
    for i in nums:
        sum+=i
        S.append(sum)
        SS.append(sum*sum)

    print(S)
    print(SS)
    return S,SS

def recur(start,parts):
    global nums
    global cache
    # print(start,parts)
    if start==num_len:
        print('work')
        return 0
    
    if cache[parts][start]:
        return cache[parts][start]

    ret=INF
    for Size in range(1,num_len-start+1):
        if start+Size<=num_len and parts>0:
            print(start,Size)
            ret=min(ret,recur(start+Size,parts-1)+error(start,Size))
    
    cache[parts][start]=ret
    return ret

case_num=int(read())

for _ in range(case_num):
    num_len,parts=map(int,read().split())
    nums=list(map(int,read().split()))
    
    cache=[[None]*(num_len+1) for _ in range(parts+1)]
    
    S,SS=partsum(nums)
    print(recur(0,parts))
    print(cache)