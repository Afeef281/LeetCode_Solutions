class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        braces =[]

        for i in range(n):
            if s[i] =='(' or s[i] == '{' or s[i] == '[':
                braces.append(s[i])
            elif s[i] ==')' or s[i] == '}' or s[i] == ']':
                if len(braces)==0:
                    return False
                else:
                    if braces[-1] =='(' and s[i] ==')':
                        braces.pop()
                    elif braces[-1] == '{' and s[i] == '}':
                        braces.pop()
                    elif braces[-1] == '[' and s[i] == ']':
                        braces.pop()
                    else :
                        return False
        if len(braces)>0:
            return False
        return True
                
                    
