# RANK- up problems 


# problem 
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
# print(index_diff)
# if index_diff == 3:


# print(f'{list1}\n{list2}') # should return 256



#PROBLEM 2 
# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
#For example:

# * url = " -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

#my solution
def domain_name(url):
    prefix = ['https://www.', 'http://www.', 'http://', 'www.', 'https://']
    for pre in prefix:
        if pre in url:
            url = url.removeprefix(pre)
    period_index = []
    ind = list(url)
    for number, value in enumerate(ind):
        if value == '.':
            period_index.append(number)    
    string = url[:period_index[0]]
    return (string)

#best voted 
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]