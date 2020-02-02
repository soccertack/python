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

def my_bisect_left(nums, target):

    lo = 0
    hi = len(nums)
    found = -1

    while lo < hi:
        mid = (lo + hi) // 2

        if target == nums[mid]:
            found = mid
            hi = mid
        elif target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid

    return found

def my_bisect(nums, target, left):

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

input_size = 10
input_range = 5
nums = []
for i in range(input_size):
    nums.append(random.randint(0, input_range))

nums.sort()
print nums

for i in range(100000):
    target = random.randint(0, input_range)

    res = bisect.bisect_left(nums, target)
    if res == len(nums) or nums[res] != target:
        res = -1

    my_res = my_bisect_left(nums, target)
    if res != my_res:
        print 'LEFT NOT CORRECT', 'target:', target, 'lib', res, 'mine is', my_res
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




