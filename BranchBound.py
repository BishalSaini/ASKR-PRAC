import heapq
def branch_and_bound(start_state, goal_test, successors, heuristic):
    # Priority queue for states to be explored
    queue = [(0 + heuristic(start_state), 0, start_state)]# (cost + heuristic, cost, state)
    visited = set()
    while queue:
        _, cost, state = heapq.heappop(queue)
        #print(cost, state)
        if goal_test(state):
            return state
        if state in visited:
            continue
        visited.add(state)
        #print(visited)
        # Explore successor states
        for successor, step_cost in successors(state):
            total_cost = cost + step_cost
            #print(total_cost)
            heapq.heappush(queue, (total_cost + heuristic(successor), total_cost, successor))
            #print(queue)
    return None # Goal is not reachable

# Example usage
def successors(state):
    # Define how to get the next state from current state
    #print((state + 1, 1), (state * 2, 1))
    return [(state + 1, 1), (state * 2, 1)]

def goal_test(state):
    #print(state==10)
    return state == 10

def heuristic(state):
    # Heuristic: Simple difference to goal (straight-line distance)
    #print (abs(state - 10))
    return abs(state - 10)

# Branch and Bound search
result = branch_and_bound(1, goal_test, successors, heuristic)
print(f"Found goal state: {result}")
