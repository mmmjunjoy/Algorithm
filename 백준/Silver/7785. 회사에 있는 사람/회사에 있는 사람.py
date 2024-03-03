

import sys


input = sys.stdin.readline



n = int(input())


namelist = set()
for i in range(n):
    name,state = map(str, input().split())

    if name in namelist:
        # if state =="leave":
            namelist.remove(name)

    if name not in namelist :
        if state == "enter":
            namelist.add(name)

# print(namelist)
namelist = list(namelist)

# print(namelist)
    
namelist.sort(reverse=True)

# print(namelist)

# for i in namelist:
#     print(i)


s =""

for i in namelist:
    s += str(i) + '\n'

print(s)
    
