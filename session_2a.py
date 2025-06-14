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

def create_dictionary(keys, values):
    newDict = {}        # 
    for i in values:
        keys[]

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
