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

    def bfs(self,start,goal,heuristic):
            pq = []
            heapq.heappush(pq,(heuristic[start],start))
            visited = set()
            path = []

            while pq:
                _,current = heapq.heappop(pq)
                if current in visited:
                    continue
                path.append(current)
                visited.add(current)

                if current == goal:
                    return path

                if current in self.graph:
                    for neighbour in self.graph[current]:
                        if neighbour not in visited:
                            heapq.heappush(pq,(heuristic[neighbour],neighbour))
            print("No path found")
            return []

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

print ("Best First Search Algorithm")
print (g.bfs(start,goal,heuristic))
