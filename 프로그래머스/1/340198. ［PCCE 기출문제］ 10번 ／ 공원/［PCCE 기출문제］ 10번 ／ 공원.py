def solution(mats, park):
    answer = -1
    mats.sort()
    #돗자리 영역을 전체 파크에서 이터레이트하면서 가능한지 확인하기
    for mat in mats:
        for row in range(len(park)-mat+1):
            for col in range(len(park[0])-mat+1):
                possible=True
                for i in range(row,row+mat):
                    for j in range(col,col+mat):
                        if park[i][j] != "-1":
                            possible=False
                if possible:
                    answer=mat
                
    return answer