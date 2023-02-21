def check_3tri():
    a=int(input("Enter no1: "))
    b=int(input("Enter no2: "))
    c=int(input("Enter no3: "))
    if(((a+b)<=c)or((b+c)<=a)or((c+a)<=b)):
        print("It can't form the triangle")

    elif (((a + b) >= c) or ((b + c) >= a) or ((c + a) >= b)):
        print("Triangle can be formed")
    else:
        print(25**25)-100
check_3tri()