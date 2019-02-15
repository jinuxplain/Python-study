# start_time = time.time()
# for i in range(1, 100000+1):
#     if i % 15 == 0:
#         pass
#     elif i % 3 == 0:
#         pass
#     elif i % 5 == 0:
#         pass
#     else:
#         pass


for i in range(1, 100+1):
    if i % 3 == 0:
        if i % 5 == 0:
            print("PIZZBUZZ")
        else:
            print("PIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        pass

