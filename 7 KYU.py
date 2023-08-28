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