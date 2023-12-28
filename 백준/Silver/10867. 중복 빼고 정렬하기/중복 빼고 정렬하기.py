# N개의 정수가 주어진다. 이때, N개의 정수를 오름차순으로 정렬하는 프로그램을 작성하시오. 같은 정수는 한 번만 출력한다.


# 첫째 줄에 수의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째에는 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다.


# 첫째 줄에 수를 오름차순으로 정렬한 결과를 출력한다. 이때, 같은 수는 한 번만 출력한다.




import sys

input = sys.stdin.readline


N = int(input())


firstlist = list(map(int ,input().split()))

#1. 중복제거

# set자료구조의 특징은 중복이 없는 것이다. 그래서 이를 이용
twolist = list(set(firstlist))


#2. 오름차순으로 정렬


# reverse = True : 내림차순으로 하고싶을때

lastlist = sorted(twolist )


for i in lastlist:
  print(i,end=' ')


