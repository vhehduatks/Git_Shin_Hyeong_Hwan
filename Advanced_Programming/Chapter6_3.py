class cafe:

    manu={}
#https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
    def add_item(self,name,price):
        self.manu[name]=price

    def is_item(self,key):
        if key in self.manu:
            return True
        else:
            return False        
#continue 사용 코드건너뛰기
    def choose_item(self):
        while(1):
            item=input("메뉴중 하나를 선택하세요(종료시 x입력) :")
            if self.is_item(item):
                print(item,"은 ",self.manu[item],"원 입니다.")
                continue
            elif item=="x":
                break
            print(item,"은 메뉴에 없습니다.")
        

#공백은 포맷코드 사용 "%10s"%[str] 전체길이가 10인 문자열공간 오른쪽정렬 -10은 왼쪽정렬
    def show_item(self):
        for x in self.manu:
            print("%-20s"%x,"가격 : ",self.manu[x],"원")

if __name__== "__main__":
    Cafe=cafe()
    Cafe.add_item("Americano",3000)
    Cafe.add_item("Ice Americano",3500)
    Cafe.add_item("Cappuccino",4000)
    Cafe.add_item("Cafe Latte",4500)
    Cafe.add_item("Espresso",3600)
    Cafe.show_item()
    Cafe.choose_item()
