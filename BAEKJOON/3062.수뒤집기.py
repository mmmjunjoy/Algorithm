# 수 124를 뒤집으면 421이 되고 이 두 수를 합하면 545가 된다. 124와 같이 원래 수와 뒤집은 수를 합한 수가 좌우 대칭이 되는지 테스트 하는 프로그램을 작성하시오.


# 입력
# 4
# 13
# 58
# 120
# 5056

a = int(input())
s=[]
x=[]
new = ''
for i in range(a):
  b = input()
  for i in range(len(b)):
    s.append(b[i])
  print("리스트에 담기" ,s)
  for i in range(len(b)):
    x.append(s.pop())
  print("거꾸로 리스트" ,x)
