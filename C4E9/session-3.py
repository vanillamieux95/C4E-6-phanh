name0 = "Thao"
name1 = "V.A"
name3 = "Son"
name4 = "Hoang"
name5 = "Trung"
name6 = "V.A k xoan"
name7 = "Duc"
name8 = "Khai Anh"
name9 = "Bach"

names = ["Thao", "V.A", "Son", "Hoang", "Trung"]

#Adding object to list
names.append("V.A k xoan")

#index - accessing each items in list (update)
names[-1] = "Claudia"

#Deleting
names.remove("V.A")

##for name in names:
##    print ("Hi ", name)


#.strip() -> take off enter space, special character in line
file = open ("c4e-name.txt")
for line in file:
    name = line.strip()
    word = name.split()
    print (word)
    print ("Hi ", word[-1])
    
