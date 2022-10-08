def find_median(self, v):
    v.sort()
    n=len(v)
    if len(v)%2!=0:
        return v[(n//2)]
    else:
        return (v[(n//2)]+v[(n//2)-1])//2