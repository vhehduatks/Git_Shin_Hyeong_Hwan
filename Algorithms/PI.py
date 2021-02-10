import sys
sys.setrecursionlimit(10**8)
read=sys.stdin.readline
MAX=float('inf')
def classify(N):

    same=True
    mono=True
    cross=True
    arith=True

    previous_1=N[0]
    previous_2=N[1]

    for i in range(2,len(N)):
        
        if not(previous_1==previous_2 and previous_2==N[i]):
            same=False
        # if not(abs(previous_1-previous_2)==1 and abs(previous_1-N[i])==2):
        #     mono=False
        if not(abs(previous_2-N[i])==1):
            mono=False
        if not(N[i]==previous_1):
            cross=False
        if not((previous_1-previous_2)==(previous_2-N[i])):
            arith=False
        previous_1=previous_2
        previous_2=N[i]

    if same:
        return 1
    if mono and arith:
        return 2
    if cross:
        return 4
    if arith:
        return 5
    return 10

# print(classify([2,4,6,8]))

def recur(begin):
    global numbers
    global cache

    if begin==len(numbers):
        return 0

    if cache[begin]:
        return cache[begin]



    ret=MAX

    for N in range(3,6):
        
        if N+begin<=len(numbers):
            temp=list(map(int,list(numbers[begin:begin+N])))
            # print(temp)
            # print(begin+N)
            # print(recur(begin+N)+classify(temp))
            ret=min(ret,recur(begin+N)+classify(temp))
    
    cache[begin]=ret
    return ret


csn=int(read())
for _ in range(csn):
    numbers=read().strip()
    size=len(numbers)
    cache=[None]*(size)
    print(recur(0))
