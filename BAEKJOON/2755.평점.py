# 최백준이 이번 학기에 들은 과목과 학점 그리고 성적이 주어졌을 때, 평균 평점을 계산하는 프로그램을 작성하시오.

# 성적은 A+~F까지 총 13개가 있다.

# A+: 4.3, A0: 4.0, A-: 3.7

# B+: 3.3, B0: 3.0, B-: 2.7

# C+: 2.3, C0: 2.0, C-: 1.7

# D+: 1.3, D0: 1.0, D-: 0.7

# F: 0.0

# 평균 평점은 각 과목의 학점*성적을 모두 더한 뒤에, 총 학점으로 나누면 된다.





#-------------------------start-----------------------
# 이렇게 하면 답은 나오나 , 런타임 오류가 뜬다


#0.5반올림해주기 위해서
# import decimal


# 필요한 변수 지정

# 듣는 과목 몇학점인지
gradeplus = []

# 학점
point = []    

# 최종합
bigpoint = 0  

# 최종듣는수업시간합
pluspoint = 0

# 첫 입력값
a = int(input())


for i in range(a):
  b = input()
  lens = len(b)
  gradeplus.append(b[lens-2])
  gradeplus.append(b[lens-1])
  # print('과목당 점수' , gradeplus)
  point.append(b[lens-4])
  # print("과목당 수업시수", point)

 # 실수형 변환학점
  if gradeplus[0] == "A":
    if gradeplus[1] == "+":
      pointf = 4.3
    elif gradeplus[1] == "-":
      pointf = 3.7
    else :
      pointf = 4.0
  elif gradeplus[0] == "B":
    if gradeplus[1] == "+":
      pointf = 3.3
    elif gradeplus[1] == "-":
      pointf = 2.7
    else :
      pointf = 3.0
  elif gradeplus[0] == "C":
    if gradeplus[1] == "+":
      pointf = 2.3
    elif gradeplus[1] == "-":
      pointf = 1.7
    else :
      pointf = 2.0
  elif gradeplus[0] == "D":
    if gradeplus[1] == "+":
      pointf = 1.3
    elif gradeplus[1] == "-":
      pointf = 0.7
    else :
      pointf = 1.0
  else:
    pointf = 0.0

  xy = float(point[0])*float(pointf)
  # print("한과목당 합", xy)
  bigpoint += xy
  # print("나누기전 점수", bigpoint)
  pluspoint += float(point[0])
  # print("최종 듣는 수업 시간 합", pluspoint)
  gradeplus =[]
  point = []

lastpoint = bigpoint/pluspoint


# round 사용하여 , 소수점 둘쨰자리까지 출력

# print("반올림 전" , lastpoint)
# print("가공" , round(lastpoint + 10**-10,2))
print(round(lastpoint + 10**-10,2))


# 입력값

# 7
# General_Physics_1 3 A+
# Introduction_to_Computer_Science_and_Eng 3 B0
# Reading_And_Writing 2 C0
# English_1 3 C+
# Analytic_Geometry_and_Calculus_1 3 B+
# Fortran_Programming 3 B+
# C_Language_Programming 3 A+


