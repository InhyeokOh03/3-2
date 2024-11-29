def can_learn_paths(num_nodes, max_memory, edges):
    edges.sort(key=lambda x: x[2])

    parent = list(range(num_nodes))

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            parent[root2] = root1

    mst_weight = 0
    edge_count = 0

    for node1, node2, weight in edges:
        if find(node1) != find(node2):
            union(node1, node2)
            mst_weight += weight
            edge_count += 1

            if edge_count == num_nodes - 1:
                break

    if edge_count < num_nodes - 1:
        return -1

    return mst_weight if mst_weight <= max_memory else -1

if __name__ == "__main__":
    results = []
    try:
        num_nodes, max_memory = map(int, input().strip().split())
        
        edges = []

        for _ in range(int(num_nodes * (num_nodes - 1) / 2)):
            line = input().strip()
            if not line:
                continue
            node1, node2, distance = map(int, line.split())
            edges.append((node1, node2, distance))

        result = can_learn_paths(num_nodes, max_memory, edges)
        results.append(result)

    except EOFError:
        pass
    print("\n".join(map(str, results)))

# if __name__ == "__main__":
#     results = []
#     empty_count = 0

#     while True:
#         try:
#             case_line = input().strip()

#             if not case_line:
#                 continue
#             num_nodes, max_memory = map(int, input().split())

#             edges = []
#             for _ in range(int(num_nodes * (num_nodes - 1) / 2)):
#                 node1, node2, distance = map(int, input().split())
#                 edges.append((node1, node2, distance))
#             # print(edges)
#             empty_count = 0
#             case_number = case_line.split()[1].strip(":")

#             result = can_learn_paths(num_nodes, max_memory, edges)
#             results.append(f"case {case_number}:\n{result}")
#         except EOFError:
#             break
#     print("\n\n".join(results))



# case 1:
# 4 10
# 0 1 1
# 0 2 5
# 0 3 2
# 1 2 6
# 1 3 4
# 2 3 1

# case 2:
# 3 1
# 0 1 1
# 0 2 1
# 1 2 1

