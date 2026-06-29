class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        vowels = "aeiouAEIOU"
        ans = []
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels:
                word = word + "ma" + "a" * (i + 1)
                ans.append(word)
            else:
                word = word[1:] + word[0] + "ma" + "a" * (i + 1)
                ans.append(word)
        return " ".join(ans)
