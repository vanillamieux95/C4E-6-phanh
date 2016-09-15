##### LIST OF STRING  #####
#1.1
color = ["Blue", "Red", "Green", "Pink", "White", "Black"]
print (color)

#1.2
print (color[3])

#1.3
a = int(input("Enter a number from 0-5: "))
print ("Your color: " + color[a])

#1.4
print (color)
for color in color:
    print (color)

#1.5
##b = input("What is your favorite color? ")
##
##for i in range (len(color)):
##    if color[i] == b:
##        print ("Your color is at index {0} in my list".format(i))
##
##    else:
##        print ("Sorry, I could not find your color")
##        break

#********************************************************************#
#### LIST OF NUMBER ####
#2.1
size = [5, 7, 300, 90, 24, 50, 75]
intro = "Hello, my name is P and these are my sheep sizes {0}".format(size)
print (intro)

#2.2
max_size = max(size)
cau2_2 = "Now my biggest sheep has size {0} let's shear it".format(max_size)
print (cau2_2)

#2.3
size[size.index(max_size)] = 8
#new_size = size[size[size.index(max_size)]]
cau2_3 = "After shearing, here is my flock {0}".format(size)
print (cau2_3)

#2.4
first_month = [size + 50 for size in size]
cau2_4 = "One month has passed, now here is my flock {0}".format(first_month)
print (cau2_4)

#2.5
size = [5, 7, 300, 90, 24, 50, 75]
print (intro)


for n in range (1, 4):
    def month():
        max_size = max(size)
        first_month = [size +50 for size in size]
        for i in range (n):
            print ("Month {0}".format(n))
            print( "One month has passed, now here is my flock {0}".format(first_month))
            print( "Now my biggest sheep has size {0} let's shear it".format(max_size))
            print( "After shearing, here is my flock {0}".format(size))
    month()
break
            
            

##def month():
##    print (cau2_4)
##    print (cau2_2)
##    print (cau2_3)
##
##print("month 1: ")
##month()
##print("month 2: ")
##month()
##print("month 3: ")
##month()
