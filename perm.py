import math

def perm (string, curr_string, res):
    if not string:
        res.append(curr_string)

    for i in range(len(string)):
        new_string = curr_string + string[i]
        perm(string[:i] + string [i+1:], new_string, res)

def subset(string, curr_string, res):
    if not string:
        res.append(curr_string)
        return

    subset(string [1:], curr_string, res)
    subset(string [1:], curr_string + string[0], res)

def subset_dup_old(string, curr_string, res):

    if not string:
        res.append(curr_string)
        return

    i = 0
    while i < len(string) and string[i] == string[0]:
        i += 1

    for j in range(i):
        print (string[0:j+1])
        subset(string [i:], curr_string + string[0:j+1], res)

    subset(string [i:], curr_string, res)

#Passing original string + idx
def subset_1(string, idx, curr_string, res):
    res.append(curr_string[:])
    for i in range(idx, len(string)):
        curr_string += string[i]
        subset_1(string, i+1, curr_string, res)
        curr_string = curr_string[:-1]

#Passing modified string
def subset_2(string, curr_string, res):
    res.append(curr_string[:])
    for i in range(len(string)):
        curr_string += string[i]
        subset_2(string[i+1:],  curr_string, res)
        curr_string = curr_string[:-1]

def subset_dup(string, curr_string, res):
    res.append(curr_string[:])
    for i in range(len(string)):
        # do something here #
        if i and string[i] == string[i-1]:
            continue

        curr_string += string[i]
        subset_dup(string[i+1:],  curr_string, res)
        curr_string = curr_string[:-1]

#https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
#Passping original string
# This definitely does't work for duplicated strings at all
def perm_1(string, curr_string, res):
    if len(curr_string) == len(string):
        res.append(curr_string)
        return

    for i in range(len(string)):
        if string[i] in curr_string:
            continue
        curr_string += string[i]
        perm_1(string, curr_string, res)
        curr_string = curr_string[:-1]

# This gives duplicated answers for duplicated strings
def perm_2(string, curr_string, res):
    if not string:
        res.append(curr_string[:])
        return

    for i in range(len(string)):
        curr_string += string[i]
        perm_2(string[0:i] + string[i+1:], curr_string, res)
        curr_string = curr_string[:-1]

def perm_dup(string, curr_string, res):
    if not string:
        res.append(curr_string[:])
        return

    for i in range(len(string)):
        if (i != 0) and (string[i] == string[i-1]):
            continue
        curr_string += string[i]
        perm_dup(string[0:i] + string[i+1:], curr_string, res)
        curr_string = curr_string[:-1]

def check_duplicated(res):
    dict = {}
    found = False
    for item in res:
        if item in dict:
            print ('duplicated item', item)
            found = True
            break
        dict[item] = 1
    if not found:
        print ('Great! Returned set doesn\'t have any duplicated items')

string = 'abbccc'
res = []
subset_1(string, 0, '', res)
#print (res)

res = []
subset_2(string, '', res)
#print (res)

res = []
subset_dup(string, '', res)
print (res)
check_duplicated(res)

res = []
perm_1(string, '', res)
#print (res)

res = []
perm_2(string, '', res)
#print (res)

res = []
sorted_string = ''.join(sorted(string))
perm_dup(sorted_string, '', res)
#print (res)
#check_duplicated(res)

#res = []
#string='abcef'
#perm(string, '', res)
#print (res)
#print (len(res))
#print (math.factorial(len(string)))
#
#res = []
#subset(string, '', res)
#print (res)
#print ('real len', len(res))
#print ('math len', 2 ** len(string))
#
#
#string= 'abab'
##join: '123'.join('abc') : a 123 b 123 c (without spaces)
#
#string = ''.join(sorted(string))
#res = []
#subset_dup(string, '', res)
#print (res)
#print ('real len', len(res))
#print ('math len', 2 ** len(string))

