from collections import deque

def make_one_bfs(real_n):
    # BFS를 위한 큐 초기화: (현재 값, 연산 횟수)
    queue = deque([(1, 0)])
    visited = set()  # 방문한 상태 저장
    
    while queue:
        current, count = queue.popleft()
        
        # 목표 숫자에 도달하면 연산 횟수 반환
        if current == real_n:
            return count
        
        # 방문한 숫자라면 스킵
        if current in visited:
            continue
        visited.add(current)
        
        # 다음 가능한 연산 추가 (3배, 2배, +1)
        if current * 3 <= real_n:
            queue.append((current * 3, count + 1))
        if current * 2 <= real_n:
            queue.append((current * 2, count + 1))
        if current + 1 <= real_n:
            queue.append((current + 1, count + 1))

# 입력
real_n = int(input().strip())
if real_n == 1:
    print(0)
else:
    # 결과 출력
    print(make_one_bfs(real_n))
