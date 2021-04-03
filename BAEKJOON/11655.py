#57
#13
import sys
import string
read=sys.stdin.readline
Ascii_low=string.ascii_lowercase
Ascii_high=string.ascii_uppercase

def Rot13(Str):
    ret=''
    ptr=0
    while ptr<len(Str):
        if Str[ptr] in Ascii_high:
            idx=Ascii_high.index(Str[ptr])
            ret+=Ascii_high[(idx+13)%26]
        elif Str[ptr] in Ascii_low:
            idx=Ascii_low.index(Str[ptr])
            ret+=Ascii_low[(idx+13)%26]
        else:
            ret+=Str[ptr]
        ptr+=1
    
    return ret

print(Rot13(read().strip('\n')))