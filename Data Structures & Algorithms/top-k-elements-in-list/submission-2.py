class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        setted = set(nums)
        arr = []
        for i in setted:
            arr.append(nums.count(i))

        arr = sorted(arr, reverse = True)

        res = set()

        for n in range(k):
            curr = arr.pop(0)
            for i in setted:
                if nums.count(i) == curr:
                    res.add(i)
                        
                
        return list(res)