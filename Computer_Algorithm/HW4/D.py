import sys
input = sys.stdin.readline

INF = 10**9

def main(n, m, sx, sy, tx, ty, obstacles):
    def node_in(x, y):
        return (x * (n + 1) + y) * 2

    def node_out(x, y):
        return (x * (n + 1) + y) * 2 + 1

    def valid(x, y):
        return 0 <= x <= n and 0 <= y <= n

    is_obs = [[False] * (n + 1) for _ in range(n + 1)]
    for (ox, oy) in obstacles:
        if 0 <= ox <= n and 0 <= oy <= n:
            is_obs[ox][oy] = True

    total_nodes = (n + 1) * (n + 1) * 2 + 2
    S = (n + 1) * (n + 1) * 2
    T = (n + 1) * (n + 1) * 2 + 1

    g = [[] for _ in range(total_nodes)]

    def add_edge(u, v, cap):
        g[u].append([v, cap, len(g[v])])
        g[v].append([u, 0, len(g[u]) - 1])

    for x in range(n + 1):
        for y in range(n + 1):
            if is_obs[x][y]:
                continue
            vin = node_in(x, y)
            vout = node_out(x, y)
            if x == sx and y == sy:
                add_edge(vin, vout, INF)
                add_edge(S, vin, INF)
            elif x == tx and y == ty:
                add_edge(vin, vout, INF)
                add_edge(vout, T, INF)
            else:
                add_edge(vin, vout, 1)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for x in range(n + 1):
        for y in range(n + 1):
            if is_obs[x][y]:
                continue
            uin = node_in(x, y)
            uout = node_out(x, y)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if valid(nx, ny) and not is_obs[nx][ny]:
                    vin = node_in(nx, ny)
                    add_edge(uout, vin, INF)

    def bfs():
        level = [-1] * total_nodes
        level[S] = 0
        queue = [S]
        f = 0
        while f < len(queue):
            u = queue[f]
            f += 1
            for i, (v, cap, rev) in enumerate(g[u]):
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level

    def send_flow(u, flow, level, it):
        if u == T:
            return flow
        while it[u] < len(g[u]):
            v, cap, rev = g[u][it[u]]
            if cap > 0 and level[v] == level[u] + 1:
                curr_flow = min(flow, cap)
                temp = send_flow(v, curr_flow, level, it)
                if temp > 0:
                    g[u][it[u]][1] -= temp
                    g[v][rev][1] += temp
                    return temp
            it[u] += 1
        return 0

    total_flow = 0
    while True:
        level = bfs()
        if level[T] < 0:
            break
        it = [0] * total_nodes
        while True:
            f = send_flow(S, INF, level, it)
            if f <= 0:
                break
            total_flow += f

    if total_flow >= INF:
        return -1
    else:
        return total_flow


if __name__ == "__main__":
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    obstacles = set(tuple(map(int, input().split())) for _ in range(m))

    ans = main(n, m, x1, y1, x2, y2, obstacles)
    print(ans)
