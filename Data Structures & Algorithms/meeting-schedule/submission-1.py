"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i in intervals:
            print(i.start, i.end)
        for i in range(len(intervals)-1):
            print(intervals[i+1].end, intervals[i].start)
            if intervals[i+1].start < intervals[i].end:
                return False
        return True