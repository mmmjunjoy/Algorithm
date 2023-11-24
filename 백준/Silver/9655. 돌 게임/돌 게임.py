
import sys 

input = sys.stdin.readline

a = int(input())

# 수가 짝수일떄는 상근이가 이기고, 홀수있때는 찬영이가 이긴다.

if a%2 == 1 :
  print("SK")

else:
  print("CY")
