class Solution:
    def sortSentence(self, s: str) -> str:
        strlist = s.split()

        for j in range(len(strlist)):
            for i in range(len(strlist) - 1 - j):
                if strlist[i][-1] > strlist[i + 1][-1]:
                    strlist[i], strlist[i + 1] = strlist[i + 1], strlist[i]

        for i in range(len(strlist)):
            strlist[i] = strlist[i][:-1]

        s = " ".join(strlist)
        return s