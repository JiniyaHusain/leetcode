class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len=len(nums)
        for i in range(nums_len):
            for j in range(nums_len):
                if j!=i:
                    if nums[i]+nums[j]==target:
                        return [i,j]

        