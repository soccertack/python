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

res = []
string='abcef'
perm(string, '', res)
print (res)
print (len(res))
print (math.factorial(len(string)))

res = []
subset(string, '', res)
print (res)
print ('real len', len(res))
print ('math len', 2 ** len(string))


string= 'abab'
#join: '123'.join('abc') : a 123 b 123 c (without spaces)

string = ''.join(sorted(string))
res = []
subset_dup(string, '', res)
print (res)
print ('real len', len(res))
print ('math len', 2 ** len(string))

