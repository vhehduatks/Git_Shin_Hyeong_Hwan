import sys
read=sys.stdin.readline

def Bottom_up(n):

    sum=0
    for n in range(1,n+1):
        for k in range(10):
            if n==1:
                if k==0:
                    cache[n][k]=0
                else:
                    cache[n][k]=1
                continue
            if k==0:
                cache[n][k]=cache[n-1][1]
                continue
            if k==9:
                cache[n][k]=cache[n-1][8]
                continue
            cache[n][k]=cache[n-1][k-1]+cache[n-1][k+1]
    
    for k in range(10):
        sum+=cache[n][k]
    return sum

cache=[[None]*10 for _ in range(101)]
test_case=int(read())
print(Bottom_up(test_case)%1000000000)