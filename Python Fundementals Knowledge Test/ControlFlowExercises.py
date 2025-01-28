print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
print(x[0:5])


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
even_numbers = []
for number in x:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
even_numbers = []
for number in x[:5]:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
A_names = []
for name in names:
    if name[0] == "A":
        A_names.append(name)

print(A_names)




print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
index_space = []
for name in names:
    index = name.index(" ")
    index_space.append(index)
print(index_space)


print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
initials = []
for name in names:
    parts = name.split()
    first_initial = parts[0][0]
    last_initial = parts[1][0]
    initials.append(first_initial + last_initial)

print(initials)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:
new_list = []
for element in list_of_lists:
    if len(element) == len(set(element)):
        new_list.append(element)

print(new_list)

# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
number = int(input('type a number > 100: '))
while number <= 100:
    number = int(input('THAT IS NOT > 100, try again! >:|'))

print(f"Well Done! You entered: {number}")



print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
div_list = []
# Collect divisors
for i in range(1, number + 1):
    if number % i == 0:
        div_list.append(i)

# Check if the number is prime
if len(div_list) == 2:  #If Only 1 and the number itself are divisors
    print("prime")
else:
    print("not prime")

