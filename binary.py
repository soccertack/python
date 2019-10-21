

# This is a simple binary search
def bsearch(input, start, end, target):

    if start > end:
        return -1

    if start == end:
        if input[start] == target:
            return start
        else:
            return -1

    m = (start + end) / 2

    if input[m] > target:
        idx = bsearch(input, start, m - 1, target)
    elif input [m] < target:
        idx = bsearch(input, m + 1, end, target)
    else:
        idx = m

    return idx

def find_rotation(input, start, end):

    if start > end:
        print (start, end)
        return -1

    if start + 1 == end:
        if input[start] > input[end]:
            return end;
        else:
            print ("BUGBUG")

    m = (start + end) / 2

    if input[start] > input[m]:
        idx = find_rotation(input, start, m)
    elif input[m] > input[end]:
        idx = find_rotation(input, m, end)
    else:
        print ("BUG")

    return idx


input = [1, 3, 5, 7, 9]
target = 2

ret = bsearch(input, 0, len(input), target)
print (ret)

input = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
target = 5
offset = find_rotation(input, 0, len(input))
print (offset)
new_input = input[offset:len(input)] + input[:offset]
ret = bsearch(new_input, 0, len(new_input), target)
print ("target", target, "is at", ret + offset)


