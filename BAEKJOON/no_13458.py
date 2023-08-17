n = int(input())

a = list(map(int, input().split()))
main, sub = map(int, input().split())


answer = n
for i in range(n):
  a[i]-=main
  if a[i]>0:
    if a[i]%sub>0:
      answer += a[i]//sub+1
    else:
      answer += a[i]//sub
print(answer)


# 풀이 1

# total = 0
# for i in range(n):
#   minusmain =int(a[i]) - main
#   total += 1
#   b = minusmain // sub
#   total = total + b
#   c = minusmain % sub
#   if c != 0:
#     total += 1

# print(total)