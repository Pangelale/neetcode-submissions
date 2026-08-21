class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_pair = []
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[i] + nums[j + 1] == target:
                    if i < j + 1:
                        idx_pair.append(i)
                        idx_pair.append(j + 1)
                        return idx_pair
                    elif i > j + 1:
                        idx_pair.append(j + 1)
                        idx_pair.append(i)
                        return idx_pair


        