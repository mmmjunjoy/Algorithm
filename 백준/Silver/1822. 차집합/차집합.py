import sys
input = sys.stdin.readline

a = map(int,input().split())



alist = set(map(int,input().split()))
blist= set(map(int,input().split()))

res = []

for n in alist:
    if n not in blist:
        res.append(n)

res.sort()

print(len(res))

if len(res) != 0:
    print(*(res))