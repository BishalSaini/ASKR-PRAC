import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))  # (cost, node, path)
    visited = set()

    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == goal:
            return path, cost

        for neighbor, edge_cost in graph.get_neighbors(current_node):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))

    return None, float('inf')  # Return None if no path is found

class WeightedGraph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, node, neighbor, cost):
        if node not in self.edges:
            self.edges[node] = []
        self.edges[node].append((neighbor, cost))

    def get_neighbors(self, node):
        return self.edges.get(node, [])

weighted_graph = WeightedGraph()
weighted_graph.add_edge('A', 'B', 1)
weighted_graph.add_edge('A', 'C', 4)
weighted_graph.add_edge('B', 'D', 2)
weighted_graph.add_edge('C', 'E', 1)
weighted_graph.add_edge('D', 'F', 5)
weighted_graph.add_edge('E', 'F', 1)

path, cost = uniform_cost_search(weighted_graph, 'A', 'F')
print("UCS Path:", path, "with cost:", cost)
