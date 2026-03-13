from .bfs import SAMPLE_GRAPH, NODES, EDGES


def dfs_steps(start="A"):
    steps = []
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        order.append(node)
        steps.append({
            "nodes": NODES, "edges": EDGES,
            "visited": list(visited), "current": node, "queue": [],
            "code_line": 3,
            "text": f"Visit {node}. DFS order: [{', '.join(order)}]"
        })
        for neighbor in SAMPLE_GRAPH[node]:
            if neighbor not in visited:
                steps.append({
                    "nodes": NODES, "edges": EDGES,
                    "visited": list(visited), "current": node, "queue": [],
                    "code_line": 5,
                    "text": f"Exploring edge {node} → {neighbor}"
                })
                dfs(neighbor)

    dfs(start)
    steps.append({
        "nodes": NODES, "edges": EDGES,
        "visited": list(visited), "current": None, "queue": [],
        "code_line": 9,
        "text": f"DFS complete! Traversal order: {' → '.join(order)}"
    })
    return steps
