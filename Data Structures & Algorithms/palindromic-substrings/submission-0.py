class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for center in range(len(s)):
            # Find count for odd palindrome string lengths
            left = center
            right = center

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            # For even palindrome str. len
            left = center
            right = center + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count
            

            
