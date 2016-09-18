############# EXCERCISE 1 ################

#### I ####
inventory = {
   'gold' : 500,
   'pouch': ['flint', 'twine', 'gemstone'],
   'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
#1
inventory['pocket'] = []
#2
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
#3
print (sorted(inventory['pocket']))
#4
del inventory['backpack'][1]
#5
inventory['gold'] = inventory['gold'] + 50

#### II ####
prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
    }

#1
stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
    }
def print_info():
    for k1 in prices:
        print (k1)
        print ("Price: ", prices[k1])
        print ("stock", stock[k1])
        print()
print_info()
total = 0
for k2 in prices:
    total = total + stock[k2] * prices[k2]
print ("if we sold out all of them, we can earn in total: {0}".format(total))


#### III ####
groceries = ['banana', 'orange', 'apple']
prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
    }
stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
    }
##total = 0
##for x in groceries:
##    def comput_bill(x):
##        total = total + prices[x]
##        return total
