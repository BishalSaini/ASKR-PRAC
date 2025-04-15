import heapq
class Graph:
    def __init__(self):
        self.graph = {}
    def add_Edge (self,start,end):
        if start not in self.graph:
            self.graph[start]=[]
        self.graph[start].append(end)
    def greedy(self,start,goal,heuristic):
        current = start
        path = [current]
        while current != goal:
            if current not in self.graph:
                print("No path found")
                return []
            current = min (self.graph[current],key=lambda node: heuristic[node])
            path.append(current)
        return path

g = Graph()
g.add_Edge("A","B")
g.add_Edge("A","C")
g.add_Edge("B","D")
g.add_Edge("C","D")
g.add_Edge("C","E")
g.add_Edge("D","E")

heuristic ={
    "A":7, "B":6, "C":2, "D":1, "E":0
    }

start = "A"
goal = "E"
print("Greedy algorithm:")
print(g.greedy(start,goal,heuristic))
