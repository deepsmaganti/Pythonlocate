
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            prev, current = result[-1], intervals[i]
            if current.start <= prev.end:
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)
        return result

def merge(self, intervals):
    if not intervals:
        return []
    int_sort = sorted(intervals, key=lambda x: x.start)
    ans, start, end = [], int_sort[0].start, int_sort[0].end
    for n in int_sort[1:]:
        if n.start > end:
            ans.append(Interval(start, end))
            start, end = n.start, n.end
        else:
            end = max(end, n.end)
    ans.append(Interval(start, end))
    return ans