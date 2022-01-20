st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)

print(list(range(0,11,2)))

mylist = [x for x in range(1,51) if x%3 == 0]
print(mylist)

st = 'Print every word in this sentence that has an even number of letters'
for string in st.split():
    if len(string)%2 == 0:
        print(string)

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('Fizzbuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st.split(' ')])
text = st.split()
print(type(text))





