# 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.

# 3 : 3 (한 가지)
# 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
# 53 : 5+7+11+13+17 = 53 (두 가지)
# 하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다. 또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.

# 자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.


#1. step1. 어떠한 수가 들어왔을때 그것보다 이하인 수에서 소수를 찾아 리스트로 반환
#2. step2. 리스트에 있는 수들을 합할떄 , 본래의 input값이 되는 경우의 수를 반환

inp = int(input())
arrays = []


# step1.

a =[False,False] + [True] * (inp-1)
print("a",a)


# step2.

count = 0
sum = 0
i,j = 0,0


# while안에 if문 두가지 사용
while(True):
    if sum == inp:
        count +=1
    if sum > inp:
        sum -= arrays[i]
        i+=1
    elif j == len(arrays):
        break
    else:
        sum += arrays[j]
        j+=1
print(count)


# for i in range(len(arrays)):
#     one = int(arrays[i])
#     inp = inp - one
#     print("one", one)
#     print("new inp" ,inp)
#

# print("소수의 리스트", arrays)



