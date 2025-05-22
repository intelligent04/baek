def solution(diffs, times, limit):
    answer = 0
    
    start = 1
    end = max(diffs)

    while start < end:
        level=(start+end)//2
        for i in range(len(diffs)):
            if diffs[i]<=level:
                answer+=times[i]
            else:
                answer+=(times[i]+times[i-1])*(diffs[i]-level)+times[i]
            if answer>limit:
                break
        if answer>limit:
            start=level+1
        else:
            end = level

        answer=0


    return end