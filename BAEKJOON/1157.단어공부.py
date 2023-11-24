# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.



#collections 가 counter의 역할을 가지고 있다.
import collections


import sys
input = sys.stdin.readline

a = input().strip()

#upper는 소문자를 대문자로 바꿔준다
a = a.upper()


answer=[]

count = collections.Counter(a)
max_value = max(list(count.values()))


for key in list(count):
  if count[key] == max_value:
    answer.append(key)

# print("counter", count)

# print("답", answer)

if len(answer) == 1 :
  print(answer[0])

else:
  print("?")

