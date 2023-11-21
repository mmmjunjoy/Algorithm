
import sys
input = sys.stdin.readline

number = int(input())


listss = []
finalss = []


#pop을 () 이렇게만 쓰지말고 , pop(0) 이런식으로 인덱스를
#활용해서 사용해주기

for i in range(number):
    listss.append(i+1)

while(len(listss) != 0):
    finalss.append(listss.pop(0))

    if len(listss) != 0:
        listss.append(listss.pop(0))



for j in finalss:
    print(j , end=" " )
