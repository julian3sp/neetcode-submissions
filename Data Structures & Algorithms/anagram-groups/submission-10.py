class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            if tuple(counter) not in res:
                res[tuple(counter)] = []
            res[tuple(counter)].append(s)
        return list(res.values())