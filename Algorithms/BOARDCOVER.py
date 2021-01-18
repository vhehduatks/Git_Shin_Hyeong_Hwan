# https://hellominchan.tistory.com/263


"""
3
3 7
#.....#
#.....#
##...##
3 7
#.....#
#.....#
##..###
8 10
##########
#........#
#........#
#........#
#........#
#........#
#........#
##########

"""
import sys
read=sys.stdin.readline




def in_range(x,y,H,W):
    
    if (0<=x and x<W)and(0<=y and y<H):
        return True
    return False

dx=[[0,1,1],[0,0,1],[0,0,1],[-1,0,0]]
dy=[[0,0,-1],[0,-1,-1],[0,-1,0],[-1,0,-1]]

def DFS(H,W,board):
    row=-1
    col=-1
    for y in range(H):
        loop_out=False
        for x in range(W):
            if not board[y][x]:
                row=y
                col=x
                loop_out=True
                break
        if loop_out:
            break
    
    if row==-1 and col==-1:
        return 1

    # print(col,row)
    total=0
    # print(board)
    for case in range(4):
        # print("work?")
        check=False
        for coord in range(3):
            temp_x=dx[case][coord]
            temp_y=dy[case][coord]
            x=col+temp_x
            #y는 다음행으로 넘어가는게 -가 아니라 +임
            y=row-temp_y
            # print("C:",x,y)
            #ㄱ자가 범위를 벗어난경우 
            if not(in_range(x,y,H,W)):
                
                break
                
            #겹친경우
            if board[y][x]:
                
                break

            #마지막 좌표까지 통과될 경우    
            if coord==2:
                # print("pass?")
                check=True
        
        if check:
            for coord in range(3):
                # print(case,coord)
                board[row-dy[case][coord]][col+dx[case][coord]]=1
                # print(board)
            
            total+=DFS(H,W,board)
            #만약 DFS가 끝까지 성공했다면 상단의 return 1을 반환하고 끝났을것임
            #여기까지 내려왔다는건 DFS 재귀를 종료했다는 뜻이므로 성공해서 1을 반환했던 실패해서 아무것도 못했던
            #보드는 원상복귀 하여야 다음 rotate에서 쓸수 있다.
            for coord in range(3):
                board[row-dy[case][coord]][col+dx[case][coord]]=0

        
    return total
    






case_num=int(read())

for _ in range(case_num):
    H,W=map(int,read().split())
    
    board=list()
    #make board
    board_sum=0
    
    for _ in range(H):
        line=read().strip()
        line=line.replace("#","1")
        line=line.replace(".","0")
        line=list(line)
        line=list(map(int,line))
        board.append(line)
        board_sum+=sum(line)
        
    if (H*W-board_sum)%3:
        print(0)
        continue

    print(DFS(H,W,board))

    

    

