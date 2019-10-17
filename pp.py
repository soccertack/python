
def put_p(res, curr, dict, char):
   print ('put_p', hex(id(curr)))
   dict_copy = dict.copy()
   dict_copy[char] -= 1
   if not dict_copy[char]:
       del dict_copy[char]
   print ('calling pp_helper', 'curr', curr, hex(id(curr)))
   curr += char
   print ('afer adding a char', 'curr', curr, hex(id(curr)))
   pp_helper(res, curr, dict_copy)
   #del curr[-1]
   # This is creating a copy of curr. The original curr is not accessable now
   curr = curr[:-1]
   print ('after pp_helper', 'curr', curr, hex(id(curr)))

def pp_helper(res, curr, dict):
    print ('pp_helper', hex(id(curr)))
    if not dict:
        print ('adding', curr)
        res.append(curr[:])
        return

    if ('(' not in dict) or (dict['('] < dict[')']):
        #we can put ')'
        print ("putting \)")
        curr_1 = curr[:]
        put_p(res, curr, dict, ')')
        curr_2 = curr[:]
        if curr_1 != curr_2:
            print ("ERROR", curr_1, curr_2)


    if '(' in dict:
        #we can put '('
        print ("putting \(")
        put_p(res, curr, dict, '(')

def pp(n):
    if not n:
        return []

    dict = {}
    dict['('] = n
    dict[')'] = n
    res = []
    pp_helper(res, '', dict)
    # This will give an error since array will be reassigned.
    # String is kind of passed by value, so it should be fine
    # Comment out del... above to make it work
    #pp_helper(res, [], dict)
    return res

ret = pp(1)
print (ret)

