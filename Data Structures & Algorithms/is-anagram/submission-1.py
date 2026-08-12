class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force solution would be to sort the strings and compare

        # 2 hashmaps for tracking character counts in the strings
        s_map = {}
        t_map = {}

        # check strings are the same length
        if (len(s) != len(t)):
            return False
       
        # populate hashmaps
        for schar,tchar in zip(s,t): 
            s_map[schar] = s_map.get(schar, 0) + 1
            t_map[tchar] = t_map.get(tchar, 0) + 1
        
        # now check if the frequencies are equal
        return s_map == t_map