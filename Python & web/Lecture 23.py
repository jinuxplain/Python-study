class PLAN_A:
    association = "PLAN_A"

    def management(self):
        print("P L A N _ A")


class APINK(PLAN_A):
    group = "APINK"

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def intro(self):
        print(f"Hi, This is APINK {self.name}")
    def management(self):
        print("FA")

naeun = APINK("NaEunSon", "25", "Main Dancer")

print(naeun.association)
naeun.management()
