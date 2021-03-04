import sys
sys.setrecursionlimit(10**8)
read=sys.stdin.readline
dp=[None]*11


# def top_down(N):
#     # print('N:',N)
#     if N==0:
#         return 0

#     if dp[N]:
#         return dp[N]

#     ret=0
#     for i in range(0,n):
#         if N-(i+1)>=0:
#             print(i)
#             print(p[i])
#             ret=max(ret,top_down(N-(i+1))) +p[i]
#     print('end')
#     print(N,ret)
#     dp[N]=ret
#     return ret

# N=int(read())
# p=list(map(int,read().split()))
# n=len(p)
# print(top_down(N))
# print(dp)


def top_down(N):
    # print('N:',N)
    if N==0:
        return 0

    if dp[N]:
        return dp[N]

    ret=0
    for i in range(4):
        print('N',N)
        print('i',i)
        print('p:',p[i])
        ret=max(ret,top_down(N-1)+p[i])
    print('end')
    print(N,ret)
    dp[N]=ret
    return ret

p=[1,5,6,7]
print(top_down(int(read())))
print(dp)