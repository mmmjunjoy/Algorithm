

# N,K값을 받기 위해

a = [*map(int,input().split())]


N = a[0]

K = a[1]


# N,K값의 조건을 세워주어서 , 조건을 만족할시에 코드가 진행되도록

# 아쉬운 부분은 조건을 만족하지 않을 경우 다시 , 기입하는 것을 시작하도록 하는 것

if (2<= N <=100000 and 2<= K <=100000):
  
  count = 0

  while N>1:
    if N%K == 0:
      N = N/K
      count += 1
    elif N%K != 0:
      N = N-1
      count += 1


  
    

print(count)
    

    


      