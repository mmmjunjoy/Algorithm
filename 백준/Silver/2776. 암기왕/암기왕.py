import sys
input = sys.stdin.readline

a = int(input())



#type(pracl) -> type이 뭔지 알 수 있다.

for _ in range(a):
    prac = int(input())
    pracl = set(map(int,input().split()))


    test = int(input())
    testl = list(map(int,input().split()))
    for i in range(test):
        if testl[i] in pracl:
            print("1")
        else:
            print("0")
