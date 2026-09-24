class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashstr ={}

        for ch in jewels:
            hashstr[ch] = hashstr.get(ch,0)+1
        count =0
        for ch in stones:
            if ch in hashstr:
                count +=1
        return count