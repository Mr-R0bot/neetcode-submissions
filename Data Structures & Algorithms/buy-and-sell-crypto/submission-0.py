class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        i, j = 0, 1

        while i<j and j<len(prices):
            while i<j and j<len(prices) and prices[i] < prices[j]:
                curprof = prices[j] - prices[i]
                maxprof = max(maxprof, curprof)
                j += 1
            
            if i<j and j<len(prices) and prices[i] >= prices[j]:
                i = j
                j += 1
        return maxprof
                
