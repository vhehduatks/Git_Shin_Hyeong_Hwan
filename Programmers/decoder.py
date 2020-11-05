import string
#실패
def Shift(str_value,shift_val): 
    
    return_str=str_value[shift_val:]+str_value[:shift_val]

    return return_str


text="b"
key="a"
def solution(encrypted_text, key, rotation):
    temp=Shift(encrypted_text,rotation)
    Low=string.ascii_lowercase
    answer = ''
    print(temp)
    for i in range(len(encrypted_text)):
        if temp[i]==" "and key[i]==" ":
            answer+=temp[i]
            continue
        p=Low.index(temp[i])
        q=Low.index(key[i])+1
        answer+=Low[p-q]
     
    return answer

print(solution(text,key,0))    