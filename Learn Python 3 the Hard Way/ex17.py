from sys import argv
from os.path import exists

script, from_file, to_file = argv #unpacking argv

print(f"Copying from {from_file} to {to_file}")

infile=open(from_file,'rt', encoding='cp949') #open file and read
indata=infile.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the ouput file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CLTR-C to abrot")
input() #break point.


out_file=open(to_file, 'w')
out_file.write(indata) #write file

print("Alright, all done")

out_file.close()
