# 예제 5) 딕셔너리의 병합
a = {
    1: "a",
    2: "b",
    3: "c"
}
k = a.keys()
v = a.values()
i = a.items()
print(a)
print(k)
print(v)
print(i)
del a[1]
print(a)
a.clear()
print(a)


# 예제 5) 딕셔너리의 병합
# a = {
#     1: "a",
#     2: "b",
#     3: "c"
# }
# b = {
#     "name": "이진우",
#     "job": "jobless"
# }
# c = {}
# c.update(a)
# c.update(b)
# print(c)

# # 예체 4) 값 추가/변경
# a = {0: "Ji"}
# a[0] = ["root"]
# a[1] = ["Ji"]
# print(a)

#  # 예제 3) 형변환 2
# a = ["Aa", "Bb", "Cc"]
# b = "aa", "bB","cC"
# print(dict(a))
# print(dict(b))

# # 예제 2) 이중 리스트를 딕셔너리로 형변환
# a = {
#     1 : "a",
#     2 : "b",
#     3 : "c"
# }
# b = [["d", 4], ["e", 5]]
# print(dict(b))

# #예제 1) 대학원에 입학한 진우
# jinwoo_info={
#     "name":"이진우",
#     "job":"jobless"
# }
# jinwoo_info["job"]="Grad."
# print(jinwoo_info["job"])
