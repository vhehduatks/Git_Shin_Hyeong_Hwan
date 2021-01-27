import sys
read=sys.stdin.readline



def Dac(left,right):
    global height_list
    # print(left,right)
    if(left==right):
        # print("work")
        return height_list[left]
    
    mid=int((right+left)/2)
    # print(mid)
    case_left=Dac(left,mid)
    case_right=Dac(mid+1,right)
    # ret=case_left if case_left>case_right else case_right
    ret=max(case_left,case_right)

    over_left=mid
    over_right=mid+1
    height=height_list[over_left] if height_list[over_left]<height_list[over_right] else height_list[over_right]
    temp_ret=(height*2)
    # ret=ret if temp_ret<ret else temp_ret
    ret=max(ret,temp_ret)

    while(left<over_left or over_right<right):
        # print(left,over_left,over_right,right)
        if (over_right<right) and (over_left==left or height_list[over_left-1]<height_list[over_right+1]):
            over_right+=1
            height=min(height,height_list[over_right])

        elif (left<over_left) and (over_right==right or height_list[over_right+1]<=height_list[over_left-1]):
            over_left-=1
            height=min(height,height_list[over_left])
        
        temp_ret=(height*(over_right-over_left+1))

        ret=max(ret,temp_ret)
    return ret
        
case_num=int(read())
for _ in range(case_num):
    fence_num=int(read())
    height_list=list(map(int,read().strip().split()))
    print(Dac(0,fence_num-1))