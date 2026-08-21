class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_freq = {}

        for num in nums:

            if num not in most_freq:
                most_freq[num] = 0
            most_freq[num] += 1

        most_freq = sorted(most_freq, key = most_freq.get, reverse=True)
        print(most_freq)


        return most_freq[:k]




        
        