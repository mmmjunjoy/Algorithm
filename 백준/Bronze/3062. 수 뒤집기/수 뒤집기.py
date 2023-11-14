s = int(input())

for i in range(s):
    b = input()
    result = str(int(b) + int(b[::-1]))
    if result == result[::-1]:
        print("YES")
    else:
        print("NO")