class Solution:

    # Return k most frequent elements within array
    # Frequent : hashmap
    # topK : heap

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        heap = []

        for num in nums:
            frequency[num] = frequency.get(num,0) + 1
        
        for num, freq in frequency.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for freq, num in heap:
            result.append(num)

        return result
        