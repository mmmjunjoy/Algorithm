
import sys

input = sys.stdin.readline


T = int(input())



for i in range(T):
    N = int(input())

    namelist = []
    sojulist = []
    for j in range(N):
        name , soju = input().split()
        soju = int(soju)
        namelist.append(name)
        sojulist.append(soju)
    maxsoju = max(sojulist)
    resi = sojulist.index(maxsoju)

    res = namelist[resi]

    print(res)