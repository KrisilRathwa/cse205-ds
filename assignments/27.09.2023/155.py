class MinStack:

    def __init__(self):
        self.stk=[]
        self.min=None

    def push(self, val: int) -> None:
        if len(self.stk)==0:
            self.stk.append(val)
            self.min=val
        else:
            if val>self.min:
                self.stk.append(val)
            else:
                self.stk.append(2*val-self.min)
                self.min=val
        

    def pop(self) -> None:
        x=self.stk.pop()
        if x<self.min:
            self.min=2*self.min-x
        

    def top(self) -> int:
        x=self.stk[-1]
        if x>=self.min:
            return x
        else:
            return self.min
        

    def getMin(self) -> int:
        return self.min