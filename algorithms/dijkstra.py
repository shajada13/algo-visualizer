# =============================================================================
# algorithms/dijkstra.py
# ----------------------
# Dijkstra's Algorithm — Weighted Grid Pathfinding।
#
# কিভাবে কাজ করে:
#   - Priority Queue (Min-Heap) ব্যবহার করে।
#   - সবসময় সবচেয়ে কম cost এর node প্রথমে process করে।
#   - প্রতিটি cell এর "distance" track করে।
#   - Weighted graph এ সবচেয়ে কম cost এর path দেয়।
#
# BFS vs Dijkstra:
#   BFS — সব edge এর weight সমান ধরে
#   Dijkstra — weighted edge handle করতে পারে
#
# Time:  O(E log V)
# Space: O(V)
# =============================================================================

import heapq


def dijkstra(grid, start, end):
    """
    Dijkstra pathfinding generator।
    grid: 2D list of strings
    start, end: (row, col) tuples
    """
    rows, cols = len(grid), len(grid[0])
    dist    = {start: 0}   # প্রতিটি cell এর shortest distance
    parent  = {}           # path reconstruct করার জন্য
    heap    = [(0, start)] # (distance, cell) — min-heap
    visited = set()

    yield {
        "grid_updates": {start: "frontier"},
        "done": False, "found": False, "stat": None,
        "info": f"Dijkstra from {start} — initial distance = 0"
    }

    while heap:
        d, cur = heapq.heappop(heap)  # সবচেয়ে কম distance এর cell

        if cur in visited:
            continue  # আগেই process হয়েছে
        visited.add(cur)

        if cur == end:
            # গন্তব্যে পৌঁছে গেছি!
            path = []
            node = end
            while node != start:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()

            updates = {c: "path" for c in path if c not in (start, end)}
            yield {
                "grid_updates": updates,
                "done": True, "found": True, "path": path,
                "stat": "path",
                "info": f"Shortest path found! Cost={d}, Length={len(path)}"
            }
            return

        r, c = cur
        # চারদিকের প্রতিবেশী cells — সব edge এর weight = 10
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            nb = (nr, nc)

            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] != "wall"
                    and nb not in visited):
                new_dist = d + 10  # edge weight = 10

                if new_dist < dist.get(nb, float("inf")):
                    dist[nb]   = new_dist
                    parent[nb] = cur
                    heapq.heappush(heap, (new_dist, nb))
                    yield {
                        "grid_updates": {nb: "frontier" if nb != end else "end",
                                         cur: "visited"},
                        "done": False, "found": False, "stat": "visit",
                        "info": f"Updated dist[({nr},{nc})] = {new_dist}"
                    }

        if cur != start:
            yield {
                "grid_updates": {cur: "visited"},
                "done": False, "found": False, "stat": None,
                "info": f"Settled ({r},{c}) with distance={d}"
            }

    yield {
        "grid_updates": {}, "done": True, "found": False,
        "stat": None, "info": "No path found!"
    }
