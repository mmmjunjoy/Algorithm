import sys


input = sys.stdin.readline

N = int(input())

alist = set(map(int,input().split()))

n = int(input())

blist = list(map(int,input().split()))







for i in range(n):
  if blist[i] in alist:
    print(1)
  else:
    print(0)