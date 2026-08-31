class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        tuples_found = []
        
        for number in range(len(nums) - 2):
            L = number + 1
            R = len(nums) - 1

            if number > 0 and nums[number] == nums[number - 1]:
                continue

            while L < R:
                if L > number + 1 and nums[L] == nums[L - 1]:
                    L += 1
                    continue

                sum = nums[L] + nums[R] + nums[number]

                if sum > 0:
                    R -= 1
                elif sum < 0:
                    L += 1
                else:
                    tuples_found.append([nums[L], nums[R], nums[number]])
                    L += 1
                    R -= 1
        
        return tuples_found

        