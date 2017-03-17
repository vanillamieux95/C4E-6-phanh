#list
#dictionary
#combo

## group of ppl buying things
# different in names, age

# person1: Nga, age: 18
# person2: Thanh, age: 17
# person3: Trong, age: 24


##person = {
##    "name" : ["Nga", "Thanh", "Trong"],
##    "age" : [18, 17, 24]
##    }
##print (person)
##print (person["name"][0]) #follow the tree frm root to branches
##

names = ["Nga","Trong","Manh"]

#### print in pair
persons = [
    {
        "name" : "Nga",
        "age": 18,
        "buy" : ["watermelon", "lemon"]
    },
    {
        "name" : "Trong",
        "age": 17,
        "buy": ["iphone7", "msi", "xbox"]
    },
    {
        "name" : "Manh",
        "age": 24,
        "buy": ["tomato"]
    }
    ]
##print (persons)
##print (persons[2]["age"])
#print (persons[1]["buy"][2]) # root: person -> no.of dict -> "<key>" -> index in <key> list

stock = {
    "watermelon" : 2,
    "lemon" : 1,
    "tomato": 0.5,
    "iphone7" : 20,
    "msi": 40,
    "xbox": 30
    }
#print(stock["tomato"])
#x = "iphone"
#print (stock[x])

###### print a sum of stock
b = ["watermelon","msi","lemon"]
total = 0 # -> always have total = 0 so that adter if want to sum it up, it will continue adding to total (cong don)
for stuff in b:
    print (stock[stuff])
    total = total + stock[stuff]

########### price of items in b = [2, 40, 1, 20]
#prices = [stock[item]for item in b]
#print (sum(prices)) #Tinh tong cua price

### Cach 2:


#### print in pair in short
totalall = 0
for i in range (len(persons)):

    person = persons[i]
    
    name = person["name"]
    age = person["age"]
    buy = person["buy"]
    
    prices = [stock[item] for item in buy]
    total = sum(prices)

    totalall = totalall + total
    
    input() #De chay tung doan
    
    print ("#", i)
    print ("name: {0}".format(name))
    print ("age: {0}".format(age))
    print ("buy: {0}".format(buy))
    print ("price: {0}".format(total))
print (totalall) 


#### Print with def:
#parameters (value passing) & return
def calculate_price(person):
    buy = person["buy"]
    
    prices = [stock[item] for item in buy]
    total = sum(prices)
    return total

def print_info(person):
    name = person["name"]
    age = person["age"]
    print ("name: {0}".format(name))
    print ("age: {0}".format(age))
    print ("buy: {0}".format(buy))
    
totalall = 0

for person in persons:
    print_info(person)
    price = calculate_price(person)
    print("price: {0}".format(price))

print ()
prices = [calculate_price]
    
    
    

totalall = totalall + total
    
input() #De chay tung doan
    
print ("#", i)
    
print ("price: {0}".format(total))
print (totalall)



### Them cap key- value vao dictionary
person = {
    "name": "Na",
    "age": 1
    }
print (person)
person["sex"] = "Female"
print (person)

### Lenh .sort() -> sap xep
l = [-2, 1, 3,4]
m = l.sorted()
print (m)

################################ EXCERCISE ###############################
    
