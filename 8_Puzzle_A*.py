from queue import PriorityQueue

def astar(graph, start, goal, heuristic):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0 + heuristic[start], 0, start))

    while not priority_queue.empty():
        _, cost, current_node = priority_queue.get()

        if current_node in visited:
            continue

        print("Visiting:", current_node)
        visited.add(current_node)

        if current_node == goal:
            print("Goal reached!")
            break

        for neighbor, neighbor_cost in graph[current_node]:
            if neighbor not in visited:
                priority_queue.put((cost + neighbor_cost + heuristic[neighbor], cost + neighbor_cost, neighbor))
