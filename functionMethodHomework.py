# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as 4/3*PI**3
def vol(rad):
    return (4 / 3) * (3.14) * (rad ** 3)


print(vol(2))


# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_bool(num, low, high):
    return low < num < high


print(ran_bool(11, 2, 10))


def ran_check(num, low, high):
    if low < num < high:
        print(f'{num} is in the range between {low} and {high}')
    else:
        print('Number our of range')


print(ran_check(4, 1, 10))


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def calc_string(text):
    d = {'upper': 0, 'lower': 0}
    # lower = 0
    # upper = 0
    for letter in text:
        if letter.isupper():
            d['upper'] += 1
            # upper += 1
        elif letter.islower():
            d['lower'] += 1
            # lower += 1
    print(f'Original string: {text}')
    print(f'{d["lower"]} lower letters and {d["upper"]} letters')


print(calc_string('Hello, how are you this fine Thursday?'))


# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(arr):
    # return list(set(arr))
    seen_numbers = []
    for nums in arr:
        if nums not in seen_numbers:
            seen_numbers.append(nums)
    return seen_numbers


mylist = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]

print(unique_list(mylist))

def multiply(numbers):
    total = 1
    for num in numbers:
        for num in numbers:
            total = total * num
        return total

print(multiply(mylist))

def palindrome(str):
    str = str.replace(' ','')
    return str == str[::-1]

print(palindrome('nurses run'))

import string

def ispangram(str, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    str = str.replace(' ','')
    str = str.lower()
    str = set (str)
    return str == alphaset

print(ispangram("The quick brown fox jumps over the lazy dog"))