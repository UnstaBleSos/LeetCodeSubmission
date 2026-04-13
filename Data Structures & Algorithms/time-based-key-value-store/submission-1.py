class TimeMap:

    def __init__(self):
       self.values = dict()
       
       

    def set(self, key: str, value: str, timestamp: int) -> None:
        if len(key) == 0 or len(value)==0 or len(value)>100 or timestamp<=0:
            return None
        
        if key not in self.values:
            self.values[key] = []
            print(self.values)
        self.values[key].append((timestamp,value))
        print(self.values[key][0])
             
               
    def get(self, key: str, timestamp: int) -> str:
        timeline = self.values[key]
        left,right = 0, len(timeline)-1
        best= ""
        while left<=right:
            mid = (left+right) // 2
            if timeline[mid][0] <= timestamp:
                best = timeline[mid][1]
                left =  mid +1
            else:
                right = mid-1
        return best
            

        

