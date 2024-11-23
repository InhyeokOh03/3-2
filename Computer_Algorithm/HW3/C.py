import sys

def find_shortest_path(n, e, k, t, edges, bike_nodes):
    graph = [[] for _ in range(n + 1)]
    for a, b, w in edges:
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    dist = [[float('inf')] * 2 for _ in range(n + 1)]
    dist[1][0] = 0

    queue = [(1, 0, 0)]

    while queue:
        # print(queue)
        # print(dist)
        current_node, current_distance, used_bike = queue.pop(0)

        if current_distance > dist[current_node][used_bike]:
            continue
            
        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            # Bike X
            if new_distance < dist[neighbor][0]:
                dist[neighbor][0] = new_distance
                queue.append((neighbor, new_distance, 0))

            # Bike O
            if current_distance >= t and current_node in bike_nodes:
                bike_distance = current_distance + weight / 2  
                if bike_distance < dist[neighbor][1]:
                    dist[neighbor][1] = bike_distance
                    queue.append((neighbor, bike_distance, 1))

    shortest_time = min(dist[n])
    return round(shortest_time) if shortest_time != float('inf') else -1


if __name__ == "__main__":
    # data = ['5 6 2 10\n', '1 2 5\n', '1 3 10\n', '2 3 3\n', '2 4 7\n', '3 5 8\n', '4 5 2\n', '2\n', '4\n']
    n, e, k, t = map(int, input().strip().split())
    
    edges = []
    for _ in range(e):
        a, b, w = map(int, input().strip().split())
        edges.append((a, b, w))

    bike_nodes = []
    for _ in range(k):
        bike_nodes.append(int(input().strip()))

    result = find_shortest_path(n, e, k, t, edges, bike_nodes)
    print(result) 

    # 81.8
