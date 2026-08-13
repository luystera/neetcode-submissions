class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # get the frequency of letters in each word
        # group together words with the same frequencies
        
        # list of strings to return
        ret = []
        # maps string to a frequency array
        groups = collections.defaultdict(list)

        # loop structure gives O(m * n) time as specified
        for i in range(len(strs)):
            alphabet_array = [0] * 26
            for j in strs[i]:
                # increase the frequency of that character
                alphabet_array[ord(j)-97] += 1
            # pair the string to the array
            key = tuple(alphabet_array)
            groups[key].append(strs[i])
        
        return list(groups.values())