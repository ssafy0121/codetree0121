n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 합이 최대
max_sum = 0

for r in range(n):
    for c in range(m):
   
        # 블럭 2: 가로 o o o
        if c + 2 < m:
            total = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            if total > max_sum:
                max_sum = total
        
        # 세로 일자:  o
        #            o
        #            o
        if r + 2 < n:
            total = grid[r][c] + grid[r+1][c] + grid[r+2][c]
            if total > max_sum:
                max_sum = total



        # 블록 1: L자 (4가지 회전)
        # o
        # o o
        if r + 1 < n and c + 1 < m:
            total = grid[r][c] + grid[r+1][c] + grid[r+1][c+1]
            if total > max_sum:
                max_sum = total
        
        #   o
        # o o
        if r + 1 < n and c - 1 >= 0:
            total = grid[r][c] + grid[r+1][c] + grid[r+1][c-1]
            if total > max_sum:
                max_sum = total
        
        # oo
        # o
        if r + 1 < n and c + 1 < m:
            total = grid[r][c] + grid[r][c+1] + grid[r+1][c]
            if total > max_sum:
                max_sum = total
        
        # oo
        #  o
        if r + 1 < n and c + 1 < m:
            total = grid[r][c] + grid[r][c+1] + grid[r+1][c+1]
            if total > max_sum:
                max_sum = total


print(max_sum)