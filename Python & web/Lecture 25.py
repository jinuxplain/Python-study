# # 예제 3 ) 자의로 에러 발생 시키기


# class MyCustomError(Exception):
#     def __str__(self):
#         return "Custom Error!!"


# try:
#     raise MyCustomError()
# except MyCustomError as e:
#     print(e)


# # 예제 2) 커스텀 에러


# class MyCustomError(Exception):
#     def ___str___(self):
#         return "나만의 특별한 에러 처리!"


# # 예제 1) numguess 오류 처리
# import random
# import traceback


# def input_answer():

#     try:
#         your_answer = int(input("1~50 사이의 정수를 입력해주세요\n"))
#         return your_answer
#     except ValueError as e:
#         traceback.print_exc()
#         print(e)
#         print("올바른 값을 넣으시오")
#         return(input_answer())


# def numguess(coins=1, answer=random.randint(1, 50)):
#     score = 1
#     while 1:
#         your_answer = input_answer()
#         if score > coins:
#             print(f"기회는 {coins}번 뿐 후후후! 다시 도전해 보라구")
#             break
#         if 0 <= answer < your_answer <= 50:
#             score += 1
#             print("Down")
#         elif 0 <= your_answer < answer <= 50:
#             print("Up")
#             score += 1
#         elif answer == your_answer:
#             print(f"정답! 점수 : {score}")
#             break
#         else:
#             print("1부터 50 사이의 값을 넣으세요")
