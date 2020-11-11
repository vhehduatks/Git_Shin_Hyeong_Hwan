R_hand="#"
L_hand="*"
Left=[1,4,7]
mid=[2,5,8,0]
Right=[3,6,9]


def solution(numbers, hand):
    global R_hand
    global L_hand
    global Left
    global Right
    global mid

    answer = ''


    for i in numbers:
        if i in mid:
            answer+=to_dist(i,hand)
        elif i in Left:
            answer+="L"
            L_hand=i
        elif i in Right:
            answer+="R"
            R_hand=i   

    
    return answer

def to_dist(dst,hand):
    global R_hand
    global L_hand
    global Left
    global Right
    global mid
    
    L_dis=0
    R_dis=0
    if L_hand in Left:
        #dst-L=1이면 한칸
        if dst-L_hand==1:
            L_dis=1
        elif dst-L_hand==4 or dst-L_hand== -2 or dst-L_hand==-7:
            L_dis=2
        elif dst-L_hand==7 or dst-L_hand==-5 or dst-L_hand==-4:
            L_dis=3
        elif dst-L_hand==-1:
            L_dis=4          
    elif L_hand in mid:
        if abs(dst-L_hand)==3 or abs(dst-L_hand)==8:
            L_dis=1
        elif abs(dst-L_hand)==6 or abs(dst-L_hand)==5:
            L_dis=2  
        elif abs(dst-L_hand)==2:
            L_dis=3
        elif dst-L_hand==0:
            L_dis=0
    else:
        if dst==2:
            L_dis=4
        elif dst==5:
            L_dis=3
        elif dst==8:
            L_dis=2
        else:
            L_dis=1    


    if R_hand in Right:
        #dst-R=1이면 한칸
        if dst-R_hand==-1:
            R_dis=1
        elif dst-R_hand==-4 or dst-R_hand== 2 or dst-R_hand==-9:
            R_dis=2
        elif dst-R_hand==-7 or dst-R_hand==5 or dst-R_hand==-6:
            R_dis=3
        elif dst-R_hand==-3:
            R_dis=4          
    elif R_hand in mid:
        if abs(dst-R_hand)==3 or abs(dst-R_hand)==8:
            R_dis=1
        elif abs(dst-R_hand)==6 or abs(dst-R_hand)==5:
            R_dis=2  
        elif abs(dst-R_hand)==2:
            R_dis=3
        elif dst-R_hand==0:
            R_dis=0
    else:
        if dst==2:
            R_dis=4
        elif dst==5:
            R_dis=3
        elif dst==8:
            R_dis=2
        else:
            R_dis=1  

    if L_dis<R_dis:
        L_hand=dst
        return "L"  
    elif L_dis>R_dis:
        R_hand=dst
        return "R"
    else:
        if hand=="left":
            L_hand=dst
            return "L"
        else:
            R_hand=dst
            return "R"

numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand="right"
print(solution(numbers,hand))