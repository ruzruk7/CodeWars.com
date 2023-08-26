#CodeWars
#question :
import functools
def square_sum(numbers):
    return print(functools.reduce(lambda x, y : x + y, [x**2 for x in numbers]))
square_sum([])
# you could use sum(iterable):   sum([x**2 for x in numbers])

# quesion list comprehension
def open_or_senior(data):
    #data(age, handicap level)
    # for pair in data:
        # if pair[0] >= 55 and pair[1] > 7:
        #     # pair.replace(str(pair), 'Senior')
        #     ind = data.index(pair)
        #     data[ind] = "Senior"
        # elif pair[0] < 55 or pair[1] <= 7:
        #     ind = data.index(pair)
        #     data[ind] = "Open"

    # can do this 
    dataa = ['Senior' if age >= 55 and handicap_level > 7 else 'Open' for age, handicap_level in data]
    return print(dataa)



def simple_multiplication(number) :
    # if number % 2 == 0:
    #     return (number * 8)
    # else:
    #     return (number * 9)
    return number*8 if number % 2 == 0 else number*9


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
series_sum(3)



# DICTIONARY 
def rps(p1, p2):
    #rps is the rock paper scissors game 

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