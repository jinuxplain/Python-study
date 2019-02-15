
def print_two(*args): #define fuction print_two
    arg1, arg2=args #unpacking args(tuple) to two strings
    print(f"arg1 : {arg1}, arg2 : {arg2}")

def print_two_again(arg1,arg2):#define function print_one
    print(f"arg1 : {arg1}, arg2 : {arg2}")

def print_one(arg1): #define function print_one
    print(f"arg1 : {arg1}")

def print_none(): #define function print_none
    print("I got nothin'.")

print_two("Zwd","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()