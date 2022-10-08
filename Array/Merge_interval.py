def merge(intervals):
    lis=[]
    intervals.sort()
    lis.append(intervals[0])
    for i in range(1,len(intervals)):
        if intervals[i][0]>lis[-1][1]:
            lis.append(intervals[i])
        else:
            x=lis.pop()
            last=max(x[1],intervals[i][1])
            lis.append([x[0],last])
    return lis