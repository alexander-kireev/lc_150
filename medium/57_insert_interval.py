def insert(intervals, new_interval):
    output = []

    if not intervals:
        return new_interval
    
    if new_interval[1] < intervals[0][0]:
        return intervals.prepend(new_interval)

    if new_interval[0] > intervals[-1][1]:
        return intervals + new_interval

    num_intervals = len(intervals)
    i = 0

    while i < num_intervals:
        interval = intervals[i]
        start = interval[0]
        end = interval[1]

        if new_interval[1] < start:
            output.append(new_interval)
            return output + intervals[i:]
        
        if new_interval[0] <= end and new_interval[1] >= start:
            start = min(start, new_interval[0])
            end = max(end, new_interval[1])
            
            while i < num_intervals:
                if end >= intervals[i][0]:
                    end = max(end, intervals[i][1])
                else:
                    break
                i += 1

            output.append([start, end])
            return output + intervals[i:]

        output.append(interval)
        i += 1




intervals = [[3,5],[12,15]]
newInterval = [6,6]

# Output: [[1,2],[3,10],[12,16]]

print(insert(intervals, newInterval))