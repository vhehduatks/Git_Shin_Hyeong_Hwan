"""
n만큼의 -1로 초기화된 리스트 하나
case 배송여부 0 인데 요소가 -1,-1이면 아무것도 안함
배송여부 1이면 요소 1로 바꿔줌
배송여부 0인데 요소가 1,-1이면 -1을 0으로 바꿈
"""
import math
n=7	
delivery=[[5, 6, 0], [1, 3, 1], [1, 5, 0], [7, 6, 0], [3, 7, 1], [2, 5, 0]]
def solution(n, delivery):
    check_list=[-1 for _ in range(n)]
    temp=int(math.sqrt(n))
    while(temp>0):
        for i in delivery:
            if i[2]==0:
                if check_list[i[0]-1]+check_list[i[1]-1]==-2:
                    continue
                elif check_list[i[0]-1]+check_list[i[1]-1]==0:
                    if check_list[i[0]-1]==-1:
                        check_list[i[0]-1]=0
                    else:
                        check_list[i[1]-1]=0    

            elif i[2]==1:
                check_list[i[0]-1]=1
                check_list[i[1]-1]=1
        temp-=1        
                

                   

    answer=""
    for i in check_list:
        if i==-1:
            answer+="?"
        elif i==0:
            answer+="X"
        else:
            answer+="O" 
    return answer

solution(n,delivery)    