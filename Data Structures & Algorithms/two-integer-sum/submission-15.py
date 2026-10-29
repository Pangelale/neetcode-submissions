# Input: array of. ints
#        int target
# Output: indices that equal target where i != j

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}

        for i in range(len(nums)):
            r = target - nums[i]

            if r in seen_nums:
                return [seen_nums[r], i]
            else:
                seen_nums[nums[i]] = i
            
        