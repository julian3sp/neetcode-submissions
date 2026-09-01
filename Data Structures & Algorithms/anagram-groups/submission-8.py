class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            cur = ''.join(sorted(s))
            if cur not in anagrams:
                anagrams[cur] = []
            anagrams[cur].append(s)
        return list(anagrams.values())

