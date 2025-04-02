# Fus!

# def sum_cubes(n):
#     sum, x = 0, 1
#     while x<= n:
#         sum, x = sum + x**3, x+1
#     return sum
# sum = sum_cubes(2)
# print(sum)

def pressure(v, t, n=6.022e23):
    """Compute the pressure in pascals of an ideal gas.
    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particles of gas (default: one mole)
    """
    k = 1.38e-23 # Boltzmann's constant
    return n * k * t / v
result = pressure(v, t, n)


# def pair(x, y):
#     '''Returns a fus that represents a pair'''
#     def get(index):
#         if index ==0:
#             return x
#         elif index== 1:
#             return y
#     return get

# def select(p, i):
#     return p(i)  

# p = pair(3, 4)
# s= select(p, 1)
# print(s)

# LIST

# pair = [6, 9]
# print(pair.__getitem__(0))

digits = [1, 8, 2, 8]
# print(digits.count(2))
# print(len(digits))
# length = digits.__len__()
# print(length)
digits = digits*2 + [-1, 0, 4, 9]
# print(digits)
# digits = [digit**2 for digit in digits if digit < 0]
# del digits[0]
# digits.clear()
print(digits.pop())
# print(digits)
# print(8 in digits)

pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
# print(pairs[0][1])
# same_count = 0
# for x, y in pairs:
#     if x== y:
#         same_count += 1
# print(same_count)

# nums_less_than_eleven = list(range(1,11))
# print(nums_less_than_eleven)
# whole_nums_less_than_twenty = [_ for _ in range(21)]
# print(whole_nums_less_than_twenty)

# STRINGS

city = 'Berkeley '
# print(len(city))
# print(city[1])
# city = city + 'CA '
# city = city*2
# print(city)
# print('Carol' in 'South Carolina')
# print(type(city))
# string = 'The Zen of Python\nclaims, "Readability counts."\nRead more: import this.'
# print(string)
# print(str(2) + ' is an element of ' + str(digits))

# INTEGERS

x = 7
# print(type(x))
# floordiv = x // 2
# print(floordiv)
# print(type(floordiv))
# div = x/2
# print(div)
# div = int(div)
# print(div)
# print(type(div))
# print(div)
# div = bool(x)
# print(type(div))
# x = str(x)
# print(type(x))

# BOOL

# x = True
# y = False
# print(x)
# print(y)
# print(type(x))
# print(type(y))
# v = str(x)
# print(v)
# print(type(v))
# w = int(x)
# print(w)
# z = int(y)
# print(z)

#TUPLES
numbers = [x for x in range(-6, 10)]
my_numbers = tuple(numbers)
# print(my_numbers)
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.sort()
# numbers.reverse()
# print(numbers)

# schools = ('ASU', 'UCLA', 'MIT', 'CALTECH', 'ASU')
# # print(dir(schools)) 
# # print(schools.__len__())
# print(schools.index('MIT'))
# print(schools.count('ASU'))

# code = ("up", "up", "down", "down") + ("left", "right") * 2
# print(len(code))
# code[3]
# print(code.count("down"))




# SETS

vowels = {'a', 'e', 'i', 'o', 'u', 'e', 'i'}
first_5_letters = {'a', 'b', 'c', 'd', 'e'}
# print(dir(vowels))
# print(vowels.__len__())
# print(vowels.intersection(first_5_letters))
# print(vowels.union(first_5_letters))
# (first_5_letters.add(1))
# (first_5_letters.update(vowels))
# print(first_5_letters)
# print(vowels)


# DICTIONARIES


# numerals = {'I': 1.0, 'V': 5, 'X': 10}
# print(numerals['X'])
# numerals['L'] = 50
# print(numerals['L']) = 50
# numerals['I'] = 1
# print(numerals['I'])
# print(numerals)

no = dict([(3, 9), (4, 16), (5, 25)])
# print(no)
# no_set = set(no)
# print(type(no_set))

# squares = {x: x*x for x in range(1,11)}
# print(squares)
# print(type(squares))

capitals = {'USA' : 'DC',
            'Zim' : 'Harare',
            'SA' : 'Pretoria',
            'Nigeria' : 'Lagos'
            }

# capitals['Zim'] = 'Mt Hmpden'
# capitals.update({'Zim' : 'Hre', 'Botswana' : 'Gaborone'})
# print(capitals['Zim'])

# print(capitals.get('Zim'))
#print(capitals.__getitem__('Zim'))
# print(capitals.pop('Zim'))
# capitals.popitem()
# print(capitals)

#LOOPS

# n = int(input("Pick any number? "))

# while n != 1: 
#     if n % 2 == 0:
#         n = int(n//2)
#         print(n)
#     else:
#         n = int(n*3 + 1)
#         print(n)
        

# while x > 1:
#     if x > 1:
#         x -= 1
#         print(x)

# n = int(input('Guess a number? '))
# while not n == 7:
#    print('You failed')
#    n = int(input('Guess a number, again? '))
# print('You got it correct')

# while n!= 7:
#     if n < 7:
#         print('Your number is less than the expected number')
#         n = int(input(f'Guess another value greater than {n}: '))  
#     else:
#         print('Your number is greater than the expected number')
#         n = int(input(f'Guess another value less than {n}: '))  
# print('You won')

# import math


#  b = int(input("what is adjacent"))
#  a = float(input("what is opposite"))
#  hypotenuse = math.sqrt((b**2) + (a**2))

#  print(f"The length of the hypotenuse is: {hypotenuse}cm^2")
#  print(f"The length of the hypotenuse is: {round(hypotenuse, 3)}cm^2")
#  print(f"The length of the hypotenuse is: {float(hypotenuse)}cm^2")
#  print(f"The length of thhypotenuse is: {float(int(hypotenuse))}cm^2")

# k = 10
# while k > 0:
#     print(k)
#     k-=1

# count = 0
# while count < 5
#     if count == 3:
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1

# for i in range(1, 11):
#     print(11 - i)

# for i in range(0, 21):
    
#     if i%2 == 0 and i > 0:
#         print(i)

# for i in range(1, 50):
#     if i%5 ==0:
#         continue
#     print(i)

#Cond'l

# a = 0
# if a > 0:
#     print('A is a positive number')
# elif a < 0:
#     print('A is a negative number')
# else:
#     print('A is zero')

# a = 0
# if a > 0 and a % 2 == 0:
#         print('A is an even and positive integer')
# elif a > 0 and a % 2 !=  0:
#      print('A is a positive integer')
# elif a == 0:
#     print('A is zero')
# else:
#     print('A is negative')




# ui = int(input("what did you get on the  ui mock exam "))
# qual_research = int(input("what did you get on qualitative research mock exam "))
# quan_research  = int(input("what did you get on quantitative research mock exam "))

# design_pass_mark = mean
# (ui, qual_research, quan_research)

# if design_pass_mark < 300:
#     print("You do not qualify for Design class")
# elif design_pass_mark == 300:
#     print("You might qualify if and only if the pass students are less than 10")
# else:
#     print("Congratulations!!! You qualify for design, please respond to the offer")


# score = int(input("Enter a student's grade? "))

# if score >= 90 and score <=/100:
#     print('A')
# elif score >=80 and score <90:
#     print('B')
# elif score >=70 and score <80:
#     print('C')
# elif score >=60 and score <70:
#     print('D')
# else:
#     print('F')

# temp = int(input('What is the tmperature right now? '))
# weather = input('Is it sunny or cloudy? ')

# if temp > 30 and weather == 'sunny':
#     print(f'the temp is {temp} and the weather is {weather}')
# else: 
#     print('it is cold')

# Username = input('Enter your username? ')
# Password = int(input('Enter your password '))

# if (Username == 'admin' and Password == 1234):
#     print(f'Welcome {Username}, you are logged in')
# else:
#     print('Invalid credentials')

# n = int(input("Pick any number? "))

# if n % 2 == 0:
#     n = int(n//2)
#     print(n)
# else:
#     n = int(n*3 + 1)
#     print(n)

#FILE

file = open('kudzifiles.txt', 'r')
content = file.read
print(content)
file.close()
with open('kudzifiles.txt', 'r') as file:
    content = file.read()
    print(content)
with open('kudzifiles.txt', 'a') as file:
    file.write('\nWena')
import os
if os.path.exists('Mathematics teacher recomendation.pdf'):
    print("File exist")
else:
    print('No file like that')
os.mkdir('IVY LEAGUE')
os.rmdir('IVY LEAGUE')