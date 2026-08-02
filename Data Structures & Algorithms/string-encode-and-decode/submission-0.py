class Solution:

    def encode(self, strs: List[str]) -> str:
        # join strings with their char lengths before them and a marking delimiter
        # [dog, 3cat, 1#3] -> 3#dog4#3cat3#1#3
        encoded_string = ""

        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # iterate through chars in the encoded string
        # when at the start of a str, keep appending nums to str_length string until delimiter is reached, then traverse+add the next str_length characters
        decoded_strs = []
        str_length = ""
        i = 0

        while i < len(s):
            if s[i] != "#":
                str_length += s[i]
                i += 1
            else:
                decoded_strs.append(str(s[i+1 : i+int(str_length)+1]))
                i += int(str_length) + 1
                str_length = ""
        
        return decoded_strs