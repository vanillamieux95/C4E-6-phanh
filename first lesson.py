#print ("Hello")

##n=input("what your name?")
##print ("Hello",n) 

##y=input("your year of birth?")
##y_int = int(y)
##age = 2016 - y_int
##print (age)
##
##if age < 6:
##    print ("baby")
##elif 6 <= age <18:
##    print ("teenager")
##else:
##    print ("adult")

#a*x**2 + b*x + c == 0
a = input("a = ")
b = input("b = ")
c = input("c = ")
a_int = int(a)
b_int = int(b)
c_int = int(c)

delta = b_int**2 - 4*a_int*c_int

if delta < 0:
    print ("Phuong trinh vo nghiem")
elif delta == 0:
    x = (-b_int)/(2*a_int)
    print ("Phuong trinh co nghiem kep", x)
else:
    x1 = (-b_int + (delta**0.5))/(2*a_int)
    x2 = (-b_int - (delta**0.5))/(2*a_int)
    print ("Phuong trinh co 2 nghiem", x1, x2)

