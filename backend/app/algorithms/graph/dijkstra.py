import heapq
from .bfs import NODES, EDGES

WEIGHTED_GRAPH = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("D", 2), ("E", 3)],
    "C": [("A", 4), ("F", 5)],
    "D": [("B", 2)],
    "E": [("B", 3), ("F", 1)],
    "F": [("C", 5), ("E", 1)],
}


def dijkstra_steps(start="A"):
    steps = []
    dist = {v: float("inf") for v in WEIGHTED_GRAPH}
    dist[start] = 0
    pq = [(0, start)]
    visited = set()

    steps.append({
        "nodes": NODES, "edges": EDGES,
        "visited": [], "current": None, "queue": [start],
        "code_line": 2,
        "text": f"Initialize Dijkstra from {start}. dist[{start}]=0, all others=∞"
    })

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        steps.append({
            "nodes": NODES, "edges": EDGES,
            "visited": list(visited), "current": u, "queue": [x[1] for x in pq],
            "code_line": 7,
            "text": f"Process node {u} (dist={d})"
        })
        for v, w in WEIGHTED_GRAPH[u]:
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
                steps.append({
                    "nodes": NODES, "edges": EDGES,
                    "visited": list(visited), "current": u, "queue": [x[1] for x in pq],
                    "code_line": 11,
                    "text": f"Shorter path to {v} found via {u}: dist[{v}]={new_dist}"
                })

    result = ", ".join(f"{k}={v}" for k, v in sorted(dist.items()))
    steps.append({
        "nodes": NODES, "edges": EDGES,
        "visited": list(visited), "current": None, "queue": [],
        "code_line": 12,
        "text": f"Dijkstra complete! Shortest distances: {result}"
    })
    return steps
