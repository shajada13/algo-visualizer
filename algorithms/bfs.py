# =============================================================================
# algorithms/bfs.py
# -----------------
# BFS (Breadth-First Search) — Grid Pathfinding।
#
# কিভাবে কাজ করে:
#   - একটি Queue ব্যবহার করে।
#   - শুরুর cell থেকে শুরু করে চারদিকের cells explore করে।
#   - Level by level explore করে — তাই সবচেয়ে কম step এর path দেয়।
#   - Unweighted grid এ সবচেয়ে ছোট path (shortest path) নিশ্চিত করে।
#
# Time:  O(V + E) — V = cells, E = edges
# Space: O(V)
# =============================================================================

from collections import deque


def bfs(grid, start, end):
    """
    BFS pathfinding generator।
    grid: 2D list of strings ('empty', 'wall', 'start', 'end')
    start: (row, col) tuple
    end: (row, col) tuple
    """
    rows, cols = len(grid), len(grid[0])
    visited = set([start])  # কোন cells গুলো visit হয়েছে
    parent  = {}            # path reconstruct করার জন্য
    queue   = deque([start])

    yield {
        "grid_updates": {start: "frontier"},
        "done": False, "found": False, "stat": None,
        "info": f"BFS starting from {start} — adding to queue"
    }

    while queue:
        cur = queue.popleft()  # Queue এর সামনে থেকে নাও

        if cur == end:
            # গন্তব্যে পৌঁছে গেছি! Path reconstruct করছি।
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
                "info": f"Path found! Length: {len(path)} cells"
            }
            return

        r, c = cur
        # চারদিকের প্রতিবেশী cells দেখছি (উপর, নিচ, বাম, ডান)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            nb = (nr, nc)

            if (0 <= nr < rows and 0 <= nc < cols
                    and nb not in visited
                    and grid[nr][nc] != "wall"):
                visited.add(nb)
                parent[nb] = cur
                queue.append(nb)
                yield {
                    "grid_updates": {nb: "frontier" if nb != end else "end",
                                     cur: "visited"},
                    "done": False, "found": False, "stat": "visit",
                    "info": f"Exploring ({nr},{nc}) — queue size: {len(queue)}"
                }

        if cur != start:
            yield {
                "grid_updates": {cur: "visited"},
                "done": False, "found": False, "stat": None,
                "info": f"Visited ({r},{c})"
            }

    # Queue শেষ হয়ে গেছে — path পাওয়া যায়নি
    yield {
        "grid_updates": {}, "done": True, "found": False,
        "stat": None, "info": "No path found! Destination is unreachable."
    }
