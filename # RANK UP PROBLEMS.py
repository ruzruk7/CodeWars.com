# RANK- up problems 


# PROBLEM 1
#5 KYU 
# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them 
# (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. 
# The last address will always be greater than the first one.

# Examples
# * With input "10.0.0.0", "10.0.0.50"  => return   50 
# * With input "10.0.0.0", "10.0.1.0"   => return  256 
# * With input "20.0.0.10", "20.0.1.0"  => return  246

# def ips_between(start, end):

#     return

# x = '10.0.0.0'
# list1 =  x.split('.') #[ip for ip in x]  #list(x)
# x2 = '10.0.1.0'
# list2 = x2.split('.')#[ip2 for ip2 in x2]
# diff_1 = ''
# diff_2 = ''
# total_amount_of_ip = 256
# for i1, i2 in zip(list1,list2):
#     if i1!= i2:
#         diff_2 = i2
#         diff_1 = i1
# index_diff = list2.index(diff_2)
# print(f'{i}'ndex_diff)
# if index_diff is 3:


# print(f'{f}''{list1}\n{list2}') # should return 256



#PROBLEM 2 
# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
#For example:

# * url = " -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

#my solutionn
def domain_name(url):
    prefix = ['https://www.', 'http://www.', 'http://', 'www.', 'https://']
    for pre in prefix:
        if pre in url:
            url = url.removeprefix(pre)
    period_index = []
    ind = list(url)
    for number, value in enumerate(ind):
        if value is '.':
            period_index.append(number)    
    string = url[:period_index[0]]
    return (string)

#best voted 
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


############################################################################################################
# NOTE REVIEW THIS 
# PROBLEM 2
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be intef'{g}'er division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

def integer(inte):
    '''returns given argument as an integer. since by default python takes 1,2,3...etc as an integer this function is simply returning 
    what is passed to it'''
    return int(inte)
def zero(func=integer):
    '''the func=integer is ma'''
    # func=integer(inte)->inte
    return func(0) 
def one(func=integer): #your code here
    return func(1)
def two(func=integer): #your code here
    return func(2)
def three(func=integer): #your code here
    return func(3)
def four(func=integer): #your code here
    return func(4)
def five(func=integer): #your code here
    return func(5)
def six(func=integer): #your code here
    return func(6)
def seven(func=integer): #your code here
    return func(7)
def eight(func=integer): #your code here
    return func(8)
def nine(func=integer): #your code here
    return func(9)



def plus(number): #your code here
    '''lambdas return '''
    return lambda num1: num1 + number
def minus(number): #your code here
    return lambda num1: num1 - number
def times(number): #your code here
    return lambda num1: num1 * number
def divided_by(number): #your code here
    return lambda num1: int(num1 / number)



##############################################################################

