
# Input: 1 ^ 0 | 0 | 1
# Desired output: 0
# return: 1 ^ ( ( 0 | 0 ) | 1 ), 1 ^ (0 | ( 1 | 0 ))

# Operators & | ^
# nums: 0 1
#


# 1 | 1: 1
# 1 | 1 | 1 : 2
# 1 | 1 | 1 | 1: 


#1 ((1 1) 1)
#(1 (1 1)) 1
#
#1 (1 (1 1))
#
#(1 1)(1 1)
#((1 1) 1) 1 
#
#
#2 parenthesis
#
#pick 2 adjacent
# 01 -> pick 2 out of three
# 12 ->
# 23 ->

def evaluate(string):

    if not string:
        print ("BUG")
        return ''

    num1 = int(string[0])
    num2 = int(string[2])
    oper = string[1]

    if oper == '|':
        ret = num1 | num2
    elif oper == '&':
        ret = num1 & num2
    elif oper == '^':
        ret = num1 ^ num2
    else:
        print ('invalid operator: ', oper)
        ret = -1
    return str(ret)

def func(string, res, curr_string, answer):

    if not string:
        # TODO
        return

    # this is when we are done
    if len(string) == 1:
        if string == answer:
            res.append(curr_string)
            print ("Yes", curr_string)
        else:
            print ("No")
        return

    for i in range(0, len(string) - 1, 2):
        print ('i : ', i, 'sring', string)
        ret = evaluate(string[i:i+3])
        print ('eval: ', ret)
        print ('curr_string size: ', len(curr_string))
        new_str = '(' + curr_string[i] + string[i+1] + curr_string[i+2] + ')'
        print (new_str)
        new_curr_string = curr_string [0:i] + [new_str] + curr_string [i+3:]
        func(string[0:i] + ret + string[i+3:], res, new_curr_string, answer)

string = '1^0|0|1'
res = []
answer = '0'
curr_string = []
for c in string:
    curr_string.append(c)

func(string, res, curr_string, answer)

print (res)



