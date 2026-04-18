class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       
        A,B = nums1,nums2
        if len(A)>len(B):
            A,B = B,A
        total = len(A)+len(B)
        half = total//2
        l,r = 0, len(A)-1
        while True:
            m = (l+r)//2
            n = half - m -2

            aleft = A[m] if m>=0 else float('-inf')
            aright = A[m+1] if (m+1)<len(A) else float('inf')
            bleft = B[n] if n>=0 else float('-inf')
            bright = B[n+1] if (n+1) < len(B) else float('inf')

            if aleft<=bright and bleft <= aright:
                if total%2:
                    return min(aright,bright)
                else:
                    return (max(aleft,bleft) + min(aright,bright)) /2
            elif aleft > bright:
                r = m - 1
            else:
                l = m+1

        