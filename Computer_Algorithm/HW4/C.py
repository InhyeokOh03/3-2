def bfs(capacity, flow, source, sink, parent):
    visited = [False] * len(capacity)
    queue = [source]
    visited[source] = True

    while queue:
        current = queue.pop(0)

        for neighbor in range(len(capacity[current])):
            if not visited[neighbor] and capacity[current][neighbor] - flow[current][neighbor] > 0:
                parent[neighbor] = current
                visited[neighbor] = True
                queue.append(neighbor)
                if neighbor == sink:
                    return True
    return False


def edmonds_karp(capacity, source, sink):
    n = len(capacity)
    flow = [[0] * n for _ in range(n)]  # 플로우 초기화
    max_flow = 0
    parent = [-1] * n

    while bfs(capacity, flow, source, sink, parent):
        # 증가 경로의 최소 용량 찾기
        path_flow = float('Inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v] - flow[u][v])
            v = u

        # 증가 경로로 플로우 전송
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u

        max_flow += path_flow

    return max_flow


if __name__ == "__main__":
    # 입력 처리
    n, m, k = map(int, input().strip().split())
    capacity = [[0] * n for _ in range(n)]  # 용량 그래프 초기화

    for _ in range(m):
        u, v, w = map(int, input().strip().split())
        if w >= k:  # 길이가 K 이상인 다리는 제거
            continue
        capacity[u][v] += w
        capacity[v][u] += w  # 양방향 다리

    # 최대 유량 계산
    max_flow = edmonds_karp(capacity, 0, n - 1)

    # 결과 출력
    if max_flow == 0:  # 침략을 막을 수 없는 경우
        print(-1)
    else:
        print(max_flow)
