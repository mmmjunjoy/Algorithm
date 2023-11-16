def standard_arg(arg):
  print("평범" , arg)

def pos_only_arg(arg, /):
  print("위치설정", arg)

def kwd_only_arg(*, arg):
  print("정의설정",arg)

def combined_ex(pos_only,/,standard,*,kwd_only):
  print("위치 :",pos_only,"평범 :",standard, "정의 :", kwd_only)


print("------------start-------------")


# standard일떄는 , 아래 두 경우 둘다 된다.

standard_arg(arg=10)
standard_arg(7)

print("------------------------")

# position 일때는 '/' : arg=10 이런식으로 설정해주면 오류가난다.

pos_only_arg(5)

print("------------------------")

#keyword 일떄 '*' : 단순하게 3 이렇게 하면 오류가난다.

kwd_only_arg(arg=3)

print("-----------end-------------")