'''def is_subsequence(lst, sequence):
    result = True

    newLst = []
    if(len(lst) == 0 or len(sequence)) > len(lst):
        result = False
    index = 0
    for i in j: # use a nested loop
        if lst[j] == sequence[i]:
            newLst.append()
            index += 1
    return result

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))'''

'''def group_anagrams(words)           # check if lengths are equal, check if the frequency of the 
    sort(words)'''                     # letters are the same || sort to get the letters in order

# problem 1
''' def is_subsequence(lst, sequence):
    idx = 0
    for n in lst:
        if sequence[idx] == n:
            idx +=1
        if idx == len(sequence):
            return True
    return False

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, 8, 10]
print(is_subsequence(lst, sequence)) '''

''' def create_dictionary(keys, values):
    newDict = {}        # 
    for i in values:
        keys[]

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"] ''' 

###################################### SESSION 2B ######################################

# problem 1
''' def cast_vote(votes, candidate):
    if candidate in votes:      # check if the candidate exists
        votes[candidate] += 1   # increment
    else:                       # if candidate !exist
        votes[candidate] = 1    # they begin at one
    return votes

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes) '''

# problem 2
''' def common_keys(dict1, dict2):
	same = []           # create an array NOT a dict
	for key in dict1:
		if key in dict2:
			same.append(key)
	return same

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list) '''

# problem 3
