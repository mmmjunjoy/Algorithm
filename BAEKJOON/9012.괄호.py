# 백준 , 9012 번 - 스택 ,자료구조 , 문자열

# 1. 입력을 받을 T
# 2. 테스트 데이터의 첫쨰 줄에는 괄호 문자열이 한줄에 주어진다.
# 하나의 괄호 문자열의 길이는 2이상 50이하다


# 1. 입력 받기 - T로

T = int(input())
print(T)

# 2. 입력된 T값만큼 값받기

# 특수문자 (,) 을 담을 공간
stack = []

# ( , ) 를 셀 카운터
# x1 = 0
# x2 = 0
#

# 수정 코드
# 유의 해야 할점  -> append와 pop을 한번에 하는 것이 아닌,
# 해당 문자열 조건에 맞게 append와 pop을 처리해주면서
# 마지막에 결과값을 확인한다.
T = int(input())


for i in range(0,T):
    stack =[]
    s = input()

    for j in s:

        if j == '(':
            stack.append(j)
        elif j ==')':
            if stack:
                stack.pop()
            else :
                print('NO')
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")







# 나의 코드 - ( ,) 의 갯수가 일치할 경우 yes처리

# for i in range(0,T):
#     s = str(input())
#     print(s)
#     lens  = len(s)
#     for j in range(0,lens):
#         stack.append(s[j])
#         print(stack)
#         x = stack.pop()
#         print("뺸 것",x)
#         if x == '(':
#             x1 += 1
#         if x == ')':
#             x2 += 1
#
#     print('x1' ,x1)
#     print('x2', x2)
#
#
#     if x1 == x2:
#
#         print("YES")
#     else :
#         print("NO")




