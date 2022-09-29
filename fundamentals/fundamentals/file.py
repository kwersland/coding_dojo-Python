num1 = 42   #variable declaration, integer
num2 = 2.3  #variable declaration, float
boolean = True  #variable declaration, boolean
string = 'Hello World'  #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #variable declaration, dictionary
fruit = ('blueberry', 'strawberry', 'banana')   #variable declaration, tuple
print(type(fruit))  #type check, tuple
print(pizza_toppings[1])    #log statement, access value, list
pizza_toppings.append('Mushrooms')  #initialize, add value, list
print(person['name'])   #log statement, 'John', dictionary
person['name'] = 'George'   #change value, dictionary
person['eye_color'] = 'blue'    #initialize, dictionary
print(fruit[2])     #log statement, tuple, access value

if num1 > 45:    #conditional, if
    print("It's greater")   #log statement
else:           #conditional, else
    print("It's lower") #log statement

if len(string) < 5: #conditional, if, length check
    print("It's a short word!") #log statement, string
elif len(string) > 15:  #conditional, elif, lenght check
    print("It's a long word!")  #log statement, string
else:               #conditional, else
    print("Just right!")    #log statement, string

for x in range(5):  #for loop, stop
    print(x) #log statement
for x in range(2,5):    #for loop, start, stop
    print(x)    #log statement
for x in range(2,10,3): #for loop
    print(x)    #log statement
x = 0   #variable declaration
while(x < 5):   #while loop
    print(x)    #log statement
    x += 1  #increment

pizza_toppings.pop()    #list, delete value, last value
pizza_toppings.pop(1)   #list, delete value, 2nd value (index[1])

print(person)   #log statement, dictionary
person.pop('eye_color') #dictionary, delete value
print(person)   #log statement, dictionary

for topping in pizza_toppings:  #for loop, 
    if topping == 'Pepperoni':  #conditional, start, if, 
        continue    #for loop, continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional, if
        break   #for loop, break, end

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)