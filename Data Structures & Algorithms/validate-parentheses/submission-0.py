class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
    
        parentheses = {'(' : ")",
                       '{' : '}',
                       '[' : ']'}

        for char in s:
            if char in parentheses:
                stack.append(char)

            elif char in parentheses.values():
                if not stack: 
                    return False
                
                first_out = stack.pop()

                if parentheses[first_out] != char:
                    return False
                
        return len(stack) == 0
        
