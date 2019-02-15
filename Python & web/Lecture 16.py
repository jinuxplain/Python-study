# 에제 1-3 ) size of generator
import sys
print(sys.getsizeof([i for i in range(1,20000+1)]))
print(sys.getsizeof((j for j in range(1,20000+1))))


# # 예제 1-2 ) generator
# def generator():
#     yield "hello"
#     yield "it's me"
#     yield "I was wondering if after all these years you'd like to mee"
#     yield "To go over everything"


# gen = generator()
# for i in gen:
#     print(i)

# # 예제 1-1 ) generator
# def generator():
#     yield "hello"
#     yield "it's me"
#     yield "I was wondering if after all these years you'd like to mee"
#     yield "To go over everything"


# gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
