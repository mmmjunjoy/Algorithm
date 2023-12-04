import sys

input = sys.stdin.readline

# n = int(input())


# lists = []

# lists = list(range(1,n+1))

    
# while len(lists) > 1: 
#     lists.pop(0)
#     lists.append(lists.pop(0))

# print(lists[0])


# pop으로 풀면 "시간초과" 가 생긴다
# deque로 풀자



from collections import deque

ns = int(input())

deque = deque([i for i in range(1,ns+1)])

while(len(deque)>1):
    deque.popleft()
    deque.append(deque.popleft())

print(deque[0])