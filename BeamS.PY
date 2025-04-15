import heapq

def beam_search(start_state, goal_test, successors, beam_width):
    # Initialize the beam with the start state
    beam = [(start_state, 0)] # (state, cost)

    while beam:
        # List of nodes at the current level
        next_beam = []

        for state, cost in beam:
            if goal_test(state):
                return state

            # Get the successor states and their costs
            successors_list = successors(state)

            for successor, successor_cost in successors_list:
                total_cost = cost + successor_cost
                next_beam.append((successor, total_cost))

        # Keep the top `beam_width` nodes from the next level
        beam = heapq.nsmallest(beam_width, next_beam, key=lambda x: x[1])

    return None # Goal is not reachable

# Example usage
def successors(state):
    # Define how to get the next state from current state
    return [(state + 1, 1), (state * 2, 1)]

def goal_test(state):
    return state == 10

# Beam search with beam width 2
result = beam_search(1, goal_test, successors, beam_width=2)
print(f"Found goal state: {result}")
