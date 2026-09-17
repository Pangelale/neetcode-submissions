class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            current = intervals[i]

            # Before
            if current[1] < newInterval[0]:
                res.append(current)
            
            # After
            elif current[0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res

            # Overlap
            else:
                newInterval[0] = min(newInterval[0], current[0])
                newInterval[1] = max(newInterval[1], current[1])

        res.append(newInterval)

        return res

        