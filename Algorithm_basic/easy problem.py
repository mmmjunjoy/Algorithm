# 나의 풀이

s,e = map(int, input().split())

list =[0]
for i in range(e):
  for j in range(i):
    list.append(i)

result = sum(list[s:e+1])

print(result)

      
  
# 다른 사람의 코드
# a,b = map(int,input().split())
 
# arr = [0]
# for i in range(46):
#     for j in range(i):
#         arr.append(i)
 
# print(sum(arr[a:b+1]))