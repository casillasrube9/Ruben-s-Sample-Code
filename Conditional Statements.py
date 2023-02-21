#If-Then-Else-If statement
#It only runs if the original if wasn't true
#Multiple Else-Ifs: We must start with an if and we can have at most one else.
#but we can have at most one else. But we can have any number of else-ifs in between
#We can have an if-then else-if without having a final else



#This is an excercie to practice conditional statements
Sale = "Chocolate Donuts"


if Sale == "Chocolate Donuts":
    print(f"If {Sale} are on sale, buy me a half-dozen of those")
elif Sale == "jelly donuts":
    print("buy me 3 of those")
elif Sale == "cake donuts":
    print("buy me 8 of those")
else:
    print(f"Otherwise, buy me a dozen glazed {Sale}")



#Practice Excercise #1
craving = "pizza"

if craving == "tacos":
    print("Go to Takorea!")
elif craving == "sushi":
    print("Go to Satto!")
elif craving == "pizza":
    print("Go to Ray's!")


#coding excercise number 1
#we are looking to see if 5 and 15 are factors of each other
mystery_int_1 = 15
mystery_int_2 = 5

if mystery_int_1 % mystery_int_2 or mystery_int_2 % mystery_int_2 == 0:
    print("Factors!")
else:
    print("Obviously not a factor!!!")



#Sample excercise using input
def check_3tri():
    a=int(input("Enter no1: "))
    b=int(input("Enter no2: "))
    c=int(input("Enter no3: "))
    if(((a+b)<=c)or((b+c)<=a)or((c+a)<=b)):
        print("It can't form the triangle")

    else:
        if (((a + b) >= c) or ((b + c) >= a) or ((c + a) >= b)):
            print("Triangle can be formed")
    else:
        print(25**25)-100
check_3tri()


