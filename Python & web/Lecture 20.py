# 예제 ) numguess 오류 처리
import random


def input_answer():

    try:
        your_answer = int(input("1~50 사이의 정수를 입력해주세요\n"))
        return your_answer
    except ValueError:
        print("올바른 값을 넣으시오")
        return(input_answer())


def numguess(coins=1, answer=random.randint(1, 50)):
    score = 1
    while 1:
        your_answer = input_answer()
        if score > coins:
            print(f"기회는 {coins}번 뿐 후후후! 다시 도전해 보라구")
            break
        if 0 <= answer < your_answer <= 50:
            score += 1
            print("Down")
        elif 0 <= your_answer < answer <= 50:
            print("Up")
            score += 1
        elif answer == your_answer:
            print(f"정답! 점수 : {score}")
            break
        else:
            print("1부터 50 사이의 값을 넣으세요")


numguess(5)

# # 예제 ) 피보나치 수열 반복문
# def fib(n):
#     a = [0, 1]
#     i = 1
#     while i < n:
#         a = [a[1], a[0]+a[1]]
#         i+=1
#     return a[1]

# print(fib(6))

# #예제 ) 피보나치 수열

# def fib(n):
#     if n<=2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# a=fib(5)
# print(a)
