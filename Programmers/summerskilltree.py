"""
선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.
예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 
썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 
먼저 스파크를 배워야 합니다.
위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 
따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 
썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.
선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 
매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.
"""

skill="CBD"
skill_trees=["BACDE", "CBADF", "AECB", "BDA"]


def solution(skill, skill_trees):
    temp=list(skill)
    count=0
    temp2=list()
    

    for i in skill_trees:
        index=list()
        for j in temp:
            index.append(i.find(j))
        temp2.append(index)

    for i in temp2:
        for j in range(1,len(i)):
            if i[j-1]==-1 and i[j-1]<i[j]:
                print(i,"1:",i[j-1],",",i[j])
                break
            if i[j-1]>i[j] and i[j]!=-1:
                print(i,"2:",i[j-1],",",i[j])
                break
                
            if j==len(i)-1:
                count+=1

    return count

print(solution(skill,skill_trees))