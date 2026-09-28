class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        while strs:
            current = strs.pop(0)  # Take the first string
            group = [current]
        # Compare with all other strings
            i = 0
            while i < len(strs):
                if len(current) == len(strs[i]) and sorted(current) == sorted(strs[i]):
                    group.append(strs.pop(i))  # Add to group and remove from strs
                else:
                    i += 1
            res.append(group)
        return res