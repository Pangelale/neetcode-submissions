class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longestLIS = [1] * len(nums)

        for i in range(len(nums)):
            j = i - 1
            while j >= 0:
                if nums[j] < nums[i]:
                    longestLIS[i] = max(longestLIS[i], longestLIS[j] + 1)
                j -= 1

        
        return max(longestLIS)