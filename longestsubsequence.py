def findLongestConseqSubseq(arr, N):
    s = set(arr)
    longest_streak = 0
    
    for num in arr:
        if num - 1 not in s:
            current_num = num
            current_streak = 1

            while current_num + 1 in s:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak

t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(findLongestConseqSubseq(l, n))
