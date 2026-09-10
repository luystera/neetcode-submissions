class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert the array to a hashset
        hashset = set(nums)
        max_seq = 0
        curr_seq = 0
        for num in hashset:
            if (num - 1) not in hashset:
                # this is the start of a new sequence
                curr_seq = 0
                curr = num
                while (curr in hashset):
                    print("num:" + str(curr))
                    curr += 1
                    curr_seq += 1
                print("seq:" + str(curr_seq))
                if (max_seq < curr_seq):
                    max_seq = curr_seq
        
        return max_seq