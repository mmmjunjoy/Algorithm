sub = int(input())
total_num = sc = 0
grade_arr = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D+', 'D0', 'D-', 'F']
score_arr = [4.3, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0.7, 0]


for i in range(sub):
    s, num, gr = input().split(" ")

    total_num += int(num)
    # print("과목성적- 영어" ,gr)
    # print("과목성적 - 인덱스 " ,grade_arr.index(gr))
    # print("과목성적 - 숫자" ,score_arr[grade_arr.index(gr)])
    sc += (score_arr[grade_arr.index(gr)] * int(num))

print("%.2f" % round(sc/total_num + 10**-10, 2))