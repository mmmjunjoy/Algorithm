# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.



# # 처음 , N 과 M의 수

# a = input().split()

# n = a[0]
# m = a[1]

# nstop = int(n)

# nm = int(n)+int(m)


# result = []
# final = []

# # for i in range(int(n)):
# #   result.append(input())
  

# # input(' ')

# # for j in range(int(m)):
# #   result.append(input())

# # 리스트컴프리헨션
# [ result.append(input()) for i in range(nm)]

# # 중복 제거

# for value in result:
#     if value not in final:
#         final.append(value)

# okay = sorted(final)


# count = len(okay)
# print(count)
# for i in range(len(okay)):
#    print(okay[i])



import sys
input = sys.stdin.readline


a = input().split()

n = a[0]
m = a[1]

nstop = int(n)

nm = int(n)+int(m)



# 빈 리스트에 값을 채울떄 , append가 아닌 인덱스를 사용하여 접근방법으로 변경
# result = []
result = [0] * nm

# # 리스트컴프리헨션
for i in range(nm):
    result[i] = input()

final = []
for value in result:
    if value not in final:
        final.append(value)

okay = sorted(final)


count = len(okay)
print(count)
for i in range(len(okay)):
   print(okay[i])


