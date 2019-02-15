# 실습 예제 1)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = {1: 1, 2: 2, 11: 11, 12: 12}
A = set(a)
B = set(b)
print((B-A))
# # 예제 2 ) 집합 연산
# a = {1, 2, 3, 4, 5}
# b = {3, 4, 5, 6, 7, 8}
# print("a|b:{}".format(a | b))
# print("a&b:{}".format(a & b))
# print("a-b:{}".format(a-b))
# print("b-a:{}".format(b-a))
# print("a^b:{}".format(a ^ b))

# # 에졔 1 ) set으로 형변환
# a="AaAbBbsdafsdf"
# b=[1,2,3,2,32,3,1,23,123,12,3,43,5,356,3,24]
# c=(1,2,3,"a",4,3,"b")
# d={
#     1:"1",
#     2:"a",
#     3:"a",
#     4:5,
#     5:"1"
# }
# print(set(a))
# print(set(b))
# print(set(c))
# print(set(d))
# print(set(d.values()))
