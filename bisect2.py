import bisect
import random
def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo

# [0, 0, 1, 3, 3, 3, 4, 5, 5, 5]
# with lo = 0, hi = len(nums)-1, target = 5
# lo = 0, hi = 9 mid = 4
# lo = 5, hi = 9 mid = 7
# lo = 8, hi = 9 mid = 8 found = 8
# lo = 9, hi = 9, terminate without eval 9th

# [1, 3]
# lo 0, hi 1, target 1
# lo = 0, hi = 1, mid 0
# lo = 1, hi = 1, break if lo<hi.

# inf with lo <= hi, lo = mid +1, hi = mid
# [0, 0, 0, 1, 1, 3, 4, 5, 5, 5], target = 1
# lo = 0, hi = 9, mid = 4, found
# lo = 0, hi = 4, mid = 2
# lo = 3, hi = 4, mid = 3, found
# lo = 3, hi = 3, mid = 3, found
# lo = 3, hi = 3, mid = 3, found
# inf

def my_bisect_neq(nums, target, left):

    lo = 0
    hi = len(nums)
    found = -1

    while lo < hi:
        mid = (lo + hi) // 2
        if target == nums[mid]:
            found = mid
            if left:
                hi = mid
            else:
                lo = mid + 1
        elif target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid

    return found

def my_bisect_eq(nums, target, left):

    lo = 0
    hi = len(nums) - 1
    found = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if target == nums[mid]:
            found = mid
            if left:
                hi = mid - 1
            else:
                lo = mid + 1
        elif target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1

    return found

def my_bisect(nums, target, left):
    return my_bisect_neq(nums, target, left)

input_size = 10
input_range = 10
nums = []
for i in range(input_size):
    nums.append(random.randint(0, input_range))

nums.sort()
print nums

#nums = [0, 0, 0, 1, 1, 3, 4, 5, 5, 5]
#target = 1

for i in range(100000):
    target = random.randint(0, input_range)
    #target = 1
    #print target

    res = bisect.bisect_left(nums, target)
    if res == len(nums) or nums[res] != target:
        res = -1

    my_res = my_bisect(nums, target, True)
    if res != my_res:
        print 'LEFT NOT CORRECT', 'target:', target, 'lib', res, 'mine is', my_res
        break


    my_res_eq = my_bisect_eq(nums, target, True)
    if res != my_res_eq:
        print 'LEFT NOT CORRECT with eq', 'target:', target, 'lib', res, 'mine is', my_res_eq
        break

    my_res = my_bisect(nums, target, False)

    res = bisect.bisect_right(nums, target)
    if res == 0 or nums[res-1] != target:
        res = -1
    else:
        res -= 1

    if res != my_res:
        print 'RIGHT NOT CORRECT', 'lib', res, 'mine is', my_res
        break

    my_res_eq = my_bisect_eq(nums, target, False)
    if res != my_res_eq:
        print 'RIGHT NOT CORRECT with eq', 'lib', res, 'mine is', my_res_eq
        break



