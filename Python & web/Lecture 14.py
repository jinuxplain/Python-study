# 예제 4-2 gnerator expression
gen = (i for i in range(1, 5+1))
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#  # 예제 4-1  Tuple comprehension??
# some=(i*2 for i in range(1,10+1))
# print(some)

# # 예제 3-1 Dict comprehension 두 리스트를 묶어서 딕셔너리로 만들어보아라
# # {key:valuse for key,value in zip(iter1,iter2)}
# my_list_1 = [i for i in range(1, 5+1)]
# my_list_2 = ["one", "two", "three", "four", "five"]
# my_dict = {k: v for k, v in zip(my_list_1, my_list_2)}
# print(my_dict)


# # 예제 1-4 list comprehension 구구단
# gugu_list = [f"{i} * {j} = {i*j}" for i in range(1, 9+1) for j in range(1, 9+1)]
# print(gugu_list)

# # 예제 1-3 LIST comprehesion
# old_list = [1, 2, 3, 4, 5, 6]
# doubled_list = [i*2 for i in old_list if i % 2 == 0]
# print(doubled_list)

# # 예제 1-2 List comprehension
# old_list=[1,2,3,4]
# doubled_list=[i*2 for i in old_list]
# print(doubled_list)

# #예제 1-1 List
# old_list=[1,2,3,4]
# doubled_list=[]
# for i in old_list:
#     doubled_list.append(i*2)
# print(doubled_list)
