# 백트래킹이 DFS와 다른점은 가지치기를 한다는 것이다.

# DFS 는 재귀함수로 반복된다.

import sys

input = sys.stdin.readline



n,m  = map(int, input().split())



stacks = []
visited = [False]*(n+1)




def dfs():
    if len(stacks) == m:
        print(' '.join(map(str,stacks)))
        return
    
    for i in range(1,n+1):
 
        if visited[i]:
            continue
        visited[i] = True
        stacks.append(i)
        dfs()
        stacks.pop()
        visited[i] = False
    
dfs()