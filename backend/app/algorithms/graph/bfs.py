from collections import deque

SAMPLE_GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

NODES = list(SAMPLE_GRAPH.keys())
EDGES = [["A","B"],["A","C"],["B","D"],["B","E"],["C","F"],["E","F"]]


def bfs_steps(start="A"):
    steps = []
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    steps.append({
        "nodes": NODES, "edges": EDGES,
        "visited": [], "current": None, "queue": [start],
        "code_line": 4, "text": f"Initialize BFS from node {start}. Add to queue."
    })

    while queue:
        node = queue.popleft()
        order.append(node)
        steps.append({
            "nodes": NODES, "edges": EDGES,
            "visited": list(visited), "current": node, "queue": list(queue),
            "code_line": 8,
            "text": f"Dequeue {node} — visit it. Order so far: [{', '.join(order)}]"
        })
        for neighbor in SAMPLE_GRAPH[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                steps.append({
                    "nodes": NODES, "edges": EDGES,
                    "visited": list(visited), "current": node, "queue": list(queue),
                    "code_line": 12,
                    "text": f"Neighbor {neighbor} not visited — enqueue it"
                })

    steps.append({
        "nodes": NODES, "edges": EDGES,
        "visited": list(visited), "current": None, "queue": [],
        "code_line": 13,
        "text": f"BFS complete! Traversal order: {' → '.join(order)}"
    })
    return steps
