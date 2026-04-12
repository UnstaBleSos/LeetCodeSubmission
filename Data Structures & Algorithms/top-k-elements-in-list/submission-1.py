class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=0
            freq[i]+=1
        sorts = sorted(list(freq.items()),key=lambda pair:pair[1],reverse=True)
        values = []
        counter =0
        for x in sorts:
            if counter!=k:
                values.append(x[0])
                counter+=1
        
        return values
        
        
          
        
       