
# 전치상태

# row[i] for row in matrix 

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed =[]

for i in range(4):
  transposed.append([row[i] for row in matrix])



print("전치 전의 원래 상태" , matrix)
print("전치된 상태" , transposed)