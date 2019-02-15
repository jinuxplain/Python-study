# 예제 2) make iterator
my_range = range(1, 100+1)
my_range=iter(my_range)
my_list = [1, 2, 3, 4, 5]
my_list=iter(my_list)
my_set = {1, 2, 3, 4, 5}
my_set=iter(my_set)
my_str = "12345"
my_str=iter(my_str)


print(next(my_list))
print(type(my_list))

print(next(my_range))
print(type(my_range))

print(next(my_set))
print(type(my_set))

print(next(my_str))
print(type(my_str))




#  #예제 1) Iterator
# my_range=range(1,100+1)
# my_list=[1,2,3,4,5]
# my_set={1,2,3,4,5}
# my_str="12345"
# # # print(next(my_list))
# # print(next(my_range))
# # print(next(my_set))
# print(next(my_str))
