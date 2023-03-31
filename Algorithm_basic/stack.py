stack = []

stack.append(2)
stack.append(2)
stack.append(2)
stack.append(2)

stack.pop()

stack.append(11)
stack.append(4)

stack.pop()

#최하단 원소부터 추출
print(stack)

#최상단 원소부터 추출
print(stack[::-1])
