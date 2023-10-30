#python - array

#list - str ,int, float ,bool 등 다른 종류의 데이터 저장 가능

#1차원 배열

list1 = [1, 2, 3, 4, 10]
print('1차원', list1)

#2차원 배열

list2 = [[1, 2], [3, 4, 5], [2, 5, 7]]

print('2차원', list2)

#빈 리스트 구현

list3 = []
list4 = list()

print(list4)

#요소 추가

list3.append("junjoy")
print("추가된 리스트3", list3)

#요소 삭제 2가지 방법 - pop,remove
#pop은 인덱스 접근
#remove는 해당 값이 존재하는지 접근

list1.pop(2)
print('pop에의해 삭제된리스트1', list1)
list1.remove(10)
print('remove에의해 삭제된리스트3', list1)
