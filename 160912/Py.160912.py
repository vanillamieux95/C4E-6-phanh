names = ["Trong", "hoang", "phanh", "duc"]

print (names)
print (type(names))
print(names[0])

for names in names:
    print (names)
#    print (names, " xinh")

##names.append("manh")
##names

##** Remove by value
##names.remove("duc")
##names

##for i in range (len(names)):
##    print (names[i])


#          Excercise:
##1. List string: 3 person in class
##        a, add the 4th
##        b,add word

##c4e = ["Ha", "Nga", "Duc" ]
##print (c4e)
##
##c4e.append("Huy")
##print (c4e)
##
### Cach 1:
####for c4e in c4e:
####    print ("Halo ", c4e)
##
### Cach 2:
##x = ["Halo " + c4e for c4e in c4e]
##print (x)
##
###eg:
##numbers = [4,5,6]
##new_list = [numbers + 2 for 
##print 

##2. Open a .txt file (full names of ppl included: Le Van Hoang,
## Nguyen Hoang Nam, Nguyen Pham Phuong Anh)
##   Split string
##   "Hello Ha, Happy coding"

##f = open("name-list.txt")
##for line in f:
##    print (line)
    
#Split String python
    #function name
    #output => (type) => list

##s = "Nguyen Van A" #-> ["Nguyen", "Van", "A"]
##x = s.split()
##print (x)

#DOING EXCERCISE 2:
##f = open("name-list.txt")
##for line in f:
##    print ("line: ", line)
###splitted line 
##    splitted_line = line.split()
### Getting the first name
##    firstname = splitted_line[-1]
##    #l = len(splitted_line)
##    #firstname = splitted_line[l -1]
###addinh Hello, happy coding
##    print ("Hello {0}, happy coding".format(firstname))
   

##** Remove by index
##names.pop() # -> remove the last value. if add number of value in (), it will remove the value w the number added
##print (names)





####***************************************************************
##              DICTIONARY

#represent by {}
#all key in dictionary must be STRING
x = ["hoang", 18, "HUST", "single", "male"]

person = {
    'name' : 'hoang', #-> coma is a must
    'age': 18,
    'school': "HUST",
    'status': "single",
    'gender': "male", #-> no need comma for the last key
    }
#print (person)

##list is sth w order (cuz it access w index) but dictionary is not (cuz it will arrange by the size of the key)!!!!

#print (person['name'])

#person['name'] = "Trong" #-> to replace the value in key!
#print (person)

#for k in person:
#    print (k, person[k])

#for k, v in person.items(): #-> items(): la 1 ham tra lai cap key-value
#    print (k,v)


####****************************************************************
##          CAU LENH BREAK
##Eg:
#for i in range (5)
#    print (i)
#    if i == 3:
#        break

## :
names = ["hoang", "nga", "trong", "nam"]
#x = "nga"
found = False
#found_index = -1

for i in range(len(names)):
#    print (names[i])
    name = names[i]
    if name == x:
        print ("Nga is found at index {0}".format(i))
        break #-> dung khi da tim thay

if not found:
    print ("Nga is not found")
#########      Tong Ket      #########
