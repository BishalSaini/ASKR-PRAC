import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g # cost from start to node
        self.h = h # heuristic estimated cost from node to goal
        self.f = g + h # total cost (f = g + h)

    def __lt__(self, other):
        # This ensures that heapq can compare nodes based on their f value
        return self.f < other.f

def a_star_algorithm(start, goal, graph, heuristic):
    open_list = []
    closed_list = set()

    # Create the start node
    start_node = Node(start, None, 0, heuristic[start])
    heapq.heappush(open_list, start_node)
    i=0
    while open_list:
        current_node = heapq.heappop(open_list)
        #print(current_node.name)
        # If we reach the goal, reconstruct the path
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1] # Reverse the path to get the correct order

        closed_list.add(current_node.name)

        # Explore the neighbors
        for neighbor, cost in graph[current_node.name]:
            #print(neighbor,cost)
            if neighbor in closed_list:
                continue
            #print(current_node.g," ",cost)
            g_cost = current_node.g + cost
            #print(g_cost)
            h_cost = heuristic[neighbor]
            #print(h_cost)
            neighbor_node = Node(neighbor, current_node, g_cost, h_cost)

            # Check if the neighbor is already in the open list
            if not any(open_node.name == neighbor and open_node.f <= neighbor_node.f for open_node in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None # No path found

# Example graph with costs (adjacency list representation)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 2)],
    'C': [('A', 3), ('D', 1)],
    'D': [('B', 2), ('C', 1)],
}

# Heuristic values (straight-line distance to goal)
heuristic = {
    'A': 4,
    'B': 2,
    'C': 1,
    'D': 0,
}

start = 'A'
goal = 'D'

# Find the path from start to goal
path = a_star_algorithm(start, goal, graph, heuristic)

if path:
    print("Path found:", path)
else:
    print("No path found")
