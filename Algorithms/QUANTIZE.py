import sys
read=sys.stdin.readline

INF=float('inf')
def error(start,size):
    global S
    global SS
    m=(S[start+size]-S[start])/size
    ret=SS[start+size]-SS[start]+size*m-2(S[start+size]-S[start])*m

    return int(ret)

def partsum(nums):
    S=list()
    SS=list()
    sum=0
    for i in nums:
        sum+=i
        S.append(sum)
        SS.append(sum*sum)

    return S,SS

def recur(start,parts):
    global nums
    global cache

    if start==num_len:
        return 0

    if cache[start][parts]:
        return cache[start][parts]

    ret=INF
    for Size in range(1,num_len-start):
        if start+Size<=num_len and parts>0:
            ret=min(ret,recur(start+Size,parts-1)+error(start,Size))
    
    return ret

case_num=int(read())

for _ in range(case_num):
    num_len,parts=map(int,read().split())
    nums=list(map(int,read().split()))
    cache=[[None]*parts for _ in range(num_len)]
    S,SS=partsum(nums)
    print(recur(0,parts))