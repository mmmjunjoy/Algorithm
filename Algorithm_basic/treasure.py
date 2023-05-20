# N = int(input())

# A = list(map(int, input().split()))
# B = list(map(int,input().split()))

# #정렬된 것 반환
# b = sorted(B)

# print(A)
# print(b)


# B의 큰 수 순서대로 인덱스를 반환해주어야 한다.



#  풀이


N = int(input())

A = list(map(int, input().split()))
B = list(map(int,input().split()))

result = 0

for _ in range(N):
  result += min(A) * max(B)
  A.pop(A.index(min(A)))
  B.pop(B.index(max(B)))

print(result)