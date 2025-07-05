# problem 1
'''def is_prime(n):
    div = n - 1
    while div > 1:
        if n % div == 0:
            return False
        div -= 1
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))
'''

# problem 2

# take a list, and reverse it using 2 pointers, not slicing
# creating a new empty list
# front and back pointer, end -> front || front > end, terminate once done, and append front
'''def reverse_list(lst):
    newList = []
    front = 0
    end = len(lst) - 1  # the last elem

    while end > front:
        newList.append(lst[end])         # adds the last elem
        # [5]
        end -= 1
    newList.append(lst[front])
    return newList

lst = [1,2,3,4,5]
print(reverse_list(lst))'''

# problem 4
# to output a list that has all even numbers in the front, followed by odd numbers
# go through each element in the first (for loop), check if odd or even. 
# if even, append to new list, remove it from the list, if odd, skip.
# all odd numbers will remain. append the entire remaining list in nums
# output new list
'''def sort_array_by_parity(nums):
    newList = []
    for i in nums:
        if (i % 2 == 0):     # is even
            newList.append(i)
            # del nums[i]
    for i in nums:      # is odd
        if (i%2 == 1):
            newList.append(i)

    return newList


nums = [3,1,2,4]
print(sort_array_by_parity(nums))'''


'''def find_pair_sum(s, target):
    # use front and back pointers
    # while front < back
    # add up front and back pointers, check if == target
    # front += 1
    # back -= 1
    # make it move one at a time
    
    digits = [int(elem)for elem in s] # converts it to an int
    front = 0
    back = front + 1
    sum = 0
    
    while front < len(s) and back < len(s):
        sum = digits[front] + digits[back]
        if sum == target:
            return True
        front += 1
        back +=1
            
    return False

s = "12345"
target = 5
print(find_pair_sum(s, target))'''

'''def find_min_sublist_sum(nums, k):
    # Write your code here
    # sort nums into groups of k (use windows)
    # add sum of those sublists, and append to an empty list
    # sort empty list
    # return list[0]
    if k > len(nums) or k < 0:
        return 0
    newList = []
    compare = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        newList.append(window)
        print(window)
    for j in newList:
        compare.append(sum(j))
        print(sum(j))
    compare.sort()
        
    return compare[0]


nums = [4, 2, -5, 1, -3]
k = 5

print(find_min_sublist_sum(nums, k))'''

# problem 6
# output the og list, with only 

def remove_duplicates(nums):