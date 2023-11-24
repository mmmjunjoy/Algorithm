import collections
import sys
input = sys.stdin.readline

a = input().strip()
a = a.upper()


answer=[]

count = collections.Counter(a)
max_value = max(list(count.values()))

for key in list(count.keys()):
  if count[key] == max_value:
    answer.append(key)

# print("counter", count)

# print("답", answer)

if len(answer) == 1 :
  print(answer[0])

else:
  print("?")