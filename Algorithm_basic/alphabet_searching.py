# 원하는 값으로만 배열 생성하기

temp = [-1 for x in range(26)]

# for i in range(26):
#   temp.append(-1)

alphabet = input()

i = 0

for c in alphabet:
  # print(c, ord(c), ord(c) - 97, i)
  s = ord(c) - 97
  if temp[s] == -1:
    temp[s] = i

  i += 1

  # 그러면 , temp에서 ord(c) 자리에 i값이 들어가도록 코드를 짜서 temp를 변형시켜준후 , temp를 뽑아보면 될것이다.

# print("for문으로 출력")
for n in temp:
  print(n, end=" ")
