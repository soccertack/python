import sys
nums = [3, 18, 18, 18, 18, 18, 18, 25]
nums = [18, 18, 18, 18]
nums = [3, 3, 3, 3, 18, 18, 18, 18, 200, 200, 200, 7777, 7777, 7777, 7777, 7777, 7777]
#nums = [1, 3, 5]
nums = [1, 3, 5, 7]
target = int(input())

print('--input array--')
for idx, val in enumerate(nums):
    print idx, val
print('----')

#return idx that first nums[idx] > target
# For duplicates, it returns the first occurance of it
# for target < nums[0], return 0
# for target > nums[-1], return len(nums)
# 
def basic(target):
    lo = 0
    hi = len(nums) - 1

    if target < nums[lo] or target > nums[hi]:
        print 'out of range'
        return -1

    while lo < hi:
        mid = (lo + hi) / 2

        if nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid
            break

    if nums[lo] < target:
        lo += 1

    return lo

def dup_lower():
    return basic()

def dup_upper():
    lo = 0
    hi = len(nums) - 1

    if target < nums[lo] or target > nums[hi]:
        print 'target is out of range'
        return -1

    valid_lo = lo

    while lo <= hi:
        print 'dup_upper', lo, hi
        mid = (lo + hi) / 2

        if nums[mid] == target:
            lo = mid + 1
        elif nums[mid] <= target:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo

def binLowerBound(a, lo, hi, x):
    if (lo > hi):
        return lo;

    mid = lo +  (hi - lo) / 2;
    if (a[mid] == x):
        return binLowerBound(a, lo, mid-1, x);
    elif a[mid] > x:
        return binLowerBound(a, lo, mid-1, x);
    else:
        return binLowerBound(a, mid+1, hi, x);

def binHigherBound(a, lo, hi, x):
    if (lo > hi):
        return lo;
    mid = lo + (hi - lo) / 2;
    if (a[mid] == x):
        return binHigherBound(a, mid+1, hi, x);
    elif (a[mid] > x):
        return binHigherBound(a, lo, mid-1, x);
    else:
        return binHigherBound(a, mid+1, hi, x);

idx = basic(target)
print 'basic with bigger', idx

#idx = basic(target - 1)
#print 'basic with smaller', idx

#idx = dup_lower()
#print 'dub_lower', idx
#
#idx = dup_upper()
#print 'dub_upper', idx

#idx = binLowerBound(nums, 0, len(nums) - 1, target)
#print 'lower bound', idx
#
#idx = binHigherBound(nums, 0, len(nums) - 1, target)
#print 'higher bound', idx
