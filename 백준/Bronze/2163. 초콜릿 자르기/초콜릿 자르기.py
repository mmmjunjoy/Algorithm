import sys
# import math


input = sys.stdin.readline

n,m = map(int, input().split())


resultone = n-1

resulttwo = (m-1) * n

print(resultone + resulttwo)

