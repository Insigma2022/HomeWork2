import math
a = int(input("Enter side a="))
b = int(input("Enter side b="))
c = int(input("Enter side c="))

if a + b > c:
    if a + c >b:
        if b + c > a:
            p = (a + b + c) / 2
            s = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print("The area of the triangle is:\n ")
            print(s)
            print("Yes, are the sides of the triangle")
        else:
            print(" 'a' Error")
    else:
        print(" 'b' Error")
else:
    print(" 'c' Error")