# m = int(input())
# n = int(input())
# k = int(input())

# l = list(map(int,input().split()))

# n = l[0]   #여학생수
# m = l[1]   #남학생수
# k = l[2]   #인턴수

#해설
n, m, k = map(int, input().split())
result = 0
while n >= 2 and m >= 1 and n + m >= k + 3:
  n -= 2
  m -= 1
  result += 1
print(result)
