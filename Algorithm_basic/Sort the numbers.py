#나의 코드

# a = int(input())

# b= len(a)

# for _ in range(b):
#   nums = list(map(int, input().split()))
#   for _ in range(nums):





# import sys 사용 방법


# import sys

# line = sys.stdin.readline()

# line = line.rstrip('\n')

# print(line)



# 풀이

# 이번 과정에서 sort()  , sys 사용법을 알게되었다.

import sys

n = int(input())
num =[]
for _ in range(n):
  num.append(int(sys.stdin.readline()))

num.sort()

for i in num:
  print(i)

