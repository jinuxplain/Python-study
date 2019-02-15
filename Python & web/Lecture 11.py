# 예제 2 수정) 숫자 맞추기 게임
"""
1. 난수 생성
2. 숫자 입력
3. 난수와 같읕지 확인
4. up and down or 정답
5. 점수 출력
"""
import random
answer = random.randint(1, 50)
count=0
while 1:
    your_answer = eval(input("1~50 사이의 숫자를 입력해주세요\n"))
    if type(your_answer) == int:
        count+=1
        if 0 <= answer < your_answer <= 50:
            print("Down")
        elif 0 <= your_answer < answer <= 50:
            print("Up")
        elif answer == your_answer:
            print(f"정답! 점수는 {count}")
            break
        else:
            pass
    else:
        pass
        

# # 예제 2) 숫자 맞추기 게임
# """
# 1. 난수 생성
# 2. 숫자 입력
# 3. 난수와 같읕지 확인
# 4. up and down or 정답
# 5. 점수 출력
# """
# import random
# answer = random.randint(1, 50)
# while 1:
#     try:
#         your_answer = int(input("1~50 사이의 숫자를 입력해주세요\n"))
#     except ValueError:
#         your_answer = int(input("1~50 사이의 숫자를 입력해주세요\n"))
#     if 0 <= answer < your_answer <= 50:
#         print("Down")
#     elif 0 <= your_answer < answer <= 50:
#         print("Up")
#     elif answer == your_answer:
#         print("정답!")
#         break

# 예제 1) 간단한 예시
# cash = 200000
# credit_card=True
# if cash<100000:
#     print("go to restaurant")
# elif cash<80000:
#     print("go to bobjib")
# elif cash < 30000:
#     print("don't eat")
# elif cash==0:
#     print("DIE!!")
#     if credit_card:
#         print("Killed")
# else:
#     print("WORK HARD")
