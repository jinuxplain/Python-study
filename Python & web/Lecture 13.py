#시작부분 코드
import time
start_time = time.time() 
#------------------------
"""
입력 받은 숫자가 3의 배수이면 "FIZZ" 
5의 배수이면 "BUZZ"
15의 배수이면 "FizzBuzz"를 출력하라
"""
import time
start_time = time.time() 
for i in range(1, 100+1):
    a = i % 3
    b = i % 5
    if a+b == 0:
        print(f"{i}FizzBuzz")
    elif a == 0:
        print(f"{i}FIZZ")
    elif b == 0:
        print(f"{i}BUZZ")
    else:
        pass
#----------------------------
#종료부분 코드
print("start_time", start_time) #출력해보면, 시간형식이 사람이 읽기 힘든 일련번호형식입니다.
print("--- %s seconds ---" %(time.time() - start_time))