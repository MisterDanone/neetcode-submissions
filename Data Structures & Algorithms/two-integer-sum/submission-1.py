class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            if nums.count(target - nums[i]) != 0:
                if target - nums[i] == nums[i] and nums.count(nums[i]) >= 2:
                    return sorted([i, nums.index(target - nums[i], i+1)])
                elif nums.count(target - nums[i]) >=1 and not(target - nums[i] == nums[i]):
                    return sorted([i, nums.index(target - nums[i])])
        return False
