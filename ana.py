


# assumption: all lower case letters
def count(string):
    arr = [0] * 26
    for c in string:
        arr[ord(c)-ord('a')] += 1

    return str(arr)

def sort_ana(input, dict):
    for string in input:
        ret = count(string)
        if ret in dict:
            dict[ret].append(string)
        else:
            dict[ret] = [string]

    output = []
    for key in dict:
        for v in dict[key]:
            output.append(v)

    return output

input = ['abc', 'bed', 'cba', 'dfdf', 'ima', 'iam', 'bac', 'mai']
ret = sort_ana(input, {})
print (ret)
