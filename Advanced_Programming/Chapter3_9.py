class INTEGER_DIV:
    def __init__(self, int_val):
        self.Integer = int_val
        self.temp = 0

    # private 선언법 _두개 protect는 _하나
    def __div_2(self, int_val):
        if int_val % 2 == 0:
            return "2로 나누어집니다."
        self.temp += 1
        return "2로 나누어지지 않습니다."

    def __div_3(self, int_val):
        if int_val % 3 == 0:
            return "3으로 나누어집니다."
        self.temp += 1
        return "3으로 나누어지지 않습니다."

    def print_func(self):
        print(self.Integer, "는 ", self.__div_2(self.Integer))
        print(self.Integer, "는 ", self.__div_3(self.Integer))
        if self.temp == 0:
            print(self.Integer, "는 2와 3모두로 나누어집니다.")
        elif self.temp == 1:
            print(self.Integer, "는 2와 3중 하나로만 나누어집니다")
        elif self.temp == 2:
            print(self.Integer, "는 2와 3 둘다 나눌수 없습니다.")
        self.temp = 0


if __name__ == "__main__":
    # 형변환 확인할것
    try:
        main_func = INTEGER_DIV(int(input("정수를 입력하세요 :")))
        main_func.print_func()
    except ValueError as e:
        print(e, "Wrong Value")

    
