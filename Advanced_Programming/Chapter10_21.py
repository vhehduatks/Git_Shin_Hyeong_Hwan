test_case=[1,2,3,4,5,6,7,8,9,10,12,14,16]

def reverse_generator1(list_l):
    temp=[]
    for i in list_l[::-1]:
        yield i
    
for i in reverse_generator1(test_case):
    print(i,end=" ")

#better way
reverse_generator2=lambda x:reversed(x)


#람다식 구현시에 filter(조건,iter객체)는 참인 조건(즉 조건문이 필요)을 묶어서 리턴함-> list로 형변환 필요
# lambda x: x~~은 x를 매개변수로 받아서 return x~~이란 뜻   
last_odd=max(list(filter(lambda x:x%2!=0,list(reverse_generator2(test_case)))))

#better way
#람다는 매게변수를 가진 함수임
last_odd2=lambda x: max([i for i in reversed(x) if i%2!=0])
print("\n",last_odd)
print(last_odd2(test_case))