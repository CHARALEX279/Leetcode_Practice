class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        extra = ""
        merged_str = ""
        w1_len = len(word1)
        w2_len = len(word2)

        if w1_len > w2_len:
            extra = word1[w2_len:]
            word1 = word1[:w2_len]
        elif w1_len < w2_len:
            extra = word2[w1_len:]
            word2 = word2[:w1_len]
            print(extra)

        for character in range(len(word1)):
            merged_str = merged_str + word1[character]
            merged_str = merged_str + word2[character]

        if extra != "":
            merged_str = merged_str + extra
        
        return merged_str      
