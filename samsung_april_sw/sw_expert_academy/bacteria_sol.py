import sys
sys.stdin = open(r'/Users/kangdaeyoung/Downloads/sample_input (5).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    # 넉넉하게 배열 선언
    brd = [[0]*(M+K*2) for _ in range(N+K*2)]

    input_cells = [list(map(int, input().split())) for _ in range(N)]

    cells = []
    for r in range(N):
        for c in range(M):
            X = input_cells[r][c]
            if X > 0:
                brd[K+r][K+c] = [X, X]
                cells.append([K+r, K+c])

    for time in range(K):
        # 새로 태어나는 세포 저장 공간
        new_cells = []
        for idx, cell in enumerate(cells):
            r, c = cell[0], cell[1]
            # 아직 세포 분열 전
            if brd[r][c][1] > 0:
                brd[r][c][1] -= 1
            # 세포 분열
            elif brd[r][c][1] == 0:
                X = brd[r][c][0]
                for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    if brd[r+dr][c+dc] == 0:
                        new_cells.append([r+dr, c+dc, X])
                # 생명력 감소
                brd[r][c][1] -= 1
                brd[r][c][0] -= 1
            # 생명력 깎이는 중
            else:
                if brd[r][c][0] > 0:
                    brd[r][c][0] -= 1

        # 새로운 태어난 세포 배열에 넣어주기
        for new_cell in new_cells:
            r, c, X = new_cell
            if brd[r][c] == 0:
                brd[r][c] = [X, X]
                cells.append([r, c])
            else:
                # 생명력이 더 센 세포가 자리를 마지막에 차지
                if brd[r][c][0] < X:
                    brd[r][c] = [X, X]

    answer = 0
    # 살아남은 세포 개수 세기
    for r in range(len(brd)):
        for c in range(len(brd[0])):
            if brd[r][c] and brd[r][c][0] > 0:
                answer += 1

    print(f'#{tc} {answer}')