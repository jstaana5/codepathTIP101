# problem 1

''' def print_list(lst):
    for i in lst:
        print(i)

lst = ["squirtle", "gengar", "charizard", "pikachu"]

print_list(lst) '''

# problem 2
''' def doubled(lst):
    for i in lst:
        print(i*2)
lst = [1,2,3]
doubled(lst) '''

# problem 3
''' def doubled(lst):
    new_lst = lst.copy()    # creates a copy
    for i in lst:   
        new_lst.append(i*2)
    return new_lst
    
lst = [1,2,3]
x = doubled(lst)
print(x) '''

# instructor demo that takes a list of ints and creates a new list that returns 
# numbers greater than the threshold

def above_threshold(lst, threshold):
    new_lst = []     # creates an empty list
    for i in lst:       # iterates through the og list
        if(i > threshold):     # if greater than threshold
            new_lst.append(i)      # adds to the new list
    return new_lst

lst = [8, 2, 13, 11, 4, 10, 14]

print(above_threshold(lst, 10))


# problem 5
''' def max_difference(lst):
    lst.sort()
    last = lst[-1]
    first = lst[0]
    return last-first

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff) '''


#problem 6
'''def count_less_than(numbers, threshold):
    index = 0
    for i in numbers:
        if i < threshold:
            index+=1
    return index

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)'''

# problem 7  
'''def get_evens(lst):
    x = []
    for i in lst:
        if(i%2 == 0):      # checks if even
            x.append(i)
    return x

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)'''

# problem 8
'''def multiples_of_five():
    for i in range(5, 101, 5):
        print(i)

multiples_of_five()
'''


# problem 9
'''def find_divisors(n):
    b = []
    for i in range(1, n+1):
        if(n % i == 0):      # divisible
            b.append(i)
    return b

lst = find_divisors(6)
print(lst)'''