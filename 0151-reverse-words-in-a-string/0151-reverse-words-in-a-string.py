class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        # words = []
        # word = ""

        # for i in range(len(s)):
        #     if s[i] != ' ':
        #         word += s[i]
        #     else:
        #         if word != "":
        #             words.append(word)
        #             word = ""

        # if word != "":
        #     words.append(word)
                
        res =[]

        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])
            if i != 0:
                res.append(" ")

        return "".join(res)

        
        