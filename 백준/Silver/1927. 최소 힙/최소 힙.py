
import heapq


import sys
input = sys.stdin.readline

N = int(input())
lists = []

for _ in range(N):
     a = int(input())
     if a == 0:
      
        if len(lists) == 0:
            print("0")
        else:
            print(heapq.heappop(lists))      
     elif a > 0 :
        heapq.heappush(lists,a)
