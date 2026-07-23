class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # creates default list when key is absent

        # look over the list of strings
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())