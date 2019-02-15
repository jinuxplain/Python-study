from sys import argv

script, filename = argv

txt=open(filename,newline='\n',mode='r+')

print(f"Here's your file {filename}:")
print(txt.read())
txt.write('\rend')

print("Type the filename again:")
file_again=input(">")

txt_again=open(file_again,mode='r+')

print(txt_again.read())
