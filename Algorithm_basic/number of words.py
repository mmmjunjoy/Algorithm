
#나의 생각

a = input ()
b = len(a)
c = " "

result = 1

if b < 1000000:
  for i in range(b):
    if a[i] == c:
      if i == 0 or i == b-1:
        result = result
      else :
        result += 1


print(result)

# 다른사람 생각

word = input().split()

print(len(word))


