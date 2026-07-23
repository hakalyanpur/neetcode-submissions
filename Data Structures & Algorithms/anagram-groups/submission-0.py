class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            signature = ''.join(sorted(word))
            anagrams[signature].append(word)

        
        return list(anagrams.values())




