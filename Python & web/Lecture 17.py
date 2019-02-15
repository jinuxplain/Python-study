import random


def pizzbuzz(maxnum):
    if (type(coins) == int):
        pass
    else:
        print("input int only!")
        return -1
    for i in range(1, maxnum+1):
        if i % 3 == 0:
            if i % 5 == 0:
                print("PIZZBUZZ")
            else:
                print("PIZZ")
        elif i % 5 == 0:
            print("BUZZ")
        else:
            pass


def numguess(coins):
    if (type(coins) == int):
        pass
    else:
        print("input less than 5 coins at once. and input only coins!")
        return -1
    answer = random.randint(1, 50)
    score = 1
    while 1:
        try:
            your_answer = int(input("1~50 사이의 정수를 입력해주세요\n"))
        except ValueError:
            print("올바른 값을 넣으시오")
        else:
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
