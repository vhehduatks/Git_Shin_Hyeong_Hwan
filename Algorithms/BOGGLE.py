import sys
#함수를 호출하고 어떤 작업을 수행시키기 위해서는, 이름 끝에 ()를 붙여야한다.
read=sys.stdin.readline

#입력처리 구간
word_num=int(read())
word_list=[read().strip() for _ in range(word_num+1)]
word_list.pop(len(word_list)-1)

BOGGLE_num=int(read())
BOGGLE_list=list()
BOGGLE_text=list()
for i in range(BOGGLE_num*4):
    if (i!=0) and (i%4==0):
        _=read()
    BOGGLE_text.append(read().strip())
    if len(BOGGLE_text)==4:
        BOGGLE_list.append(BOGGLE_text)
        BOGGLE_text=[]


#단락을 나누기위한 기준 추가
# BOGGLE_text.append('')
# BOGGLE_list=list()
# temp=list()
# #''을 기준으로 보글 표를 2차원 행렬로 가눔
# for line in BOGGLE_text:
#     if line=='':
#         BOGGLE_list.append(temp)
#         temp=[]
#     else:
#         temp.append(list(line))


SCORE={1:0,2:0,3:1,4:1,5:2,6:3,7:5,8:11}

def find_word(word_list,BOGGLE_list):
    for BOGGLE in BOGGLE_list:
        score=0
        in_word_list=[]
        longest=''
        for word in word_list:
            temp_word=list(word)
            for n in range(16):
                BOGGLE_row=n//4
                BOGGLE_col=n%4
                if word in in_word_list:
                    break
                if(hasword(BOGGLE_row,BOGGLE_col,temp_word,BOGGLE)):
                    if len(longest)<=len(word):
                        if len(longest)==len(word):
                            if longest>word:
                                longest=word
                        elif len(longest)!=len(word):
                            longest=word               
                    in_word_list.append(word)
                    score+=SCORE[len(word)]
                    
        print(score,longest,len(in_word_list))
    

def in_range(row,col):
    if (0<=row<=3) and (0<=col<=3):
        return True
    return False

#단어를 찾는 좌표
dx=[-1,-1,-1,1,1,1,0,0]
dy=[-1,0,1,-1,0,1,-1,1]

def hasword(row,col,word,BOGGLE):
    if not(in_range(row,col)):
        return False
    #앞글자부터 짤라가기 때문에 이걸로 검사하는거임
    if BOGGLE[row][col]!=word[0]:
        return False
   
    #단어를 하나씩 pop해서 없에는데 단어의 문자가 1개 남았고 BOGGLE[row][col]!=word[0] 조건을 통과했으면
    #단어의 모든 문자열이 정답이라는 뜻
    if len(word)==1:
        return True
    if len(word)>1:
        word.pop(0)
    #8방향 확인
    for i in range(8):
        next_row=row+dy[i]
        next_col=col+dx[i]
        
        if(hasword(next_row,next_col,word,BOGGLE)):
            return True
    return False


find_word(word_list,BOGGLE_list)