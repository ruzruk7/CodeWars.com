# PYTHON FUNDAMENTLS

################################################# 8 KYU ##########################################################
# Problem 1
# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.
def positive_sum(arr):
    return sum([x for x in arr if x >= 0])


# Problem 2
# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"
def rps(p1, p2):
    # This  method defines each victory as a key  verses its value as its opponent.
    # This dict could also be made as a defeat key, value pair.
    # The conditions simply test which key, value pair is present as arguments.
    beat = {'rock': 'scissors', 'scissors': 'paper', 'paper':'rock'}
    if beat[p1] == p2:
        return ('Player 1 won!')
    elif beat[p2] == p1:
        return ('Player 2 won!')
    else:
        return ('Draw!')
    

#     if p1 == 'rock' and p2 == 'scissors':
#         return ('Player 1 won!')
#     elif p1 == 'scissors' and p2 == 'rock':
#         return ('Player 2 won!')
#     elif p1 == 'scissors' and p2 == 'paper':
#         return ('Player 1 won!')
#     elif p1 == 'paper' and p2 == 'scissors':
#         return ('Player 2 won!')
#     elif p1 == 'rock' and p2 == 'paper':
#         return ('Player 2 won!')
#     elif p1 == 'paper' and p2 == 'rock':
#         return ('Player 1 won!')
#     else:
#         return ('Draw!')



#Problem 3 
# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.
def sum_mix(arr):
    return sum([int(i) for i in arr])


#Problem 4
# DESCRIPTION:
# After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

# Write a code that gives out the total amount for different days(d).
def rental_car_cost(d):
    x = 40 * d
    if d >= 7:
        x -= 50
    elif d >= 3 and d <= 7:
        x -= 20 
    return x


#Problem 5
# DESCRIPTION:
# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

# Return true if yes, false otherwise :)
def hero(bullets, dragons):
    return (True if 2*dragons <= bullets else False)

#Problem 6
# DESCRIPTION:
# Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

# For example (Input -> Output):

# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
def summation(num):
    su = 0
    for n in range(num+1):
        su += n
    return (su)

#Problem 7
# DESCRIPTION:
# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]
def digitize(n):
    z = list(str(n))
    z.reverse()
    zlis = []
    for i in z:
        zlis.append(int(i))
    return (zlis)


#Problem 8

# DESCRIPTION:
# Implement a function which convert the given boolean value into its string representation.

# Note: Only valid inputs will be given.
def boolean_to_string(b):
    return str(b)

#Problem 9

# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
def simple_multiplication(number) :
#     if number % 2 == 0:
#         return (number * 8)
#     else:
#         return (number * 9)
    return number*8 if number % 2 == 0 else number*9


#Problem 10

# DESCRIPTION:
# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]
def maps(a):
    return [x*2 for x in a]

#Problem 11
# DESCRIPTION:
# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

# Examples(Operator, value1, value2) --> output
# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7

def basic_op(operator, value1, value2):
    # if operator == '+':
    #     total = value1 + value2
    # if operator == '-':
    #     total = value1 - value2
    # if operator == '*':
    #     total = value1 * value2
    # if operator == '/':
    #     total = value1 / value2
    # return print(total)
    
    # can use
    return eval(f'{value1}{operator}{value2}')


#Problem 12 
# DESCRIPTION:
# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2

# Input: []
# Output: 0

# Input: [-2.398]
# Output: -2.398

# Assumptions
# You can assume that you are only given numbers.
# You cannot assume the size of the array.
# You can assume that you do get an array and if the array is empty, return 0.
# What We're Testing
# We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
# Advanced users may find this extremely easy and can easily write this in one line.
def sum_array(a):
    return sum(a)



#Problem 13

# DESCRIPTION:
# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

# Considering these factors, write a function that tells you if it is possible to get to the pump or not.

# Function should return true if it is possible and false if not.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    can = (fuel_left * mpg)/ distance_to_pump
    if can >= 1:
        return True
    if can < 1:
        return False
    
#Problem 14

# Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

# For example:

# time = 3 ----> litres = 1

# time = 6.7---> litres = 3

# time = 11.8--> litres = 5
import math
def litres(time):
    return math.floor(time * 0.5)

#Problem 15 
# DESCRIPTION:
# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'
def solution(string):
    lis = [*string]
    lis.reverse()
    return ''.join(lis)

# Problem 16 
# DESCRIPTION:
# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
def lovefunc( flower1, flower2 ):
    if (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0):
        return True
    elif (flower1 % 2 == 0 and flower2 % 2 == 0) or (flower1 % 2 != 0 and flower2 % 2 != 0):
        return False
    

# PROBLEM 17
# Write a function named setAlarm/set_alarm/set-alarm/setalarm (depending on language) which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.

# The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

# employed | vacation 
# true     | true     => false
# true     | false    => true
# false    | true     => false
# false    | false    => false

def set_alarm(employed, vacation):
    return (True if employed == True and vacation == False else False)
        



##################################### 8 KYU ######################################################
 

################################### 7 KYU ###############################################################         

# 7 KYU

# Problem 1 
# DESCRIPTION:
# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.
def find_short(s):
    sentences = s.split()
    length = len(sentences[0])
    for word in sentences:
        if len(word) < length:
            length = len(word)
    return (length)


def find_short(s):
    s = s.split() # splits the string into a list of individual words
    l = min(s, key = len) # finds the shortest string in the list
    return len(l) # returns shortest word length

def find_short(s):
    return min(len(x) for x in s.split())


# Problem 2
# DESCRIPTION:
# In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants

# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213

# It will need 3 entire years.
# More generally given parameters:

# p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)

# the function nb_year should return n number of entire years needed to get a population greater or equal to p.

# aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)

# Examples:
# nb_year(1500, 5, 100, 5000) -> 15
# nb_year(1500000, 2.5, 10000, 2000000) -> 10
# Note:
# Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02.
def nb_year(p0, percent, aug, p):
    year_count = 0
    while p0 < p:
        year_count += 1
        percent_gain_per_year = int(p0 * (percent/100))
        p0 += (percent_gain_per_year + aug)
        print(year_count)
    
    return(year_count)


# Problem 3
# DESCRIPTION:
# Task:
# Given a list of integers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

# Examples:
# Input: [0]
# Output: "even"

# Input: [0, 1, 4]
# Output: "odd"

# Input: [0, -1, -5]
# Output: "even"
def odd_or_even(arr):
    x = sum(arr)
    if x % 2 == 0:
        return('even')
    elif x % 2 !=0:
        return('odd')
    
# Problem 4 
# DESCRIPTION:
# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))

# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
def add_binary(a,b):
    return (bin(a+b).removeprefix('0b'))

# Problem 5 
# DESCRIPTION:
# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

def high_and_low(numbers):
    numbers = numbers.split()
    return (f'{max(numbers, key=int)} {min(numbers, key=int)}')

# PROBLEM 6
# DESCRIPTION:
# Task:
# Your task is to write a function which returns the sum of following series upto nth term(parameter).

# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
# Rules:
# You need to round the answer to 2 decimal places and return it as String.

# If the given value is 0 then it should return 0.00

# You will only be given Natural Numbers as arguments.

# Examples:(Input --> Output)
# 1 --> 1 --> "1.00"
# 2 --> 1 + 1/4 --> "1.25"
# 5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
def series_sum(n):
    num_list = []
    if n == 0:
        return (f'{n:.2f}')
    elif n == 1 :
        return (f'{n:.2f}')
    else:
        denom = 4
        num_list.append(1)
        for i in range(1, n):
            value = (1/denom)
            num_list.append(value)
            denom += 3
        return (f'{round(sum(num_list), 2):.2f}')
    
def series_sum(n):
    sum = 0.0
    for i in range(0,n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum

# PROBLEM 7
# DESCRIPTION:
# The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

# Input
# Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

# Output
# Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

# Example
# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
def open_or_senior(data):
    for pair in data:
        if pair[0] >= 55 and pair[1] > 7:
            ind = data.index(pair)
            data[ind] = "Senior"
        elif pair[0] < 55 or pair[1] <= 7:
            ind = data.index(pair)
            data[ind] = "Open"
    return data

def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

# PROBLEM 8
# DESCRIPTION:
# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
def filter_list(l):
    'return a new list with the strings filtered out'
    return ([x for x in l if type(x) == int])


#PROBLEM 
#8kyu
def remove_exclamation_marks(s):
    # s = 'hi! hello!'
    # ss = s.replace('!','')
    return print(s.replace('!',''))

#PROBLEM 
# 8 kyu
# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

# For example, when the input is green, output should be yellow.
def update_light(current):
    signal = ['red', 'green', 'yellow']
    current_signal = signal.index(current)
    if current_signal == 2:
        current_signal = -1
    return (signal[(current_signal+1)])

# good alternative 
def update_light(current):
    '''this works by settings the next light in a signal as the VALUE of the current light which is the KEY'''
    signals ={"green": "yellow", "yellow": "red", "red": "green"}
    return signals[current]


#PROBLEM
# 6 KYU
# Your task is to construct a building which will be a pile of n cubes.
#  The cube at the bottom will have a volume of �3n3, the cube above will have volume of (�−1)3(n−1)3 and so on until the top which will have a volume of 1313.
# You are given the total volume m of the building.
#  Being given m can you find the number n of cubes you will have to build?
# The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an integer m and you have to return the integer n such as �3+(�−1)3+(�−2)3+...+13=�n3+(n−1)3+(n−2)3+...+13=m if such a n exists or -1 if there is no such n.
# Examples:
# find_nb(1071225) --> 45
# find_nb(91716553919377) --> -1
def find_nb(m):
    '''we move the equation accross the = sign making it (n + 1)^3.
      when we keep adding 1 to n eventually n will equal m if this never occurs then we return -1.
      
      '''
    top = 1
    n = 0 
    while n <= m:
        n  += top**3
        if n == m: # this is needed to stop top being updated even after n > m. so we return top before we add 1 to top
            return (top)
        top += 1
    else:
        return (-1)
    

# PROBLEM
# 7 KYU
# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.
def accum(s):
    s_list = list(s)
    string = ''
    for number, value in enumerate(s_list):
        for i in range(number+1):
            string += value
        if number >= (len(s_list)-1):
            # return print(string)
            break
        string += '-'
    s_list = string.split('-')
    print(s_list)
    formatted = []
    for value in s_list:
        cap_first_let = value.title()
        formatted.append(cap_first_let)
    return print('-'.join(formatted))
    
            

accum("abcd") # "A-Bb-Ccc-Dddd"