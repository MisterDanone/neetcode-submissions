class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for index, a in enumerate(nums):
            if index > 0 and a == nums[index -1]:
                continue
            l, r = index + 1, len(nums) - 1
            while l < r:
                curSum = a + nums[l] + nums[r]
                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l +=1
        return res