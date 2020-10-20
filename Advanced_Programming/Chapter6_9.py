class Chapter_func:
    def __init__(self,nums):
        nums=nums.split(' ')
        try:
            self.nums=tuple(map(int,nums))
            print("입력한 튜플 :",self.nums)
        except Exception as e:
            print("Wrong_value :",e)

    def remove_overlap(self):
        self.nums=list(set(self.nums))
        self.nums.sort()
        self.nums=tuple(self.nums)
        print("중복을 제거한 튜플 :",self.nums)
        
        return self.nums

if __name__ == "__main__":
    Nums=input("임의의 수를 입력하세요 :")
    Func=Chapter_func(Nums)
    Func.remove_overlap()