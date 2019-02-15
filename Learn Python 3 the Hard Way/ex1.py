print("hello world")
print('hello "world"')
print("hello 'world'")
print("hello \"world\"") # a quote can be escaped by using the '\'
print(3) #octothorpe (pound, hash or mesh) is used for annotations
#how can we make multple line?
print("""multiple
lien""")#use ''' or """
'''
i'm
multiple comment line
'''
print('multiple \
line')

print("i\nm",end='\n') # use \n
#some useful arguments
print(3,3,sep='\n') # string inserted between values, default a space
print(3,end='end') #string appended after the last value, default a newline.
