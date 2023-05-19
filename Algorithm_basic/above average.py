# 나의 코드


# a = input()

# b = len(a)

# for i in range(b):
#   c= input().split()
#   d = len(c)
#   avg =0
#   for j in range(d):
#     if j == 0:
#       avg = avg
#     else:
#       avg += int(c[j])
#   avg /= (d-1)
#   result = 0
#   for ss in range(d):
#     if ss ==0:
#       result = result
#     else:
#       if int(c[ss]) > avg:
#         result += 1
#   result /= (d-1)
#   print(result)

# 다른사람 코드



n = int(input())

for _ in range(n):
  nums = list(map(int,input().split()))
  avg = sum(nums[1:])/nums[0]
  cnt =0
  for score in nums[1:]:
    if score > avg:
      cnt += 1
  rate =cnt /nums[0] *100
  print(f'{rate:.3f}%')