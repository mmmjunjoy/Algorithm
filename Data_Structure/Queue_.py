#큐-Queue

# 먼저 입력된 데이터가 먼저 엑세스 되는 ,
# FIFO 방식의 선입선출

# HEAD-TAIL / FRONT-BACK 에서 PUSH 또는 POP수행가능

# 시간 순서가 중요할떄 사용

# Enqueue :  Queue에 데이터를 넣는 기능
# Dequeue : Queue에서 데이터를 꺼내는 기능

# 즉 , 큐에서 데이터를 push & pop하는 것을 enqueue,dequeue라고 한다.


qlist = [ ]
def enqueue(qlist,data):
    qlist.append(data)
def dequeue(qlist):
    data=qlist[0]
    del qlist[0]
    return data

#데이터 삽입
enqueue(qlist,10)
enqueue(qlist,15)
enqueue(qlist,5)
enqueue(qlist,20)

#데이터 아웃 , # 가장먼저 들어간 것을 아웃되게 하는 dequeue
dequeue(qlist)

print("변한 큐",qlist)


# python 제공 큐 라이브러리 3가지

# 1 .Queue()
# 2. LifoQueue()
# 3. PriorityQueue()


### 1. 일반적인 queue
import queue
data_q = queue.Queue()


#put 이 enqueue역할을 한다
data_q.put(1)
data_q.put("junjoy")

# 큐 사이즈 체크
print("큐사이즈 체크" ,data_q.qsize())
# data 가져오기
print("데이터 가져오기" ,data_q.get())

# get 한 후 queue사이즈
print("get한 후큐사이즈 체크" ,data_q.qsize())


### 2. LifoQueue()
# 이름에서 알 수 있듯이,
# 후입선출이다.

data_lq = queue.LifoQueue()
data_lq.put("1")
data_lq.put("himan")

# 큐 사이즈 체크
print("lf 큐 사이즈 체크", data_lq.qsize())
# 큐 하나 아웃
print("lf 큐 아웃" , data_lq.get())


### 3. PriorityQueue()
# 우선순위에 따라 아웃

data_pq = queue.PriorityQueue()

data_pq.put((10.,"cats"))
data_pq.put((1. ,"a dog"))
data_pq.put((7. , "lion"))

# 무엇이 우선순위가 높은지 체크

print("우선순위 높은 것 아웃" , data_pq.get())







