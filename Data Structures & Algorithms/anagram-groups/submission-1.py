class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)

        # loop through each string in strs
        for s in strs:
            # have an index for each letter
            count = [0] * 26

            # loop through each character in s
            for c in s:
                # ord() gets the ASCII value of a char
                count[ord(c)-97] += 1

            # group all strings with the same count
            # lists cannot be keys, so change count to a tuple
            ret[tuple(count)].append(s)

        return list(ret.values())