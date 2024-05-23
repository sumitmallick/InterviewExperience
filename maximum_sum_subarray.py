## Task: **Problem Statement: Maximum Sum Subarray**

# You are given an array of integers, and your task is to find the contiguous subarray with the maximum sum. In other words, you need to determine the subarray that has the largest sum among all possible contiguous subarrays.

# Write a function or algorithm to solve this problem efficiently, with the following specifications:

# **Input:** An array of integers, where 1 ≤ n ≤ 10^5, and each element of the array is an integer between -10^4 and 10^4.

# **Output:** Return the sum of the maximum sum subarray.

# **Example:** 

# ```
# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: The contiguous subarray [4, -1, 2, 1] has the maximum sum (4 + (-1) + 2 + 1 = 6).
# ```

# **Constraints:**

# - The array may contain both positive and negative integers.
# - An empty array is not a valid input.
# - The array may contain only one element.

# Solve the problem with efficiency and provide a clear explanation of your approach.


def maaximum_sum_subarray(input_arr):
    if not input_arr:
        return 0

    max_arr, max_arr_end = 0, 0

    for value in input_arr:
        max_arr = max(value, max_arr + value)
        if max_arr > max_arr_end:
            max_arr_end = max_arr

    return max_arr_end

print(maaximum_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # Output: 6
# Time Complexity: O(n) & Space Complexity: O(1)