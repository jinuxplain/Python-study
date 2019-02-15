# 예제 1) class를 사용하여 APINK를 작성


class APINK:
    group = "APINK"

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def intro(self):
        print(f"APINK {self.name}")


naeun = APINK("손나은", "25", "APINK")

naeun.intro()


# def naeun(name, age, position):
#     return_dict = {
#         "name": name,
#         "age": age,
#         "position": position
#     }
#     return return_dict


# apink("naeun", "25", "Main Dancer")


# def introduce(name):
#     print("Hi I'm {name}")
