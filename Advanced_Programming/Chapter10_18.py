
def partition(list_l):
    pivotitem=list_l[0]
    pointer=0
    for i in range(1,len(list_l)):
        if list_l[i]<pivotitem:
            pointer+=1  
            list_l[i],list_l[pointer]=list_l[pointer],list_l[i]

    list_l[0],list_l[pointer]=list_l[pointer],list_l[0]
    return list_l


test_list=[int(x) for x in input("임의의 정수를 입력하세요 :").split()]

print("before partition:",test_list)
print("after partition:",partition(test_list))

