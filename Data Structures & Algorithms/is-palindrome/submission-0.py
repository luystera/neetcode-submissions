class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers, one at the beginning and one at the end
        left_ptr = 0
        right_ptr = len(s)-1

        while(left_ptr < right_ptr):
            if (s[left_ptr].isalnum()):
                if (s[right_ptr].isalnum()):
                    # need to convert to lowercase characters so that 'A' and 'a' are equal
                    if (s[left_ptr].lower() != s[right_ptr].lower()):
                        return False
                    right_ptr -= 1
                    left_ptr += 1
                else:
                    right_ptr -= 1
            else:
                left_ptr += 1
            
        return True