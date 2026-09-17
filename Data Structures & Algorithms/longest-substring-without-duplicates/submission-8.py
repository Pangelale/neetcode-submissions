class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()
        longest_substring = 0
        L = 0

        for idx in range(len(s)):
            
            while s[idx] in seen_chars:
               seen_chars.remove(s[L])
               L += 1
            
            seen_chars.add(s[idx])

            if len(seen_chars) > longest_substring:
                longest_substring = len(seen_chars)
        
        return longest_substring
        