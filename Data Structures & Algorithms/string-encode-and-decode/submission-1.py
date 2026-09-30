class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for word in strs:
            l = len(word)
            enc = str(l) + "#" + word
            encoded.append(enc)
        
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        cur = 0
        words = []
        while cur < len(s):
            start = cur
            while s[cur] != "#":
                cur += 1
            l = int(s[start: cur])
            cur += 1
            word = s[cur: cur + l]
            words.append(word)
            cur += l
        return words

