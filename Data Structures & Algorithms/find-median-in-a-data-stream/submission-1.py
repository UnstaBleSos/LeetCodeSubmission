class MedianFinder:

    def __init__(self):
        self.maxHeap= []
        self.minHeap =[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap,-num)

        heapq.heappush(self.minHeap,-(heapq.heappop(self.maxHeap)))

        if len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap,-(heapq.heappop(self.maxHeap)))
        elif len(self.minHeap) > len(self.maxHeap)+1:
            heapq.heappush(self.maxHeap,-(heapq.heappop(self.minHeap)))

    def findMedian(self) -> float:
        total = len(self.maxHeap) + len(self.minHeap)
        if total % 2 == 0:
            return ((self.minHeap[0] + (-(self.maxHeap[0])))/2)
        else:
            return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -(self.maxHeap[0])
        