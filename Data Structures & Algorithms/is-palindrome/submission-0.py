class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace(" ", "")
        # s = s.lower()
        s_clean = ""

        for char in s:
            if char.isalnum():
                s_clean += char.lower()

        i = 0
        j = len(s_clean) - 1

        while i < j:
            if s_clean[i] != s_clean[j]:
                return False
            i += 1
            j -= 1

        return True
