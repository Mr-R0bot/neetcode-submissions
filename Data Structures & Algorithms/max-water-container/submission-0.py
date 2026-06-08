class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        i, j = 0, len(heights)-1

        while i<j:
            ln = j-i
            wd = min(heights[i], heights[j])
            curarea = ln*wd
            maxarea = max(maxarea, curarea)

            if heights[i] >= heights[j]:
                j -= 1
            else:
                i += 1
        
        return maxarea