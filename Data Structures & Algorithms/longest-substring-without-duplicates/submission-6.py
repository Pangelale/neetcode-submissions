class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # current_substring = []
        # max_count = 0

        # for char in s:

        #     if char not in current_substring:
        #         current_substring.append(char)

        #     else:
        #         char_index = current_substring.index(char)
        #         current_substring = current_substring[char_index + 1:]
        #         current_substring.append(char)
            
        #     max_count = max(max_count, len(current_substring))

        current_substring = set()
        L = 0
        max_count = 0

        for i in range(len(s)):
            while s[i] in current_substring:
                current_substring.remove(s[L])
                L += 1

            current_substring.add(s[i])
            max_count = max(max_count, len(current_substring))

        return max_count
