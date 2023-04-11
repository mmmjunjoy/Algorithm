# # 시간 , 분 조건에 맞게 input 하게끔

resulthour = 0
resultmin = 0

while 1:
  a, b = input().split()
  a = int(a)
  b = int(b)
  if a < -1 or a > 24 or b < -1 or b > 60:
    continue
  else:
    break

resultmin = b - 45
if resultmin < 0:
  resulthour = a - 1
  if resulthour < 0:
    resulthour = 24 + (a - 1)
    resultmin = 60 + (b - 45)
  else:
    resulthour = a - 1
    resultmin = 60 + (b - 45)
else:
  resulthour = a
  resultmin = b - 45

print(resulthour, resultmin)
