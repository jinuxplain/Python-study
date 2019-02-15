my_str_1="""
mult line string input\n
    \tyeah!
    """

print(f"{my_str_1}")

def my_func(input):
    a=input*2+1
    return a,input
a=33
print("a:{}, my_func(a):{}".format(*my_func(a)))
#unpack1 unpack2=*tuple 

