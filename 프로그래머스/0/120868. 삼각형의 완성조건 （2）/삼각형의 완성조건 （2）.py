def solution(sides):
    answer=0
    sides.sort()
    for i in range(1,2001):
        if i<sides[1]:
            if sides[1]<sides[0]+i:
                answer+=1
        else:
            if sides[0]+sides[1]>i:
                answer+=1
    return answer
                
        