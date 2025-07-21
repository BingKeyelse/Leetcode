from typing import List

def canAttendMeetings(intervals: List[List[int]]) -> bool:

    # Sắp xếp các khoảng thời gian theo thời gian bắt đầu
    intervals.sort(key=lambda x: x[0])
    
    # Kiểm tra các khoảng thời gian có trùng lặp hay không
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    
    return True