from sys import argv
script, fName=argv
#fName=input("Please type the name of your file\n")
f=open(fName,'w')
print(f.read())
f.truncate()
print("this has become empty", f.read())
f.write("\n\nI added these additionaly")
print(f.read())
