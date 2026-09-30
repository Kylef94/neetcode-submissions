class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]

        groups = dict()
        for word in strs:
            freqs = [0] * 26
            for char in word:
                freqs[ord(char) - 97] += 1
            
            freqs = tuple(freqs)
            if freqs not in groups:
                groups[freqs] = []
            
            groups[freqs].append(word)
        
        return list(groups.values())
        