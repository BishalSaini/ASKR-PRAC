class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, node, neighbor):
        if node not in self.edges:
            self.edges[node] = []
        self.edges[node].append(neighbor)

    def get_neighbors(self, node):
        return self.edges.get(node, [])

def depth_limited_search(graph, start, goal, limit):
    if start == goal:
        return [start]
    if limit <= 0:
        return None
    for neighbor in graph.get_neighbors(start):
        path = depth_limited_search(graph, neighbor, goal, limit - 1)
        if path:
            return [start] + path
    return None

def iterative_deepening_search(graph, start, goal):
    depth = 0
    while True:
        path = depth_limited_search(graph, start, goal, depth)
        if path:
            return path
        depth += 1

graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')
graph.add_edge('D', 'F')

print("IDS Path:", iterative_deepening_search(graph, 'A', 'F'))
