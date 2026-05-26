from collections import defaultdict

# 격자의 크기 n, 구슬의 개수 m, 시간 t
n, m, t = map(int, input().split())

# n x n 격자 입력 (0-indexed)
a = [list(map(int, input().split())) for _ in range(n)]

# m개의 구슬 시작 위치 입력 후 0-indexed 변환
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] - 1 for pos in marbles]
c = [pos[1] - 1 for pos in marbles]

# 상하좌우 방향 벡터
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 각 구슬의 생존 여부 → 초기: [True, True, True]
alive = [True] * m

# t초 동안 시뮬레이션
for _ in range(t):
    # 동시 이동을 위해 새 위치를 별도 배열에 저장
    new_r = r[:]
    new_c = c[:]

    for i in range(m):
        if not alive[i]:
            continue

        cr, cc = r[i], c[i]

        # 인접한 4방향 중 가장 큰 값을 가진 칸으로 이동
        best_val = -1
        best_r, best_c = cr, cc  # 이동 못하면 현재 위치 유지

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            # 격자를 벗어나지 않는 경우만
            if 0 <= nr < n and 0 <= nc < n:
                val = a[nr][nc]
                # 더 큰 값이면 갱신 (같으면 갱신 안 함 → 상>하>좌>우 우선순위 유지)
                if val > best_val:
                    best_val = val
                    best_r, best_c = nr, nc

        # 새 위치 저장 (아직 r, c 업데이트 X)
        new_r[i] = best_r
        new_c[i] = best_c

    # 모든 구슬 이동 완료 후 충돌 체크
    # 위치별로 묶어서 처리 → 3개 이상 동시 충돌도 전부 제거
    # (쌍으로 비교하면 A-B제거 후 C를 alive 체크로 skip하는 버그 발생)
    pos_count = defaultdict(list)
    for i in range(m):
        if alive[i]:
            pos_count[(new_r[i], new_c[i])].append(i)

    for pos, indices in pos_count.items():
        if len(indices) >= 2:  # 2개 이상이면 전부 제거
            for i in indices:
                alive[i] = False

    # 위치 업데이트
    r = new_r
    c = new_c

# t초 후 살아있는 구슬의 수 출력
cnt = 0
for i in range(len(alive)):
    if alive[i]:
        cnt += 1
print(cnt)