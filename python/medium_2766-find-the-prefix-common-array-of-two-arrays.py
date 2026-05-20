class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        
        seenA = set()
        seenB = set()
        
        ans = []
        common = 0
        
        for i in range(n):
            # add current elements
            seenA.add(A[i])
            seenB.add(B[i])
            
            # if A[i] already seen in B
            if A[i] in seenB:
                common += 1
            
            # if B[i] already seen in A
            # avoid double count when A[i] == B[i]
            if B[i] in seenA and A[i] != B[i]:
                common += 1
            
            ans.append(common)
        
        return ans