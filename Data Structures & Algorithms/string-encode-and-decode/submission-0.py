class Solution:

    def encode(self, strs: List[str]) -> str:
        ret_str = []
        for s in strs:
            # efficient way to join 
            ret_str.append(f"{len(s)}#{s}")
        # ["Hello", "World"] -> 5#Hello5#World
        return "".join(ret_str)

    def decode(self, s: str) -> List[str]:
        ret = []

        i = 0
        while i < len(s):
            # locate the position of the delimiter
            j = s.find('#', i)
            length = int(s[i:j])
            # find where the word starts and ends
            start = j + 1
            end = start + length
            # append that string to the list
            ret.append(s[start:end])
            # move the pointer to the end of the word
            i = j + 1 + length

        return ret

            
        