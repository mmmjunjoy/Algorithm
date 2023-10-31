# stack

# 가장 나중에 들어온 자료가 가장 먼저 처리되는
# LIFO (Last In First Out) 방식
# 즉 , 병에 구멍이 하나밖에 없다고 생각하면 편하다.

# 빈 리스트 생성

stack = []

# 스택에 원소 추가 - append

stack = [1,2,3]
stack.append(4)

print("스택 현 상태", stack)

# 스택에서 원소 제거 - pop

top = stack.pop()

print("나온 값" , top)


# 리스트의 마지막 값 - 인덱스 -1 사용

