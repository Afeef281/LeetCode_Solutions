class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # res=count = 0
        # if len(s)<=1:
        #     return len(s)
        # hashstr ={}
        # index=i=0

        # while i<len(s):
        #     if s[i] in hashstr and s[i-1] == s[i]:
        #         count =1
        #     elif s[i] in hashstr and index ==0:count -=1
        #     elif s[i] in hashstr:pass
        #     else:
        #         hashstr[s[i]] = index
        #         index+=1
        #         count+=1
        #     i+=1

        #     res=max(res,count)
        # return res

        res = count = 0

        if len(s) <= 1:
            return len(s)

        hashstr = {}
        index = i = 0

        while i < len(s):

            if s[i] in hashstr and hashstr[s[i]] >= index:
                index = hashstr[s[i]] + 1

            hashstr[s[i]] = i

            count = i - index + 1
            res = max(res, count)

            i += 1

        return res