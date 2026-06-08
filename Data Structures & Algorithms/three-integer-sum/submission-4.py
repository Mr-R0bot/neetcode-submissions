class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()

        for k in range(len(nums)-2):
            target = -nums[k]
            i, j = k+1, len(nums)-1
            while i<j:
                if nums[i] + nums[j] == target:
                    res.add((nums[k], nums[i], nums[j]))
                    i+=1
                    j-=1
                if nums[i] + nums[j] > target:
                    j-=1
                if nums[i] + nums[j] < target:
                    i+=1
        
        return [[trip[0], trip[1], trip[2]] for trip in res]
        # res = []
        # for trip in sum3:
        #     for num in trip:

        