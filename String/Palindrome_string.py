class Solution:
    def isPalindrome(self, S):
        i=0
        j=len(S)-1
        while i<j:
            if S[i]!=S[j]:
                return 0
            i+=1
            j-=1
        return 1