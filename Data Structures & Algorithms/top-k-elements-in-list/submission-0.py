class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # calculate the frequency of each number, add it to hashmap
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # iterate through the hashmap
        for n,c in count.items():
            freq[c].append(n)
        
        res = []
        # loop through freq in reverse order
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res