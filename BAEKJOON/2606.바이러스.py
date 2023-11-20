# import sys
# input = sys.stdin.readline

# a = int(input())

# b = int(input())


# final = []

# for _ in range(b):
#     fir =[]
#     n,m = map(int,input().split())
#     fir.append(n)
#     fir.append(m)
#     print("Fir",fir)
#     final.append(fir)

# print("Final", final)

n=int(input()) # 컴퓨터 개수
v=int(input()) # 연결선 개수
graph = [[] for _ in range(n+1)] # 그래프 초기화    


visited=[0]*(n+1) # 방문한 컴퓨터인지 표시
for i in range(v): # 그래프 생성
    a,b=map(int,input().split())
    graph[a].append(b) # a에 b 연결
    graph[b].append(a) # b에 a 연결 -> 양방향


# graph에서는 -> 인덱스가 1번,2번 컴퓨터 역할을 해주며, 리스트 안에 들어있는 것들이 해당 컴퓨터와 연결되어 있는 것을 말해준다.

print("graph final", graph)
def dfs(graph,v,visited):
    visited[v]=1
    for i in graph[v]:
        if visited[i]==0:
            dfs(graph,i,visited)
dfs(graph,1,visited)

print("visited", visited)
print(visited.count(1)-1)
