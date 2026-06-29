class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for l in s:
            if l in letters:
                letters[l] = letters[l] + 1
            else:
                letters[l] = 1
        for l in t:
            if l not in letters:
                return False
            else:
                letters[l] = letters[l] - 1
                if letters[l] == 0:
                    del letters[l]
        if len(letters) == 0:
            return True
        return False

        
        