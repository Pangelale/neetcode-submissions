class Solution:
    # True -> s2 contains perm of s1
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = {}
        s2_chars = {}
        
        if len(s1) > len(s2):
            return False

        for char in s1:
            s1_chars[char] = s1_chars.get(char, 0) + 1
        
        for i in range(len(s1)):
            s2_chars[s2[i]] = s2_chars.get(s2[i], 0) + 1

        if s1_chars == s2_chars:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            s2_chars[s2[left]] -= 1

            if s2_chars[s2[left]] == 0:
                del s2_chars[s2[left]]
            
            s2_chars[s2[right]] = s2_chars.get(s2[right], 0) + 1
            
            left += 1

            if s1_chars == s2_chars:
                return True
        
        return False


            


        