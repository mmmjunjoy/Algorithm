import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S_hear = set()
S_see = set()

for _ in range(N):
    name = input().strip()
    S_hear.add(name)

for _ in range(M):
    name = input().strip()
    S_see.add(name)


# 리스트당 중복 있는 것만 정렬한다.
result = sorted(list(S_hear & S_see))


# *result -> 리스트에 있는 값을 풀어써준다.
print(len(result), *result, sep="\n")