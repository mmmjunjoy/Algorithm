import sys
import collections

input = sys.stdin.readline

N = int(input())

books =[]

for i in range(N):
    a = input()
    books.append(a)

countlist = collections.Counter(books)


res = max(countlist.values())

reslist = []

for key , value in countlist.items():
    if value == res:
        reslist.append(key)


reslist = sorted(reslist)

print(reslist[0])