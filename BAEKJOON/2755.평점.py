# 최백준이 이번 학기에 들은 과목과 학점 그리고 성적이 주어졌을 때, 평균 평점을 계산하는 프로그램을 작성하시오.

# 성적은 A+~F까지 총 13개가 있다.

# A+: 4.3, A0: 4.0, A-: 3.7

# B+: 3.3, B0: 3.0, B-: 2.7

# C+: 2.3, C0: 2.0, C-: 1.7

# D+: 1.3, D0: 1.0, D-: 0.7

# F: 0.0

# 평균 평점은 각 과목의 학점*성적을 모두 더한 뒤에, 총 학점으로 나누면 된다.



# 입력값

# 7
# General_Physics_1 3 A+
# Introduction_to_Computer_Science_and_Eng 3 B0
# Reading_And_Writing 2 C0
# English_1 3 C+
# Analytic_Geometry_and_Calculus_1 3 B+
# Fortran_Programming 3 B+
# C_Language_Programming 3 A+

#-------------------------start-----------------------

# 필요한 변수 지정

# 듣는 과목 몇학점인지
gradeplus = []

# 학점
point = []    

# 최종합
bigpoint = 0  

# 첫 입력값
a = int(input())


for i in range(a):
  b = input()
  lens = len(b)
  gradeplus.append(b[lens-2:lens-1])
  print('과목당 점수' , gradeplus)
  point.append(b[lens-4])
  print("과목당 수업시수", point)

  if gradeplus[0] == "A+":
    # 실수형 변환학점
    pointf = 4.3
  elif gradeplus[0] =="A0":
    pointf = 4.0
  elif gradeplus[0] =="A-":
    pointf = 3.7
  elif gradeplus[0] =="B+":
    pointf = 3.3
  elif gradeplus[0] =="B0":
    pointf = 3.0
  elif gradeplus[0] =="B-":
    pointf = 2.7
  elif gradeplus[0] =="C+":
    pointf = 2.3
  elif gradeplus[0] =="C0":
    pointf = 2.0
  elif gradeplus[0] =="C-":
    pointf = 1.7
  elif gradeplus[0] =="D+":
    pointf = 1.3
  elif gradeplus[0] =="D0":
    pointf = 1.0
  elif gradeplus[0] =="D-":
    pointf = 0.7
  else:
    pointf = 0.0

  xy = int(point[0])*pointf
  gradeplus =[]
  point = []
bigpoint += xy

lastpoint = bigpoint/a

print(lastpoint)
