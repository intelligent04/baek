def binary_search(target, start, end):
    if start > end:		 # 범위를 넘어도 못찾는다면 -1을 반환
        print(0,end=" ")
        return

    mid = (start + end) // 2  # 중간값

    if cards[mid] == target:
        print(1,end=" ")	# 중간값의 데이터가 target과 같다면 mid를 반환
        return

    elif cards[mid] > target: # target이 작으면 왼쪽 탐색
        end = mid - 1
    else:                    # target이 크면 오른쪽 탐색
        start = mid + 1

    binary_search(target, start, end) # 줄어든 범위를 더 탐색

import sys
n = int(input())
cards = list(map(int,sys.stdin.readline().split()))
cards.sort()
m = int(input())
check = list(map(int,sys.stdin.readline().split()))

for i in check:
    binary_search(i,0,n-1)
