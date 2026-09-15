class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if nums[i] in map and map[nums[i]] != i:
                return [map[nums[i]], i]
                
            map[diff] = i
