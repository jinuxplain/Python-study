# 심화 실습
a=list(range(1,4+1))
b=["one","two","three","four"]
c={}
if len(a)==len(b):
    i=0
    for i in range(len(a)):
        c[a.pop()]=b.pop()
print(a)
print(b)
print(c)

# # 예제 8) break point
# time = 1
# while True:
#     if time == 123:
#         print("break!!")
#         break
#     else:
#         print(time)
#         time += 1

# # 예제 7) pop list
# l = list(range(1, 2000+1))
# i = 0
# while l:
#     l.pop()
#     i += 1
# print(i)

# # 예제 6) dump list
# l = list(range(1, 2000+1))
# i = 0
# while l:
#     del l[0]
#     i += 1
# print(i)

# # 예제 5) 23423개의 블록으로 피라미드를 몇 층까지 쌓을 수 있을까?
# sum = 0
# i = 1
# while sum < 23423:
#     sum += i
#     i += +1
# print(i, sum)
# # 실습 1) 99단
# for i in range(1, 10):
#     print("{}단 시작".format(i))
#     for j in range(1, 10):
#         print("{}*{}={}".format(i, j, i*j))


# # 예제 4) enumerate
# a = {1: "a", 2: "A", 3: "b", 4: "C", 5: "d"}
# for i, j in enumerate(a):
#     print(i, j)
# # 예제 3)
# a = {1: "a", 2: "A", 3: "b", 4: "C", 5: "d"}
# for i, j in a.items():
#     print(i, j)
# # 예제 3)
# a = {1: "a", 2: "A", 3: "b", 4: "C", 5: "d"}
# for i in a:
#     print(i)
# for i in a.values():
#     print(i)
# # 예제 2) 1부터 100까지 더하기
# sum = 0
# for i in range(1, 100+1):
#     sum = sum+i
# print(sum)

# # 예제 1) for문
# a = {1, 2, 3, 4, 56, "s", 1}
# for i in a:
#     print(i)
