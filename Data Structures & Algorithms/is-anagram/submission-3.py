class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sChar = {}
        tChar = {}

        for i in range(len(s)):
            char = s[i]
            if char in sChar:
                sChar[char] += 1
            else:
                sChar[char] = 1
            
            char = t[i]
            if char in tChar:
                tChar[char] += 1
            else:
                tChar[char] = 1
        
        if sChar == tChar:
            return True
        else:
            return False

        