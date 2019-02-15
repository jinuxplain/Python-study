# 실습
some_list = [1, "1", "one", 4.567, {1: "one"}]
print(list(filter(lambda x: isinstance(x,str), some_list)))

# 예제 1) 리스트의 요소를 2배하기
# some_list = [1, 2, 3, 4, 5, 4, 3, 24, 4, 23, 4]
# result = list(map(lambda x: x*2, some_list))
# result_gen=map(lambda x: x*2, some_list)

# print(result)
# print(result_gen)
# print(next(result_gen))