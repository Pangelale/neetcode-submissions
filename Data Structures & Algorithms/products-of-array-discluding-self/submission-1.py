class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            outputs[i] = left
            left *= nums[i]

        right = 1
        for j in range(len(nums) - 1, -1, -1):
          outputs[j] *= right
          right *= nums[j]
        
        return outputs