#from sys import argv
#script,fileN=argv
fileN=input("please enter the file name")
fileobj=open(fileN)
print(fileobj.readline())
print("next line checking")
print(fileobj.read())
fileobj.close()
#fileobj=open(fileN,'w+')
#fileobj.write("hello.testing")
#print(fileobj.read())
