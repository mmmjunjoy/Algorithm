h = int(input())

count = 0

# 3중 for문을 이용해서 풀어보자

# 정수형을 문자열로 바꾸고 해당되는 문자가 있는지 확인하는 방식으로 해보자

for hs in range(h + 1):
  for ms in range(60):
    for ss in range(60):
      if '3' in str(hs) + str(ms) + str(ss):
        count += 1

print(count)
