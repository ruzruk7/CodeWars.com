# Scrap file

def unique_in_order(sequence):
    lis = []
    temp = ""
    for x in sequence:
        if x != temp:
           lis.append(x.upper()) 
        temp = x 
    print(lis)
unique_in_order('AAAABBBCCDAABBB')# == ['A', 'B', 'C', 'D', 'A', 'B']