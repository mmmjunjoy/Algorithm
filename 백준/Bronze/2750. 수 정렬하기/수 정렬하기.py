
import sys

input = sys.stdin.readline


N = int(input())


middle = []
for i in range(N):
  middle.append(int(input()))




middle.sort()



for i in middle:
  print(i , sep='/n')