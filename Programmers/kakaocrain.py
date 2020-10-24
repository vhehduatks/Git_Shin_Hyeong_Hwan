
board=[ [0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]	
moves=[1,5,3,5,1,2,1,4]


def solution(board, moves):
    temp=[-1]
    t=list()
    answer = 0
    for i in moves:
        for j in range(len(board)):
            item=board[j][i-1]
            if item!=0:
                if temp[-1]==item:
                    answer+=2
                    t.append(temp.pop())
                    board[j][i-1]=0
                    break
                temp.append(item)
                board[j][i-1]=0
                break
            
    return answer

print(solution(board,moves))