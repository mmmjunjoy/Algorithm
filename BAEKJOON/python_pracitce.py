

# match 쓰이는게 맞는가 , 왜 오류 .


# def http_error(status):
#   match status:
#     case 400:
#       return "bad request"
#     case 404:
#       return "not found"
    
  
# http_error(400)

# for n in range(1, 11):
#     match n % 2:
#         case 0:
#             print(f"{n} is even.")
#         case 1:
#             print(f"{n} is odd.")


#----------------------------------------------

# list - zip 쓰임

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# format - 문자열이 들어갈 자리를 지정해줄떄 

formatprac = '오늘은 {}년 {}월 {}일 입니다'.format(2022,3,17)

print("format실험", formatprac)