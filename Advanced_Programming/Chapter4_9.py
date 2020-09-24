#내장함수 사용법 https://wikidocs.net/32#map
def mean_of_n(nums):
    nums=nums.split(' ')
    try:
        nums=list(map(int,nums))
    except Exception as e:
        print("Wrong_value :",e)

    return sum(nums)/len(nums)

def max_of_n(nums):
    nums=nums.split(' ')
    try:
        nums=list(map(int,nums))
    except Exception as e:
        print("Wrong_value :",e)

    return max(nums)

def min_of_n(nums):
    nums=nums.split(' ')
    try:
        nums=list(map(int,nums))
    except Exception as e:
        print("Wrong_value :",e)

    return min(nums)

if __name__ == "__main__":
    Nums=input("정수를 여러 개 입력하시오")
    print("평균값 :",mean_of_n(Nums))
    print("최댓값 :",max_of_n(Nums))
    print("최솟값 :",min_of_n(Nums))