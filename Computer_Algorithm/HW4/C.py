def main(n, k, graph):
    INF = 10**9 

    g = [[] for _ in range(n)]

    def add_edge(u, v, cap):
        g[u].append([v, cap, len(g[v])])
        g[v].append([u, 0, len(g[u]) - 1])

    visited = [False]*n
    visited[0] = True
    queue = [0]
    front = 0
    while front < len(queue):
        u = queue[front]
        front += 1
        for v, c in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    if not visited[n-1]:
        return 0

    added = set() 
    for u in range(n):
        for v, c in graph[u]:
            edge_key = (min(u,v), max(u,v))
            if edge_key not in added:
                added.add(edge_key)
                cap = c if c < k else INF
                add_edge(u, v, cap)
                add_edge(v, u, cap)

    def bfs():
        level = [-1]*n
        level[0] = 0
        q = [0]
        front = 0
        while front < len(q):
            u = q[front]
            front += 1
            for i, (vv, cap, rev) in enumerate(g[u]):
                if cap > 0 and level[vv] < 0:
                    level[vv] = level[u] + 1
                    q.append(vv)
        return level

    def send_flow(u, flow, level, it):
        if u == n-1:
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
        if level[n-1] < 0:
            break
        it = [0]*n
        while True:
            f = send_flow(0, INF, level, it)
            if f <= 0:
                break
            total_flow += f

    if total_flow >= INF:
        return -1
    return total_flow


if __name__ == "__main__":
    n, m, k = map(int, input().strip().split())
    graph = {i: [] for i in range(n)}
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    result = main(n, k, graph)
    print(result)
