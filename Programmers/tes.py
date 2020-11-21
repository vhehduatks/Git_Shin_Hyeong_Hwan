def insert(J,i,deadline):
    K=J[:]
    for j in range(len(J),0,-1):
        if(deadline[i]>=deadline[K[j-1]]):
            j+=1 #파이썬에서 반복문을 실행하면 1까지 실행되고 0이 실행되지 않는다.
                #(j in range(1,10)을 하면 j=10이 실행되지않음)
                #따라서 리스트의 첫번째j=0 해당되는 j를 추가하기 위해선 
                #나중에 j-1을 하여야 함 하지만 만약 조건을 통과하여
                # j=1에 원소를 추가하려면 조건문을 통과하고 j+1을 하여야 함
                # 결론적으로 조건문에서 차이를 만들어주어야 한다는 뜻 
            break
        print(j)
    print(j)
    K.insert(j-1,i)
    return K

deadline=[0,3,1,1,3,1,3,2]
J=[2,1,4]
K=insert(J,7,deadline)
print(K)