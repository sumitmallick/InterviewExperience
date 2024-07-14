# Koko loves to eat bananas. There are N piles of bananas, the i-th pile has piles[i] bananas. The guards have gone and will come back in H hours.

# Koko can decide her bananas-per-hour eating speed of K. Each hour, she chooses some pile of bananas, and eats K bananas from that pile.

# If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards come back.

# Return the minimum integer K such that she can eat all the bananas within H hours.

# Input: piles = [30,11,23,4,20], H = 6

# Output: 23




# Input: piles = [3,6,7,11], H = 8

# Output: 4
from math import ceil

class Solution:
    def solution(self,s):
        # write the solution here..
        s = s.split(",")
        H = int(s[-1])
        piles = s[:-1]
        piles = [int(i) for i in piles]
        def wrapper(speed):
            return sum(ceil(pile / speed) for pile in piles) <= H

        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if wrapper(mid):
                high = mid
            else:
                low = mid + 1
        return low


def main():
  line = input()
  ret = Solution().solution(line)

  print(ret)

if __name__ == '__main__':
    main()