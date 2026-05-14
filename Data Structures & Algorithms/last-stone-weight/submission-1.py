class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        print(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            print(x, y)
            if y > x:
                heapq.heappush(maxHeap, x-y)
                print(maxHeap)
        if len(maxHeap):
            return abs(heapq.heappop(maxHeap))
        return 0