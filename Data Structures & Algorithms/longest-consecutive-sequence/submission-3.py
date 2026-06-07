class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = set(nums)
        max_seqlen = 1
        for num in nums:
            if num - 1 in numset:
                # Not a sequence start
                continue 
            seqlen = 1
            numi = num + 1
            while numi in numset:
                seqlen += 1
                numi += 1
            max_seqlen = max(seqlen, max_seqlen)
        
        return max_seqlen