# 예제 5 ) 예약어 with
with open("fileio.txt","r") as f:
    print(f.read())
    
# # 예제 4 )
# f = open("fileio.txt", "r")
# data = f.readlines()
# f.close()
# for line in data:
#     print(line, end="")


# # 예제 3) 파일을 한 줄 씩 읽기
# f = open("fileio.txt", "r")
# while True:
#     data = f.readline()
#     if not data:
#         break
#     print(data, end='')
# f.close()

# # 예제 2) 파일을 읽기
# f = open("fileio.txt", "r")
# print(f.read())
# f.close()

# 예제 1) 파일을 열고 쓰고 닫기
# f = open("fileio.txt", "a")
# for i in range(1, 9+1):
#     data = f"5 * {i} = {5*i}\n"
#     f.write(data)

# f.close()
