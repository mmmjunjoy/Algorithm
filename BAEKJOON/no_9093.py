# 여기서 sys
# sys.stdin.readline() -> 한줄입력받기
# rstrip() 사용하여 제거하는 기능
# split() -> 문자열을 끊어서 리스트형태로 저장

# word[::-1] -> 거꾸로 뒤집음
# end =" " -> 한칸 뛰어준다


import sys

n = int(input())

for i in range(n):
  words = sys.stdin.readline().split()
  
  for word in words:
    print(word[::-1],end=" ")
  print()
    