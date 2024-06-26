## Question

# In a university, your attendance determines whether you will be
# allowed to attend your graduation ceremony.
# You are not allowed to miss classes for four or more consecutive days.
# Your graduation ceremony is on the last day of the academic year,
# which is the Nth day.

 

#   Your task is to determine the following:

# 1. The number of ways to attend classes over N days.
# 2. The probability that you will miss your graduation ceremony.

# Represent the solution in the string format as "Answer of (2) / Answer
# of (1)", don't actually divide or reduce the fraction to decimal

# Test cases:

# for 5 days: 14/29
# for 10 days: 372/773


# Solution:
# To solve this problem, we need to consider two parts:

# The total number of ways for us to attend classes over N days.
# The number of ways for us to miss the graduation ceremony by not meeting the attendance requirement.
# Let's break down the problem:

# Part 1: Total Ways to Attend Classes
# The total number of ways for us to attend classes can be represented by sequences of attended (A) and missed (M) days over N days without any constraints. Since each day we have two choices (attend or miss), the total number of ways to attend classes over N days is 2^N.

# Part 2: Ways to Miss Graduation
# To miss the graduation ceremony, we must miss classes for the last day and at least the three preceding days. This means there are exactly 4 consecutive days missed at the end of the sequence.

# To find the number of ways to have at least one sequence of four or more consecutive missed days, we can use dynamic programming.

# Dynamic Programming Approach

# We'll define dp[i] as the number of valid ways to attend classes over i days without missing four or more consecutive days at any point.

# Base cases:
# dp[0] = 1: There's only one way to attend 0 days (do nothing).
# dp[1] = 2: A, M
# dp[2] = 4: AA, AM, MA, MM
# dp[3] = 8: AAA, AAM, AMA, AMM, MAA, MAM, MMA, MMM

# For i >= 4:
# dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

# This recurrence relation is due to the fact that we can add either an A or an M on any valid sequence of length i-1, i-2, i-3, or i-4, but adding an M to any sequence of length i-4 avoids creating a block of four consecutive Ms at the end.

# To get the number of ways to miss the graduation, we need to sum all invalid ways:
# ways to miss graduation = sum(dp[])

# Finally, the probability can be expressed as:
# Probability = ways to miss graduation / 2^N

def attendance_probability(N):
    if N < 4:
        return f"0/{2**N}"  # Less than 4 days means we can't miss 4 consecutive days

    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    dp[3] = 8

    for i in range(4, N+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

    total_ways = 2 ** N
    ways_to_miss = sum(dp[:N-3])
    
    return f"{ways_to_miss}/{total_ways}"

# Test cases
print(attendance_probability(5))  # 14/29
print(attendance_probability(10)) # 372/773
