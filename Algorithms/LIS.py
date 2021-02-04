import sys
read=sys.stdin.readline

# cache=[]
# arr=[]


def lis(start):
    global cache
    global arr
    global lnum

    # print(start)
    
    if not(cache[start]==-1):
        
        return cache[start]

    cache[start]=1
    # if start==lnum-1:
    #     print('end')
    #     return 1

    # temp=arr[start]이거때문에 에러생겼음 max(cache[start],temp) 에서 temp가 두번 사용되서
    # arr[start] 값인 5가 계속 max로 남아있었음
    
    for i in range(start+1,lnum):
       
        if arr[start]<arr[i]:
            
            temp=lis(i)+1
            # print(start,'temp',temp)
            cache[start]=max(cache[start],temp) 

    # print('out',cache[start])
    return cache[start]

cs=int(read())
for _ in range(cs):
    lnum=int(read())
    cache=[-1]*(lnum)
    arr=list(map(int,read().split()))
    ret_list=list()
    for i in range(lnum):
        ret_list.append(lis(i))
    print(max(ret_list))
    


