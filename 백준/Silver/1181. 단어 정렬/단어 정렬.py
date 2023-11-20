import sys
input = sys.stdin.readline


a = int(input())

wordlist = []

for _ in range(a):
  word = input()
  wordlist.append(word)

setword = set(wordlist)

wordlist = list(setword)

wordlist.sort()
wordlist.sort(key=len)

print(*wordlist , sep="")