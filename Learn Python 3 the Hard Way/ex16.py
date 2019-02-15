    from sys import argv

    scripts, filename =argv #unpacking argv

    print(f"We're going to erase {filename}.")
    print("If you don't want that, hit CRRL-C(^C).")
    print("If you want that, hit return.")

    input("?")#break point. program do not proceed untill user give return

    print("Opening thr file...")
    target=open(filename,'w') #open the file in write modde

    print("Truncating the file. Goodbye!")
    target.truncate() #clean up the file

    print("Now I'm going to ask you for three lines.")

    line1=input("line 1: ")
    line2=input("line 2: ")
    line3=input("line 3: ")
    #receive data from user
    print("I'm going to write these to the file.")

    line_sum_up=line1+"\n"+line2+"\n"+line3#Collect the data in a variable

    target.write(line_sum_up)#write the date

    print("And finally, we close it.")
    target.close()
