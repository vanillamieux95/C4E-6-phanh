#### LIST OF NUMBER ####
#2.1
size = [5, 7, 300, 90, 24, 50, 75]
print ("Hello, my name is P and these are my sheep sizes {0}".format(size))
print()

#2.2
print ("Now my biggest sheep has size {0} let's shear it".format(max(size)))
print()

#2.3
size[size.index(max(size))] = 8
new_size = size
print ("After shearing, here is my flock {0}".format(size))
print()

#2.4
first_month = [new_size + 50 for new_size in size]
print ("One month has passed, now here is my flock {0}".format(first_month))
print()

#2.5
size = [5, 7, 300, 90, 24, 50, 75]
print ("Hello, my name is P and these are my sheep sizes {0}".format(size))
a = [size + 50 for size in size]
m = max(size)

for n in range (1, 4):
    def month():
        for i in range (n):
            print ("Month {0}".format(i))
            print( "One month has passed, now here is my flock {0}".format(a))
            #print (len(a))
            print(len(first_month))
            print(max(size))
            #print( "Now my biggest sheep has size {0} let's shear it".format(a[m]))
##            size[size.index(max(size))] = 8
##            new_size = size
##            print( "After shearing, here is my flock {0}".format(new_size))
            #print (size)
month()
print()
