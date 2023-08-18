N = int(input())
x = str(N)
a = len(str(N))


if "0" not in x:
  print(-1)

else:
  num_sum = 0
  for i in range(a):
    num_sum += int(x[i])
  if num_sum %3 != 0:
    print(-1)
  else:
    sorted_num = sorted(x,reverse=True)

    answer = "".join(sorted_num)
    print(answer)
  
  