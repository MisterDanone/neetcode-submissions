class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers[::-1]:

            if numbers.count(target - i) != 0 :
                if target - i != i:
                    return [numbers.index(target - i)+1,numbers.index(i)+1]
                else:
                    return [numbers.index(i),numbers.index(i)+1]

        return -1