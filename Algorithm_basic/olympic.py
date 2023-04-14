while 1:

  N, K = input().split()

  n = int(N)
  k = int(K)

  if n > 1000 or n < 1 or k < 1 or k > n:
    continue

  else:
    break

for i in range(n):
  a, g, s, d = input().split()
  a = int(a)
  g = int(g)
  s = int(s)
  d = int(d)
  list[i] = [a, g, s, d]

  print(list[i])
