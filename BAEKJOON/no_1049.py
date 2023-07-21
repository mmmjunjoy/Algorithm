cut,brand = map(int,input().split())


six = []
one = []
cost = 0
line = cut//6
percent = cut%6

for i in range(brand):
  sixss,ones= map(int,input().split()) 
  six.append(sixss)
  one.append(ones)


if min(six) <= min(one)*6:
  cost = min(six)*line + min(one)*percent
  if min(six) < min(one)*percent:
    cost = min(six)*(line+1)
else:
  cost = min(one)*cut


print(cost)