class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        current_height = 0
        current_width = 0
        current_area = 0

        L = 0
        R = len(heights) - 1
        while L < R:
            current_height = min(heights[L], heights[R])
            current_width = R - L
            current_area = current_height * current_width

            if current_area > max_area:
                max_area = current_area
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
            
        return max_area






        

