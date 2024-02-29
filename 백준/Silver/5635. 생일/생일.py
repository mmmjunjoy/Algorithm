



import sys

input = sys.stdin.readline

n = int(input())

lists = []


for i in range(n):
    name=input().split()
    lists.append(name)



year =[]
mon = []
day = []
name = []    
for i in range(len(lists)):
    year.append(int(lists[i][3]))
 


# 가장 나이가 적은 사람 구하기
result1 = []
for i in range(len(lists)):
    if year[i] == max(year):
        result1.append((lists[i]))



result2 = []
if len(result1)>1:
    for j in range(len(result1)):
        mon.append(int(result1[j][2]))
    for m in range(len(result1)):
        if int(result1[m][2]) == max(mon):
            result2.append(result1[m])

else:

    result2 = result1


result3 = []
if len(result2)>1:
    for h in range(len(result2)):
        day.append(int(result2[h][1]))
    for d in range(len(result2)):
        if int(result2[d][1]) == max(day):
            result3.append(result2[d])

else:

    result3 = result2

print(result3[0][0])





year =[]
mon = []
day = []
name = []    
for i in range(len(lists)):
    year.append(int(lists[i][3]))
 


# 가장 나이가 많은 사람 구하기
result1 = []
for i in range(len(lists)):
    if year[i] == min(year):
        result1.append(lists[i])



result2 = []
if len(result1)>1:

    for j in range(len(result1)):
        mon.append(int(result1[j][2]))
    
    for m in range(len(result1)):
        if int(result1[m][2]) == min(mon):
            result2.append(result1[m])
 


else:
    result2 = result1


result3 = []
if len(result2)>1:
    for h in range(len(result2)):
        day.append(int(result2[h][1]))
    for d in range(len(result2)):
        if int(result2[d][1]) == min(day):
            result3.append(result2[d])

else:

    result3 = result2

print(result3[0][0])

