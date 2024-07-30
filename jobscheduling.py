t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    e = list(map(int, input().split()))
    
    # Create a list of meetings with their start time, end time, and original index
    meetings = [(s[i], e[i], i + 1) for i in range(n)]
    

    # Sort the meetings by their end times
    meetings.sort(key=lambda x: x[1])
    
    # Initialize variables
    last_end_time = 0
    selected_meetings = []
    
    for start, end, index in meetings:
        if start >= last_end_time:
            selected_meetings.append(index)
            last_end_time = end
    
    # Print the order of the selected meetings
    print(' '.join(map(str, selected_meetings)))
