class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []

        for s in strs:
            encoded_str.append(str(len(s)) + "#" + s)

        encoded_str = "".join(encoded_str)

        return encoded_str


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            deliminator = i

            while s[deliminator] != "#":
                deliminator += 1
            
            word_len = int(s[i:deliminator])
            start = deliminator + 1
            end = start + word_len
            decoded_strs.append(s[start:end])
            i = end

        return decoded_strs
