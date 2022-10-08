
Menu






























































Refresh

Time (IST)	Status	Lang	Test Cases	Code
2021-07-27 09:48:47	Correct	python3	-	View
2021-07-27 09:46:27	Wrong	python3	-	View
2021-07-27 09:46:05	Wrong	python3	-	View
2021-07-27 09:42:25	Wrong	python3	-	View
2021-07-27 09:42:14	Wrong	python3	-	View
2021-07-27 09:38:14	Wrong	python3	-	View
2021-02-14 08:40:19	Correct	python3	-	View

def match(a,b):
    if len(a)!=len(b):
        return False
        
    for i,j in zip(a,b):
        
        if i!=j:
            return False
    return True
class Solution:
    def checkMirrorTree(self, n, e, A, B):
        graphA=defaultdict(list)
        graphB=defaultdict(list)
        
        while A:
            u=A.pop(0)
            v=A.pop(0)
            graphA[u].append(v)
        
        while B:
            u=B.pop(0)
            v=B.pop(0)
            graphB[u].append(v)

        for k in graphA:
            a=graphA[k]
            b=graphB[k]
            
            b=b[-1::-1]
           
            if not match(a,b):
                return 0
        return 1
        # code here