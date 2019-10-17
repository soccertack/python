print ('a')


def helper(l, s_list, tmp_list, idx):

    print (tmp_list)
    s_list.append(tmp_list[:])

    for i in range(idx, len(l)):
        tmp_list.append(i)
        helper(l, s_list, tmp_list, i+1)
        del tmp_list[-1]

def get_subset(l):

    subset_list = []

    helper(l, subset_list, [], 0)

    return subset_list

input = [1, 2, 3, 4]
subset = get_subset(input)
print (subset)
