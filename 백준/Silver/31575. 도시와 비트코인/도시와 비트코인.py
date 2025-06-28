import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())     # n=열, m=행
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]

dq = deque([(0, 0)])
visited[0][0] = 1

while dq:
    r, c = dq.popleft()
    # 도착 지점에 닿으면 즉시 종료
    if r == m-1 and c == n-1:
        print("Yes")
        sys.exit(0)
    # 남쪽, 동쪽만 탐색
    for dr, dc in ((1,0), (0,1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < m and 0 <= nc < n \
           and not visited[nr][nc] and graph[nr][nc] == 1:
            visited[nr][nc] = 1
            dq.append((nr, nc))

print("No")
