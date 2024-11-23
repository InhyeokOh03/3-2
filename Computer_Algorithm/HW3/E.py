import sys
 
class Graph:
    def __init__(self):
        self.adj_list = {} 
     
    def add_edge(self, x1, y1, x2, y2):
        if (x1, y1) not in self.adj_list:
            self.adj_list[(x1, y1)] = []
        if (x2, y2) not in self.adj_list:
            self.adj_list[(x2, y2)] = []
         
        self.adj_list[(x1, y1)].append((x2, y2))
        self.adj_list[(x2, y2)].append((x1, y1))
     
    def get_neighbors(self, point):
        return self.adj_list.get(point, [])
 
def dfs(point, graph, visited, path, parent=None):
    visited.add(point)
    path.append(point)
    # print(graph.get_neighbors(point))
    if len(graph.get_neighbors(point)) == 2:
        for neighbor in graph.get_neighbors(point):
            if neighbor not in visited:
                if dfs(neighbor, graph, visited, path, point):
                    return True
            elif neighbor != parent:
                path.append(neighbor) 
                return True
     
    path.pop()
    return False
 
def is_valid_polygon(path):
    return len(path) >= 3
 
def is_valid_polygon_path(path, graph):
    path_set = set(path)
    for point in path:
        neighbors = graph.get_neighbors(point)
        if not all(neighbor in path_set for neighbor in neighbors):
            return False
    return True
 
def count(lines):
    graph = Graph()
    points = set()
 
    for (x1, y1, x2, y2) in lines:
        graph.add_edge(x1, y1, x2, y2)
        points.add((x1, y1))
        points.add((x2, y2))
 
    visited = set()
    cycle_count = 0
 
    for point in points:
        if point not in visited:
            path = []
            if dfs(point, graph, visited, path):
                if is_valid_polygon(path) and is_valid_polygon_path(path, graph):
                    cycle_count += 1
                    # print("Valid polygon path:", path)
            else:
                for p in path:
                    visited.add(p)
    return cycle_count
 
if __name__ == "__main__":
    n = int(input().strip())
    lines = []
     
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().strip().split())
        lines.append((x1, y1, x2, y2))
 
    result = count(lines)
    print(result)