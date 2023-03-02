# 시간복잡도 측정 모듈
import time

# 랜덤 모듈

from random import randint


#1 배열

array = [3,5,1,2,4]

summary = 0

for x in array:
  summary += x

print(summary)

#2 연산

a = 5

b =10 

print(a+b)


#3 이중 FOR 문

start_time = time.time()

array2 = [1,2,3,4,5]

for i in array2:

  for j in array2:
    temp = i*j
    print(temp)

end_time = time.time()

print("time :", end_time - start_time)



#4 선택정렬과 기본정렬 수행시간 비교

array = []

for _ in range(10000):
  array.append(randint(1,100))

#선택정렬

start_time =time.time()

for i in range(len(array)):
  min_index =i
  for j in range(i+1 ,len(array)):
    if array[min_index] > array[j]:
      min_index = j

  array[i],array[min_index] = array[min_index],array[i]


end_time =time.time()

print()

print("time :", end_time - start_time)


#배열 무작위로 다시 생성

array = []

for _ in range(10000):
  array.append(randint(1,100))

#기본정렬

start_time =time.time()


array.sort()

end_time =time.time()


print("time :", end_time - start_time)