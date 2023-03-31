#큐를 쓰기 위해 import해줘야한다.
from collections import deque

queue = deque()

queue.append(5)
queue.append(3)
queue.append(4)

#이것이 뺴는 것
queue.popleft()
queue.append(22)
queue.popleft()

print(queue)

#반대로 뽑기 위해 해주는 코드
queue.reverse()

print(queue)
