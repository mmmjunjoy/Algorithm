# 나의 코드 

# 11과 같은 입력값을 -1로 처리해버리는 문제점

# sultang = int(input())

# result = 0

# while sultang != 0:
#   if sultang % 5 == 0:
#     sultang -= 5
#     result += 1
#     if sultang == 0:
#       break
#   else:
#     break


# while sultang != 0:
#   if sultang % 3 == 0:
#     sultang -= 3
#     result += 1
#     if sultang == 0:
#       break
#   else:
#     break

# if sultang != 0:
#   result = -1

# else:
#   result = result

# print(result)


# 풀이

sugar = int(input())
bag =0

while sugar >= 0:
  if sugar %5 ==0:
    bag += (sugar//5)
    print(bag)
    break
  sugar -=3
  bag += 1

else:
  print(-1)
    