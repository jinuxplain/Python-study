def brk_and_sort_and_print(str):
    str = str.split(" ")
    str = sorted(str)
    print(str)
    return str


def kill_first_and_last(my_list):
    print(my_list.pop(0))
    print(my_list.pop(-1))
    return my_list


def just_pirnt_first_and_last(my_list):
    print(my_list[0])
    print(my_list[-1])


my_str = "zzx aa aab aa a bc bb ba"
my_list = brk_and_sort_and_print(my_str)
my_list = kill_first_and_last(my_list)
print(f"my_list : {my_list}")
just_pirnt_first_and_last(my_str)
just_pirnt_first_and_last(my_list)
