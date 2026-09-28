class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        variable = {}
        for i in nums:
            if i in variable:
                variable[i] += 1
            else:
                variable[i] = 1

        for i in variable:
            if variable[i] >= 2:
                return True

        return False