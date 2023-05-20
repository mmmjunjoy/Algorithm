#나의 풀이 

import math

N = int(input())

s = []
for i in range(N):
  a = list(map(int,input().split()))
  w = a[0]
  h = a[1]
  d = 77
  ppi = math.sqrt(w**2+h**2)/d
  s.append(ppi)



slen=len(s)
for i in range(slen):
  print(s.index(max(s))+1)
  s.pop(s.index(max(s)))



