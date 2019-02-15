# 예제 1) 숫자 만들기 게임 개선!
"""
1. 난수 생성
2. 숫자 입력
3. 난수와 같읕지 확인
4-1  오답 :up and down 
4-2  정답 : 점수 출력
4-3 기회를 다 쓰면 실패
"""
import random
answer = random.randint(1, 50)
score = 1
while 1:
    try:
        your_answer = int(input("1~50 사이의 정수를 입력해주세요\n"))
    except ValueError:
        print("올바른 값을 넣으시오")
    else:
        if score>5:
            print("기회는 5번 뿐 후후후! 다시 도전해 보라구")
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
