import sys
read=sys.stdin.readline


def match(wp,sp):
    global cache
    global source
    global wild

    if not(cache[wp][sp]==-1):
        # print("use cache")
        return cache[wp][sp]
    # print(source)
    # print(wp,sp)
    while((sp<len(source) and wp<len(wild))and(source[sp]==wild[wp] or wild[wp]=='?')):
        # print("ptr+")
        sp+=1
        wp+=1
#2,4
    if len(wild)==wp:
        # print("out")
        cache[wp][sp]=int(len(source)==sp)
        return len(source)==sp

    if wild[wp]=='*':
        
        skip=0
        # print("skip",skip)
        # print("sp",sp)
        while(sp+skip)<=len(source):
            if match(wp+1,sp+skip):
                cache[wp][sp]=1
                return True
            skip+=1
    
    cache[wp][sp]=0
    return False

case_num=int(read())

for _ in range(case_num):
    wild=read().strip()
    source_num=int(read())
    source_list=list()
    for _ in range(source_num):
        source_list.append(read().strip())
    source_list=sorted(source_list)
    
    for source in source_list:
        #런타임 에러가 난 이유는 메모리 관리일 때문일 수 있다. 
        #캐시의 범위는 100인데 101에 캐싱하려는 시도가 런타임 에러를 일으켰음

        cache=[[-1]*101 for _ in range(101)]
        if match(0,0):
            print(source)
        # print(cache)    
        # for c_row in range(len(cache)):
        #     for c_col in range(len(cache[0])):
        #         if not(cache[c_row][c_col]==-1):
        #             cache[c_row][c_col]=-1
  
        
