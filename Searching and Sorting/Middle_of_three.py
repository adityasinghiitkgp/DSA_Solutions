def middle(self,A,B,C):
    if (A>B and B>C) or (C>B and B>A):
        return B
    elif A>C and C>B  or (B>C and C>A):
        return C
    else:
        return A