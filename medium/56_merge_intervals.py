
def merge(intervals):
    intvals = sorted(intervals)
    output = []
    num_intvals = len(intervals)
    count = 0

    while count < num_intvals:
        cur_intval = intvals[count]
        start_intval = cur_intval[0]
        end_intval = cur_intval[1]

        while count + 1 < num_intvals and end_intval >= intvals[count + 1][0]:
            end_intval = max(intvals[count + 1][1], end_intval)
            count += 1
        
        output.append([start_intval, end_intval])
        count += 1

    return output









intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[4,7],[1,4],[5,9],[16,19]]

print(merge(intervals))

# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].