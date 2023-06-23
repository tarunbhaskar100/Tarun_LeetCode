class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= out[-1][1]:
                out[-1] = [min(out[-1][0],intervals[i][1]),max(intervals[i][1],out[-1][1])]
            else:
                out.append(intervals[i])
        return out