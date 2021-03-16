import sys
read=sys.stdin.readline

dic={}
N=int(read())
max_v=0
for _ in range(N):
    
    n=int(read())
    if not dic.get(n):
        dic[n]=1
        max_v=max(max_v,dic[n])
    else:
        dic[n]+=1
        max_v=max(max_v,dic[n])
    
max_list=[k for k,v in dic.items() if max_v==v]
# print('m',max_v,max_list)
print(min(max_list))