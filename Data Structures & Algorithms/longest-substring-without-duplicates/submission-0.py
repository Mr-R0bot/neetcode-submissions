class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxln = 0
        i, j = 0, 0
        substr = set()

        while j < len(s):
            if s[j] not in substr:
                maxln = max(maxln, j-i+1)
                substr.add(s[j])
                j += 1

            elif s[j] in substr:
                substr.remove(s[i])
                i += 1
        
        return maxln
        