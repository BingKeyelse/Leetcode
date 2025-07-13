from typing import List


def longestOnes(nums: List[int], k: int) -> int:

    # Lập trình tại đây
    counter = [0, 0]
    i = 0  # right
    j = 0  # left
    final = 0
    nums.append(0)
    while i < len(nums):
        if counter[0] <= k:
            final = max(counter[0] + counter[1], final)
            counter[nums[i]] += 1
            i += 1
        else:
            counter[nums[j]] -= 1
            j += 1

    return final


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(longestOnes(nums, k))
