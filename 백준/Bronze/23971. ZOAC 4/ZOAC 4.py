
import sys
import math

input = sys.stdin.readline


w,h,n,m = map(int,input().split())



width  = math.ceil(w/(n+1))

height = math.ceil(h/(m+1))


print(width * height)