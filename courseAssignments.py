add = 2 + 5
sub = 5 - 2
div = 4 / 2
mod = 50 % 5

print(add,
      sub,
      div,
      mod)

powers = 2 ** 3

print(powers)
mathTest = (2 + 10 * 10 + 3)
print(mathTest)
math_test2 = ((2 + 10) * (10 + 3))
print(math_test2)
math1 = 0.1 + 0.2 - 0.3
print(math1)

name = "Mattias"
print(len(name))
print(name[0])
print(name[-2])
print(name[2])
print(name)
print(name[2:])
print(name[:2])
print(name[2:4])
print(name[4:6])

name1 = "Sam"
# name1[0] = "P" for changing S to P doenst work, Strings are immutable
last_letters = name1[1:]
print(last_letters)
print('P' + last_letters)

print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 100 / 777
print("The result was {r:1.3f}".format(r=result))

my_list = [1, 2, 3]
mylist = ["one", "two", "three"]
another_list = ["four", "five"]
print(len(my_list))
print(my_list[1:])
print(my_list[0])
new_list = mylist + another_list
print(new_list)
test_list = new_list + my_list
print(test_list)
new_list[0] = "ONE ALL CAPS"  # Change to an index
print(new_list)
new_list.append("six")  # Adding to the list
print(new_list)
new_list.pop()  # Removing the added item
print(new_list)
new_list.append("six")
popped_item = new_list.pop()
print(popped_item)
abc_list = ["a", "c", "b"]
abc_list.sort()
num_list = [1, 3, 5, 2, 4]
num_list.sort()
print(abc_list)
print(num_list)
num_list.reverse()
print(num_list)

my_dict = {"key1": ["a", "b", "c"]}
mylist = my_dict["key1"]
letter = mylist[2]
print(letter)  # printing c
print(letter.upper())
print(my_dict["key1"][0].upper())
my_dict = {"key1": 100, "key2": 200}
my_dict["key3"] = 300
print(my_dict)
my_dict["key1"] = "NEW VALUE"
print(my_dict)
print(my_dict.values())
print(my_dict.keys())

t = (1, 2, 3)
print(t)
# t[0] = 2  assignments doesnt work

myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(2)  # <---- wont add the second 2. sets are unique collections
myset = set('Mississippi')  # returning s p i M
print(myset)

# ---- Booleans

a = 1 > 2
b = 1 == 1
print(a)
print(b)

with open('test.txt', mode='r') as f:
    print(f.read())
# with open('test.txt', mode='a') as f:
# f.write('\nHej världen')
# with open('test.txt', mode='r') as f:
# print(f.read())
# with open('newFile', mode='w') as f:    SKAPAR EN NY TXT FIL
# f.write('I CREATED THIS FILE')
with open('newFile', mode='r') as f:
    print(f.read())
myfile = open('test.txt', 'w')
myfile.write('testing')
myfile.close()

# ------ Comparison operators
# and , or , not
print("Operators comparison")
a = 1 < 2 > 3
print(a)
b = 1 < 2 and 2 < 3
c = 'h' == 'h' and 2 == 2
print(b, c)
d = 1 == 1 or 2 == 1
print(d)
a = not 400 > 5000
print(a)

# ------ IF ELIF ELSE

if True:
    print("ITS TRUE")

if 3 > 2:
    print('ITS TRUE')

hungry = True
if hungry:
    print("FEED ME")
else:
    print("Im not hungry")
loc = "Store"
if loc == 'Auto shop':
    print("Cars are cool")
elif loc == "Bank":
    print("Money is cool")
elif loc == "Store":
    print("Welcome to the store")
else:
    print("I do not know much")

name = "Sammy"
if name == "Frankie":
    print("Hello Frankie")
elif name == "Sammy":
    print("Hello Sammy")
else:
    print("What is your name")

# --------- FOR LOOPS

my_iterable = [1, 2, 3]
for item_name in my_iterable:
    print(item_name)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number:{num}')

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print(list_sum)

mystring = 'Hello World'
for letter in mystring:
    print(letter)
tup = (1, 2, 3)
for item in tup:
    print(item)
mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]  # TUPLEINPACKING
for item in mylist:
    print(item)
for a, b in mylist:
    print(a)
    print(b)

mylist = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]
for a, b, c in mylist:
    print(b)
    print(a)
    print(c)

d = {"k1": 1, "k2": 2, "k3": 3}
for item in d:  # Returns the keys
    print(item)
for item in d.items():  # Returns keys with values
    print(item)
for item, value in d.items():  # Returns values
    print(value)

# ------ WHILE LOOPS
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1  # x = x + 1
else:
    print("X IS NOT LESS THAN 5")
# Break, continue, pass
x = [1, 2, 3]
for item in x:
    pass  # Skip this loop
print("Hello World")

mystring = "Sammy"
for letter in mystring:
    if letter == "a":
        continue
    print(letter)

mystring = "Sammy"
for letter in mystring:
    if letter == "a":
        break
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

# -------- USEFUL OPERATORS
print("break")
x = [1, 2, 3]
for num in range(2, 11):
    print(num)

print(list(range(0, 11, 2)))

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1
index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

index_count = 0
word = 'abcde'
print('Enumerate')
for letter in enumerate(word):
    print(letter)
    index_count += 1
print('Zip')
mylist1 = [1, 2, 3, 4, 5, 6]
mylist2 = [a, b, c]
mylist3 = [100, 200, 300]
for item in zip(mylist1, mylist2, mylist3):
    print(item)
print(list(zip(mylist1, mylist2, mylist3)))
print('IN OPERATOR')
print('x' in [1, 2, 3])
print('x' in ['x', 'z', 'a'])
print('a' in 'a world')
print('mykey' in {'mykey': 234})
d = {'mykey': 345}
print(345 in d.values())
print("MIN/MAX")
print(min(mylist1))
print(max(mylist1))
print("IMPORT SHUFFLE")
from random import shuffle

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist)
print(mylist)
print("GRABBING RANDOM INT BETWEEN 0 - 100")
from random import randint

mynum = randint(0, 100)
print(mynum)
print("INPUT")
# result = input("Whats your fav number: ")
# print(result)                              Always returning in type string
# flost(result) / int(result) / result = int(input('Whats your fav number: ') TO RETURN IN OTHER THAN A STRING
print('LIST COMPREHENSIONS')  # quick way of create an unique list
mystring = 'Hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

mystring1 = 'Mattias'
mylist1 = [letter for letter in mystring1]
print(mylist1)
mylistX = [lol for lol in 'Hello world']
print(mylistX)
mylist = [num ** 2 for num in range(0, 11)]
print(mylist)
mylist = [x for x in range(0, 11) if x % 2 == 0]
print(mylist)
celcius = [0, 10, 20, 34.5]
fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9 / 5) * temp + 32))
print(fahrenheit)
fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
print(fahrenheit)

results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(results)

mylist = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        mylist.append(x * y)
print(mylist)
mylist = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(mylist)


# ----------------- FUNCTIONS

def my_function():
    """
    Docstring
    """
    print("Hello World")


# def new_function(a):
#     """
# Test of input
#     """
#     a = input(str)
#     return a
# print(new_function(a))

def add_function(num1, num2):
    """
add funtion
    """
    sum = num1 + num2
    return sum


print(add_function(2, 4))


def check_even(num):
    return num % 2 == 0


print(check_even(21))


def check_list_even(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False


print(check_list_even([1, 3, 5, 4]))


def check_list_even_numbers(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers


print(check_list_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

work_hours = [('Abby', 100), ('Billy', 4000), ('Cassidy', 600)]


def check_employee(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max)


print(check_employee(work_hours))
name, hours = check_employee(work_hours)
result = check_employee(work_hours)
print(result)
print(name)
print(hours)
stock_prices = [('APPL', 200), ('GOOGL', 600), ('MSFT', 100)]


def check_stock(prices):
    """
Check stockprice with 10% increase
    :param prices:
    """
    for company, price in prices:
        print(price + (0.1 * price))


print(check_stock(stock_prices))


# --------- ARGS

def myfunc(*args):  # ------ tuple can take unlimited of inputs. * with any argument
    return sum(args) * 0.05


print(myfunc(100, 100, 100, 100, 100))


# ---------- KWARGS

def myfunc2(**kwargs):  # ------ dictonary
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


print(myfunc2(fruit='apple', veggie='lettuce'))


def myfunc3(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))


print(myfunc3(10, 20, 30, fruit='orange', food='eggs', animal='dog'))


def my_even_func(*args):
    mylist = []
    for num in args:
        if num % 2 == 0:
            mylist.append(num)
    return mylist


print(my_even_func(1, 2, 3, 4, 5, 6))


def my_string_func(args):
    string = ''
    for letter in range(0, len(args)):
        if letter % 2 == 0:
            string = string + args[letter].lower()
        else:
            string = string + args[letter].upper()
    return string


print(my_string_func('MATTIAS'))


# ----------- MAP

def square(num):
    return num ** 2


my_num = [1, 2, 3, 4, 5]
for item in map(square, my_num):
    print(item)
print(list(map(square, my_num)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Mattias', 'Theo', 'Ines', 'Cassandra']
print(list(map(splicer, names)))


# ------------------- FILTER
def check_even(nums):
    return nums % 2 == 0


my_num = [1, 2, 3, 4, 5, 6]
print(list(filter(check_even, my_num)))
for i in filter(check_even, my_num):
    print(i)


def square2(num):
    result = num ** 2
    return result

#----------------- LAMBDA
lambda num: num ** 2

print(list(map(lambda num : num ** 2,my_num)))

print(list(filter(lambda num : num % 2 == 0,my_num)))

print(list(map(lambda x:x[::1], names)))

#----------------- NESTED STATEMENT AND SCOPE
