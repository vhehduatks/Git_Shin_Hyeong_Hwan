def unit_fraction(frac):
    if frac>1:
        return -1,-1
    elif frac>1/2:
        return 2,1/2

    unit_num=2
    while(1):
        unit_num +=1
        if 1/unit_num-frac<0 :
            break       
    
    temp1=abs(1/unit_num-frac)
    temp2=abs(1/(unit_num-1)-frac)

    if temp1<=temp2 :
        return unit_num,1/unit_num
    else :
        return unit_num-1,1/(unit_num-1)
      
if __name__ == "__main__":
    try:
        result=unit_fraction(float(input("1보다 작고 0보다 큰 소수를 입력하세요 :")))
        print("가장 가까운 단위 분수는 1/{} 이고, 이 값은 {} 이다.".format(result[0],result[1]))
    except Exception as e:
        print("worng_value",e)
      