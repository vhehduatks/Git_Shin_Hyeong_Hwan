triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    sum=[[0]*len(line) for line in triangle]

    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if(j==0):
                sum[i][j]=sum[i-1][j]+triangle[i][j]
            elif(i==j):
                sum[i][j]=sum[i-1][j-1]+triangle[i][j]
            else:
                sum[i][j]=max(sum[i-1][j-1],sum[i-1][j])+triangle[i][j]
        
    answer=max(sum[-1])
    
    return answer

print(solution(triangle))    
