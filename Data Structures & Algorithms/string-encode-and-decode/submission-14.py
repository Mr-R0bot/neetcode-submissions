class Solution:

    def encode(self, strs: List[str]) -> str:
        # Q. Easier/efficient to append to a list and join later or keep adding to a string??
        encoded = []
        for s in strs:
            ln = len(s)
            encoded.append(f"{ln}:")
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        # 1. First keep iterating till : is reached and keep collecting the digits
        # that will form the len.

        # 2. Then we need to iterate till that len and append that to output
        # Then again repeat what we did 1

        # So each outer iteration should complete 1 and 2.
        # print(s)
        decoded = []
        i = 0
        while i<len(s):
            j = i
    
            # 1. Collect len digits till first :
            while s[j] != ':':
                j += 1
            # print(i, j)
            # print(s[i:j])
            ln = int(s[i:j])

            # 2. Get str for ln chars afer :
            decoded.append(s[j+1:j+1+ln])

            # 3. Update i
            i = j+1+ln
            # print(i)
            if i>=len(s):
                break
        return decoded

                


