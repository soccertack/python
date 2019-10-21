import sys
def findUnsortedSubsarray(nums):
    # Let's return the last index

    pending = False
    last_idx = -1
    curr_max = nums[0]
    curr_min = sys.maxint
    for i in range(1, len(nums)):

        if nums[i] < curr_max:
            pending = True
            last_idx = 0
            curr_min = min (curr_min, nums[i])

        elif nums[i] == curr_max:
            if pending:
                last_idx = i - 1
                pending = False
        else:
            if pending:
                last_idx = i - 1
                pending = False
            curr_max = nums[i]
    if pending:
        print ("pending")
        last_idx = len(nums) - 1

    if last_idx == -1:
        print ("No sorting needed")
        return 0

    for j in range(len(nums)):
        if nums[j] > curr_min:
            first_idx = j
            break

    print (first_idx, last_idx)
    return last_idx - first_idx + 1



nums = [3, 2, 3, 2, 4]
nums = [1, 3, 2, 2, 2]
nums = [5, 4, 3, 2, 1]
nums = [1, 3, 5, 4, 2]
#nums = [1, 2, 3, 4, 5]
a = findUnsortedSubsarray(nums)
print (a)

