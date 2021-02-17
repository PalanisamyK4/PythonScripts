a=[0,0,0,0]
a=input("please enter 4 numbers: ")
print(a)
for i in range(5):
    if a[i]>=a[i+1]:
        max=a[i]
    max=a[i+1]
print(max)
