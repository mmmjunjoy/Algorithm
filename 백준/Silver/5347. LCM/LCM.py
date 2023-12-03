import sys

input = sys.stdin.readline

n = int(input())

for i in range(n) :

    # 한번에 값 두개 받는 것은 -> split() 사용
    a,b = input().split()
    a = int(a)
    b = int(b)

    # 이제 부터 a,b 각각의 약수를 찾자
    alist = []
    for j in range(1,a+1):
        if a%j == 0:
            alist.append(j)

    # print("alist", alist)

    blist = []
    for h in range(1,b+1):
        if b%h == 0:
            blist.append(h)

    # print("blist", blist)

    # 이제 두개의 리스트에 공통으로 있는 값들 추출

    reslist =[]
    for s in range(len(alist)):
        if alist[s] in blist:
            reslist.append(alist[s])

    
    # print("reslist" ,reslist)

    # 추출된 값들중 가장 큰 값 찾기

    resn  = reslist[-1]

    # print("resn" ,resn)

    # resn 값으로 a,b를 나누어 an ,bn 추출 

    an = a // resn
    bn = b // resn

    # 최종

    res = resn * an * bn

    print(res)