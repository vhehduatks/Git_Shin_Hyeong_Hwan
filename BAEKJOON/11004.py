import sys
read=sys.stdin.readline

N,K=map(int,read().split())
A=list(map(int,read().split()))
# #1
# A.sort()
# print(A[K-1])

#2
def merge(L,R):
    L_p=0
    R_p=0
    temp=list()

    while L_p<len(L) and R_p<len(R):
        if L[L_p]<R[R_p]:
            temp.append(L[L_p])
            L_p+=1
        else:
            temp.append(R[R_p])
            R_p+=1
    
    while L_p<len(L):
        temp.append(L[L_p])
        L_p+=1
    while R_p<len(R):
        temp.append(R[R_p])
        R_p+=1

    return temp

def merge_sort(unsorted):
    if len(unsorted)==1:
        return unsorted
    mid=len(unsorted)//2
    
    L=unsorted[:mid]
    R=unsorted[mid:]
    L_1=merge_sort(L)
    R_1=merge_sort(R)
    
    return merge(L_1,R_1)

sorted_A=merge_sort(A)
print(sorted_A[K-1])