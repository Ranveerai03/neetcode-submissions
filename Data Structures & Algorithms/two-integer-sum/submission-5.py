class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tmp = {}

        for i, n in enumerate(nums):
            if target - n in tmp:
                return [tmp[target - n], i]
            else:
                tmp[n] = i
        