#https://wikidocs.net/14
def sort3(num1,num2,num3):
    l=list()
    l.append(num1)
    l.append(num2)
    l.append(num3)
    l.sort()
    return l

if __name__ == "__main__":
    print("세 수를 입력하세요 :")
    Num1=int(input())
    Num2=int(input())
    Num3=int(input())

    a=sort3(Num1,Num2,Num3)
    print("정렬된 리스트 : {} {} {}".format(a[0],a[1],a[2]))