from collections import deque

N,M,V = map(int,input().split())


# 체크하기 위한 , N값에 해당하는 빈 그래프 생성(FALSE)
graph = [[False] * (N+1) for _ in range(N +1)]


# M -간선으로 등록된 곳은 TRUE로 체크
for _ in range(M):
    a,b = map (int,input().split())
    graph[a][b] = True
    graph[b][a] = True



# DFS와 BFS 체크를 위한 FALSE리스트 생성
visitedfs = [False] * (N+1)
visitebfs = [False]* (N+1)

# BFS 

def bfs(V):
    q = deque([V])
    visitebfs[V] = True
    #q가 queue이기 떄문에, 이게 빈 리스트가 되지않을때까지
    #돌겠다는 뜻
    while q:
        V = q.popleft()
        print(V, end = " ")
        for i in range(1,N+1):
            if not visitebfs[i] and graph[V][i]:
                q.append(i)
                visitebfs[i] = True


# DFS

def dfs(V):
    visitedfs[V] = True
    print(V, end = " ")
    for i in range(1,N+1):
        if not visitedfs[i] and graph[V][i]:
            dfs(i)



dfs(V)
print()
bfs(V)