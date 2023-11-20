
# 수를 문자열 형식으로 붙여준 뒤,
# find로 찾고 싶은 수를 찾아준다.

a = ''
for i in range(1,100001):
  a += str(i)

print(a.find(input())+1)