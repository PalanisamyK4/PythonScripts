#the amount will be given as input
#the program will calculate the least no of coins to give that amount
a=int(input("Please enter the balance amount that you give"))
if a>=10:
    if a%10==0:
        print(a//10, " no of Rs.10 coins")
    else:
        print(a//10, " no of Rs.10 coins")
        a%=10

if a>=5 and a<10:
    if a%5==0:
        print(a//5, " no of Rs.5 coins")
    else:
        print(a//5, " no of Rs.5 coins")
        a%=5
if a>=2 and a<5:
    if a%2==0:
        print(a//2, " no of Rs.2 coins")
    else:
        print(a//2, " no of Rs.2 coins")
        a%=2

if a>=1 and a<2:
    print(a, " no of Rs.1 coins")
