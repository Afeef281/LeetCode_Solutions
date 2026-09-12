class Solution:
    def frequencySort(self, s: str) -> str:
        hashstr ={}
        for char in s:
            hashstr[char] = hashstr.get(char,0)+1
        items = list(hashstr.items())

        n = len(items)

        for i in range(n - 1):
            for j in range(n - i - 1):
                if items[j][1] < items[j + 1][1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
        s=''
        
        
        for key, value in items:
            for i in range(value):
                s+=key
        return s
        