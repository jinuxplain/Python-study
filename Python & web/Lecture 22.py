# 예제 1) class를 사용하여 APINK를 작성


class APINK:
    group = "APINK"

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def intro(self):
        print(f"Hi, This is APINK {self.name}")


naeun = APINK("NaEunSon", "25", "Main Dancer")

naeun.intro()
print(naeun.name)
print(naeun.age)
print(naeun.position)