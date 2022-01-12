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