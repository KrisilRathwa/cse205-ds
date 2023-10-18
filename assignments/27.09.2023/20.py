class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        brackets={'(':')', '[':']', '{':'}'}

        for c in s:
            if c in brackets:
                stk.append(c)
            elif stk and c == brackets[stk.pop()]:
                continue
            else:
                return False
        return not stk