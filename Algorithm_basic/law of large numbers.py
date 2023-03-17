# a에는 N,M,K를 차례대로 기입해준다.

# N은 자연수의 갯수
# M은 몇 번 더할 수 있는지의 값
# K는 연속으로 더할 수 있는 지정 값

# input을 받을때 배열로 넣을 수 있는 것

# 한 줄 정수 리스트 입력받기
a = [*map(int, input().split())]

# M,K값 설정하기
M = a[1]

K = a[2]

# 정수 N의 값을 배열로 나열하기
b = list(map(int, input().split()))

# b에서 가장 큰 값을 찾기 위해서는 정렬 하는 방법이 필요
b.sort(reverse=True)

print(b)

big = b[0]
twobig = b[1]

print(big)
print(twobig)

result = 0
count = 0


for i in range(M):
 
  count += 1
  result += big
  if count == K:
    
    result += twobig
  count = 0


print(result)


# for i in range(M):
#   if count < K :
#     for i in range(M):
#       count+=1
#       result += big

#       if count == K:
#         result += twobig
#         count = 0
