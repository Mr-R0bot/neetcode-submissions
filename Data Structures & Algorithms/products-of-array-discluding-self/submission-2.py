class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fwd = [1] * len(nums)
        for i in range(1, len(nums)):
            fwd[i] = fwd[i-1] * nums[i-1]

        
        output = [1] * len(nums)
        output[-1] = fwd[-1]
        prod = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            output[i] = fwd[i] * prod
            prod *= nums[i]
        
        return output

        """
        bck = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            bck[i] = nums[i+1] * bck[i+1]
        
        output = []
        for i in range(len(nums)):
            prod = fwd[i] * bck[i]
            output.append(prod)
        
        return output
        """

            
            
