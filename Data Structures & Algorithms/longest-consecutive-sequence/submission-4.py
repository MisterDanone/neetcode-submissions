class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        arr = []
        c = 1
        for i in range(len(nums)-1):
            if nums[i + 1] - nums[i] == 1:
                c += 1
            elif nums[i] == nums[i+1]:
                c += 0
            else:
                arr.append(c)
                c = 1
        arr.append(c)
        return max(arr)
