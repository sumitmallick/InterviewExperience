# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

# You may assume the input array always has a valid answer.
import random

def wiggle_sort(nums):
    n = len(nums)
    
    def nth_element(k):
        left, right = 0, n-1
        while True:
            pivot = nums[random.randint(left, right)]
            l, r = left, right
            i = left
            while i <= r:
                if nums[i] < pivot:
                    nums[i], nums[l] = nums[l], nums[i]
                    i +=
                    l +=1 
                elif nums[i] > pivot:
                    nums[i], nums[r] = nums[r], nums[i]
                    r -= 1
                else:
                    i += 1
            if k < l:
                right = l - 1
            elif k > r:
                left = r + 1
            else:
                return nums[k]
    
    median = nth_element(n // 2)
    
    def idx(i):
        return (1+2*i) % (n | 1)
    
    i, j, k = 0, 0, n-1
    
    while j <= k:
        if nums[idx(j)] > median:
            nums[idx(i)], nums[idx(j)] = nums[idx(j)], nums[idx(i)]
            i += 1
            j += 1
        elif nums[idx(j)] < median:
            nums[idx(j)], nums[idx(k)] = nums[idx(k)], nums[idx(j)]
            k -= 1
        else:
            j += 1


nums = [1,5,1,1,6,4]
print(f"Before sort: {nums}")
wiggle_sort(nums)
print(f"After sort: {nums}")
