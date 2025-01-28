from pywin.framework.interact import valueFormatOutputError
from sympy import false

print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def division_list(n):
    div_list=[]
    for i in range(1, n+1):
        if n%i == 0:
            div_list.append(i)
    return div_list

division_list(124)

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def factor_check(int1, int2):
    div_list_1 = division_list(int1)
    div_list_2 = division_list(int2)
    if int1 in div_list_2:
       return True
    elif int2 in div_list_1:
        return True
    else:
        return False

print(factor_check(22,44))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def alpha_pos(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letter = letter.lower()
    if letter in alphabet:
        position = alphabet.index(letter) + 1
        return position
    else:
        return "Invalid input"

print(alpha_pos("D"))



print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def name_id(name):
    id_num = ""
    for letter in name:
        id_num += str(alpha_pos(letter))
    return int(id_num)
name_id('Ibrahim')

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def password_make(name):
    id_num = name_id(name)
    number_list = []
    for number in str(id_num):
        number_list.append(int(number))
    sum_id = sum(number_list)
    password = id_num - sum_id
    return password

password_make('jeff')
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def prime_check(integer):
    if len(division_list(integer)) == 2:
        return True
    else:
        return False

print(prime_check(22))


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def prime_check(integer):
    while isinstance(integer, int):
        try:
            if len(division_list(integer)) == 2:
                return True
            else:
                return False
        except ValueError:
            input('this is not an integer try again: ')

prime_check('hi')

# couldn't solve unfortunately I tried, need to find out how try and excepts work
# -------------------------------------------------------------------------------------- #






