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

def subset_dup(string, curr_string, res):

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


#https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
#Passping original string
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

res = []
string = 'abc'
subset_1(string, 0, '', res)
print (res)

res = []
string = 'abc'
subset_2(string, '', res)
print (res)

res = []
string = 'abc'
perm_1(string, '', res)
print (res)

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

