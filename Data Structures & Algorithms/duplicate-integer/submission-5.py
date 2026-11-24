class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set(nums)
        print(n)
        print(nums)

        if len(nums) != len(n):
            return True

        return False