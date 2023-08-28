# 8 KYU


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

