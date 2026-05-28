# 1이상 100이하의 숫자 n
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.

# 배열 인덱스는 0부터 시작이니까 -1
r -= 1
c -= 1

# (r,c)
k = grid[r][c]

# 폭발할 칸 
boom = [[False] * n for _ in range(n)]

# 자기 자신
boom[r][c] = True


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 4방향
for d in range(4):
    for dist in range(1, k): 
        nr = r + dr[d] * dist
        nc = c + dc[d] * dist
        # 격자 범위
        if 0 <= nr < n and 0 <= nc < n:
            boom[nr][nc] = True


# 폭발한 칸은 0으로 변경
for i in range(n):
    for j in range(n):
        if boom[i][j]:
            grid[i][j] = 0


# 중력
for j in range(n):
    # 열에서 0이 아닌 값만
    col = []
    for i in range(n):       
        if grid[i][j] != 0:
            col.append(grid[i][j])
    # 위쪽은 0으로 채우고, 아래쪽에 숫자 배치
    zeros = [0] * (n - len(col))
    new_col = zeros + col


    # 앞에서 한 것들 격자에 반영
    for i in range(n):
        grid[i][j] = new_col[i]



# 각 행에 해당하는 N개의 숫자를 공백을 사이에 두고 출력
for col in grid:
    print(*col)