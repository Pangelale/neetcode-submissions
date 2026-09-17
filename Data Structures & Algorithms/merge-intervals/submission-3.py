class Solution:
    # Return array of non-overlapping intervals, any order

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        nonoverlap = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            prev = nonoverlap[-1]
            current = sorted_intervals[i]

            if current[0] <= prev[1]:
               nonoverlap[-1][1] = max(prev[1], current[1])

            else:
                nonoverlap.append(current)

        return nonoverlap
