
#팩토리얼을 구현해보자


#반복적으로 구현


def facto(n):
  result = 1

  for i in range(1,n+1):
    result *= i

  return result



print("반복적으로 구현", facto(5)) 
  
  


#재귀함수로 구현

def factoo(n):


  if n <= 1:
    return 1

  return n * factoo(n-1)


print("재귀적으로 구현", factoo(6))
  