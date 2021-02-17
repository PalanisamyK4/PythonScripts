a=int(input("please enter a 4 digit no"))
print(a)
if a>=999:
    d1=a//1000
    print(d1)
    b=a%1000
    print(b)
if b<999 and b>=99:
    d2=b//100
    c=b%100
if c<99 and c>=9:
    d3=c//10
    d=c%10
if d<=9:
    d4=d
print("The sum of the digits is: ", d1+d2+d3+d4)
