class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            option1 = num
            option2 = num * current_min
            option3 = num * current_max

            current_max = max(option1, option2, option3)
            current_min = min(option1, option2, option3)

            max_product = max(max_product, current_max)

        
        
        return max_product
