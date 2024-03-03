

import sys


input = sys.stdin.readline



n = int(input())



# remove를 사용해야 하므로, list가 아닌 dict형태의 set을 사용하자

# list의 시간복잡도 / remove -o(n) 
# set의 시간복잡도 / remove - o(1) 이다.
namelist = set()
for i in range(n):
    name,state = map(str, input().split())

    if name in namelist:
        # if state =="leave":
            namelist.remove(name)

    if name not in namelist :
        if state == "enter":
            namelist.add(name)


# 정렬 사용하기 위해, list로 변환해준다. -set을
namelist = list(namelist)




# 역순정렬을 위해 sort ,reverse사용해주고,

namelist.sort(reverse=True)



# for i in namelist:
#     print(i)


# 시간복잡도 위해 위에것을 아래로 변경
s =""

for i in namelist:
    s += str(i) + '\n'

print(s)
    
