num = 65
for i in range (0,5):
    for k in range (5,i,-1):
        print("  ",end="")
    for j in range (0,i+1):
        num1=chr(num)
        print(num1,end="   ")
    num = num + 1
    print("\n")
