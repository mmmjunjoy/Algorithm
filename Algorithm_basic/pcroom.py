n = int(input())

s = list(map(int,input().split()))

cnt = 0  # 중복 학생 수
b= []  #피시방 자리
for i in range(n):
  if s[i] in b:
    cnt += 1
  else:
    b.append(s[i])

print(cnt)