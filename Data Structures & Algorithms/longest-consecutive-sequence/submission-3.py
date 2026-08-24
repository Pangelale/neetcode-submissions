class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) == 0:
            return 0

        count = 1
        longest_seq = 1
        for digit in range(len(nums) - 1):
            if nums[digit + 1] == nums[digit] + 1:
                count += 1
                longest_seq = max(longest_seq, count)
            elif nums[digit + 1] == nums[digit]:
                continue
            else:
                count = 1

        return longest_seq