inp = int(input())
arrays = []


# step1.  -> 에랏토스테네스의 체 (소수를 구하는 방법)
# 1.//  0,1 을 제외하고,  2부터 append시킨 후, append 시킨 수의 배수들은
# false로 변환시킨다.


a =[False,False] + [True] * (inp-1)
# print("a",a)

for i in range(2,inp+1):
    if a[i]:
        arrays.append(i)
        for j in range(2*i,inp+1,i):
            a[j] = False


# step2.ㄹ

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
