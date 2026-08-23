class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedStr = ''
        for char in s:
            if char.isalnum():
                cleanedStr += char.lower()
        print(cleanedStr)  

        left = 0
        right = len(cleanedStr) - 1

        while left < right:
            if cleanedStr[left] == cleanedStr[right]:
                left += 1
                right -= 1
            else:
                return False

        return True

        