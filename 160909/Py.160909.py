##from turtle import *
##
##speed (-1)
##
##for j in range (12):
##    for i in range (4):
##        forward (121)
##        left (90)
##    left (30)
##
###    print ("hihi")
###    print (i)
##print ("ahihi")
##mainloop()
##

##from turtle import *
##shape ("turtle")
##speed (-1)

##for n in range (10,2,-1):
##    
##    for i in range (n):
##        forward (121)
##        left (180 - (180*(n-2))/n)
##
##for i in range (4):
##    forward (121)
##    left (180 - (180*(4-2))/4)
##    
##for i in range (5):
##    forward (121)
##    left (180 - (180*(5-2))/5)
##
##for i in range (6):
##    forward (121)
##    left (180 - (180*(6-2))/6)
#circle (121)

##color("yellow", "red")
##for n in range (10,2,-1):
##    begin_fill()
##    for i in range (n):
##        forward (121)
##        left (180 - (180*(n-2))/n)
##    end_fill()
##mainloop()

##s = "techkids"
##print (s)
##n = 1
##print (s + ",", n)
##
###print (s+",", str(n) + "year anniversary")
##h = "{0}, {1} year anniversary".format(s,n)
##print (type(h))
##print (h)

while True:
    y = int(input("your year of birth"))
    age = 2016 - y
    print (age)

    if age < 6:
        print ("child")
    elif 6 <= age <= 18:
        print ("teenage")
    else:
        print ("not a child")

    if  age == 18:
        print ("10 years old")
    
