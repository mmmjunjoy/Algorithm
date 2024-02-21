import sys

input = sys.stdin.readline

ns = int(input())



n = 1

while True:
  if n*n + n > 2* ns :
    break
  else:
    n += 1


n -= 1

print(n)