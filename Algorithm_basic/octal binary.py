

# # 자리수별로 끊어주자
# eight = int(input())

# a = list(map(int,str(eight)))



# for i in range(len(a)):
#   print(a[i])


# # 여기서 내장함수가 존재할 것이라고 생각


# 풀이

a = int(input(),8)

result = bin(a)[2:]

print(result)






