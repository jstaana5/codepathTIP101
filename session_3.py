#problem 1

'''def count_mississippi(limit):
    for num in range(1, limit):
	    print( f"{num} mississippi")
                
count_mississippi(6)

# problem 2
def swap_ends(my_str):
    newStr = my_str
    # get the first letter, get middle letters, get the last letter, and add them
    return my_str[-1] + my_str[1:-1] + my_str[0]

my_str = "boat"
print(swap_ends(my_str))
'''
#problem 3
'''def is_pangram(my_str):
    alphabet = ['a', 'b,','c','d', 'e', 'f', 'g', 'h', 'i','j','k','l','m','n','o','p','q', 'r','s', 't', 'u'
    'v', 'w', 'x', 'y', 'z']
    my_str.lower()
    while i<my_str.len():
        if my_str[i] not in alphabet:
            return False
        else:
            return True
        
    alphabet = ['a', 'b,','c','d', 'e', 'f', 'g', 'h', 'i','j','k','l','m','n','o','p','q', 'r','s', 't', 'u'
    'v', 'w', 'x', 'y', 'z']
    
    for i in alphabet:
        if i not in my_str.lower():
            return False
        else:
            return True'''
        
'''my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))'''
    
# if length < 26, return false
# split, check if each letter is in the list of letters

def first_unique_char(my_str):
    frequency_map = {}
    for item in my_str:
        if item in frequency_map:
            frequency_map[item] += 1
        else:
            frequency_map[item] = 1
    # print(frequency_map)

    # check out the first char in the freq map that has the value of one

    for i in frequency_map:
        if frequency_map[i] == 1: # find out that letter
            # find that letter index in my_str
            print(my_str.index(i))
            break
    else:
        print("Not found.")

first_unique_char("bananabs")
first_unique_char("leetcode")
first_unique_char("loveleetcode")
first_unique_char("aabb")


