class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1=[]
        st2=[]
        for i in range(len(st1)):
            if st1 and s[i]=="#":
                st1.pop()
            else:
                if s[i]!="#":
                    st1.append(s[i])
        for i in range(len(st2)):
            if st2 and t[i]=="#":
                st2.pop()
            else:
                if t[i]!="#":
                    st2.append(t[i])
        if st1==st2:
            return True
        return False
