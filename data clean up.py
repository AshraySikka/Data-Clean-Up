s1 = input("Enter the scanned string: ")
new = ''
for i in s1:
    if i.isalpha() or i.isspace():
        new=new+i
    else:   
        new=new+' '
print('Cleaned Version: ', new)
