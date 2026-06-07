class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fwd = [1] * len(nums)
        # for i, num in enumerate(nums):
        #     if i==0: # Or should i do enumerate(nums[1:]); Does slicing incur an O(n) cost separately
        #         continue
        for i in range(1, len(nums)):
            fwd[i] = fwd[i-1] * nums[i-1]

        bck = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            bck[i] = nums[i+1] * bck[i+1]
        
        output = []
        for i in range(len(nums)):
            prod = fwd[i] * bck[i]
            output.append(prod)
        
        return output
        
        # output = [1] * len(nums)
        # output[-1] = fwd[-1]
        

            
            
