
# dp=[None]*31
# def top_down(n):
#     if n<=0:
#         return 1 if n==0 else 0
#     if dp[n]:
#         return dp[n]

#     ret=0
#     ret+=3*top_down(n-2)+2*top_down(n-4)+2*top_down(n-6)
#     dp[n]=ret
    
#     return ret

# print(top_down(int(input())))


dp=[0]*31
def bottom_up(n):
    dp[2]=3
    for i in range(3,n+1):
        if i%2==0:
            Sum=0
            j=i-4
            while j>=2:
                Sum+=2*dp[j]
                j-=2
            dp[i]=dp[i-2]*dp[2]+Sum+2
    return dp[n]
print(bottom_up(int(input())))

