# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

class Solution:
    def letterCombinations(self, digits ):
        output = []
        letters = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        def dfs(digits, path = ""):
            if not digits:
                if path:
                    output.append(path)
                return 
            for char in letters[int(digits[0])-2]:
                path+= char
                dfs(digits[1:], path)
                path = path[:-1]
        dfs(digits)
        return output
            
        
        