class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need],index]
            elif num not in seen:
                seen[num] = index

        return -1