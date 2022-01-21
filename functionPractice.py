# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def return_number(a, b):
    # if a%2 == 0 and b % 2 == 0:
    #     if a < b:
    #         result = a
    #     else:
    #         result = b
    # else:
    #     if a > b:
    #         result = a
    #     else:
    #         result = b
    # return result

    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(return_number(8, 2))


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(text):
    # wordlist = text.split()
    # first = wordlist[0]
    # second = wordlist[1]
    # return first[0] == second[0]

    worldlist = text.lower().split()
    print(text.split())  # Word adds to a list
    return worldlist[0][0] == worldlist[1][0]


print(animal_crackers('Crazy Lama'))


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def return_int(a, b):
    sum = a + b
    if sum == 20 or a == 20 or b == 20:
        return True
    else:
        return False
    # return (n1+n2)==20 or n1==20 or n2==20


print(return_int(1, 19))


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is to short'


print(old_macdonald('macdonald'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed

def reverse_sentence(text):
    # wordlist = text.split()
    # reverse_word_list = wordlist[::-1]
    # return reverse_word_list

    return ' '.join(text.split()[::-1])


print(reverse_sentence('We are ready'))


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def check_int(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


print(check_int(100))


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


mylist = [1, 2, 3, 3]
print(has_33(mylist))


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result


print(paper_doll('Mattias'))


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven,
# reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a, b, c):
    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
        return sum((a, b, c)) - 10
    else:
        return 'BUST'


print(blackjack(5, 6, 2))


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69([2, 1, 6, 9, 11]))


def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1


mylist = [1, 2, 3, 0, 0, 7]
print(spy_game(mylist))


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
def check_prime(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3, x, 2):  # test all odd factors up to x-1
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


print(check_prime(25))


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


print(count_primes(100))


# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# print_big('a') up to 'e'
#
# out:   *
#       * *
#      *****
#      *   *
#      *   *

def print_big(letter):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****', 5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ',
                9: '*    '}
    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5],
                'E': [4, 9, 4, 9, 4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


print(print_big('a'))


