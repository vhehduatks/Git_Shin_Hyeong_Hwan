import sys
read=sys.stdin.readline
sys.setrecursionlimit(10**7)

A=read().strip()
dp=[0]*(10001)
def is_alpha_2(idx):
    temp=int(A[idx:idx+2])
    return True if 10<=temp and temp <=26 else False

def is_alpha_1(idx):
    temp=int(A[idx])
    return True if 1<=temp and temp<=9 else False

def top_down(idx):
    if idx==len(A):
        return 1
    if dp[idx]:
        return dp[idx]

    ret=0

    if is_alpha_1(idx):
        ret+=top_down(idx+1)
    if is_alpha_2(idx):
        ret+=top_down(idx+2)

    dp[idx]=ret

    return ret

print(top_down(0)%1000000)