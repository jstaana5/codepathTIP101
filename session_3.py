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
        
    alphabet = ['a', 'b','c','d', 'e', 'f', 'g', 'h', 'i','j','k','l','m','n','o','p','q', 'r','s', 't', 'u',
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

'''def first_unique_char(my_str):
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
first_unique_char("aabb")'''


#######################

'''def reverse_words(s):
    #remove whitespaces
    s = s.split()

# we want to get each word, which can be detected by the space
# then create a new string that prints the words backwards
    return " ".join(s[::-1])       # reverses the list

    # s.reverse() will also reverse the words in the list 

s = "  the sky is blue     "
print(reverse_words(s))

set(my_str) # strips every letter and disregards duplicates'''


# problem 1
'''def sum_of_number_strings(nums):
    # turn strings into integers, 
    newList = []
    result = 0
    for i in nums:
        i = int(i)
        newList.append(i)
        # print(newList) # new list of all ints [10,20,30]
    # add all vals in list
    for i in range(len(newList)):
        # get current num, add it to total result, move on
        result += newList[i]
    return result
        


nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)'''

# problem 2
'''def remove_duplicates(nums):
    # use a frequency dictionary, add new vals that have no freq to the new list, if it already exists, just skip
    frequency_map = {}
    newList = []
    for item in nums:
        if item in frequency_map:
            frequency_map[item] += 1
        else:
            frequency_map[item] = 1
            newList.append(item)

    return newList

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))
# no_dups = [1,2,3,4,5,6]'''

# problem 3
'''def reverse_only_letters(s):
    # go through each char, if isalpha(), add to a list until a new str is created where its just letters
    # reverse that new str
    # get positions of the non alphabetic chars, print out letters backwards with alphabet
    # go through the str, if char isalpha, add to newstr and take note of its position (use enumerate)
    str = ""
    for char in s:
        if char.isalpha():
            str += char
    str = str[::-1]     #string has been reversed

    result = []
    index = 0
    for i in s:
        if i.isalpha():
            result.append(str[index])
            index +=1
        else:
            result.append(i)

    return "".join(result)




s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)'''


'''word = "encourage"
char_count = {}

for char in word:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1

char_count['e'] +=2
print(char_count['e'])'''


# problem 4
'''def longest_uniform_substring(s):
    # go through the list, frequency table? whatever is highest, return that value
    frequency_map = {}
    for letter in s:
        if letter in frequency_map:
            frequency_map[letter] +=1
        else:
            frequency_map[letter] = 1
    for i in frequency_map:
        return max(frequency_map.values())



s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)'''

