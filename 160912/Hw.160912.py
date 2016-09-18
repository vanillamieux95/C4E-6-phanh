##### LIST OF STRING  #####
#1.1
color = ["Blue", "Red", "Green", "Pink", "White", "Black"]
print (color)
print()
#1.2
print ("color_list at index 3: {0}".format(color[3]))

#1.3
a = int(input("Enter a number from 0-5: "))
print ("Your color: " + color[a])
print()
#1.4
print (color)
for color in color:
    print (color)
print()
#1.5
b = str(input("What is your favorite color? "))

found = False
for i in range (len(color)):
    if b == color[i]:
        print ("Your color is at index {0} in my list".format(i))
        found == True

    elif found == False:
        print ("Sorry, I could not find your color")
    break
print()
#********************************************************************#
#### LIST OF NUMBER ####
#2.1
size = [5, 7, 300, 90, 24, 50, 75]
intro = "Hello, my name is P and these are my sheep sizes {0}".format(size)
print (intro)
print()
#2.2
cau2_2 = "Now my biggest sheep has size {0} let's shear it".format(max(size))
print (cau2_2)
print()
#2.3
size[size.index(max(size))] = 8
cau2_3 = "After shearing, here is my flock {0}".format(size)
print (cau2_3)
print()
#2.4
first_month = [size + 50 for size in size]
cau2_4 = "One month has passed, now here is my flock {0}".format(first_month)
print (cau2_4)
print()
#2.5
size = [5, 7, 300, 90, 24, 50, 75]
print (intro)

for n in range (1, 4):
    def month():
        for i in range (n):
            print ("Month {0}".format(i))
            print( "One month has passed, now here is my flock {0}".format([size + 50 for size in size]))
            print( "Now my biggest sheep has size {0} let's shear it".format(first_month[max(size)]))
            size[size.index(max(size))] = 8
            new_size = [size + 50 for size in size]
            print( "After shearing, here is my flock {0}".format(new_size))
            #print (size)
month()
print()
#2.6

            
