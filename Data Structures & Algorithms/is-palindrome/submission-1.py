class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            # make sure the char is alphanumeric
            if c.isalnum():
                # only add lowercase letters
                newStr += c.lower()
        # [::-1] is python syntax for reversing a string
        return newStr == newStr[::-1]