# =============================================================================
# algorithms/dfs.py
# Guide focus: Show depth traversal, backtracking
# Visualization: stack-like path — গভীরে যাচ্ছে, dead end এ ফিরে আসছে
# Time: O(V + E) | Space: O(V)
# =============================================================================

def dfs(grid, start, end):
    """
    DFS pathfinding generator।
    grid: 2D list of strings ('empty', 'wall', 'start', 'end')
    start: (row, col) tuple
    end: (row, col) tuple
    """
    rows, cols = len(grid), len(grid[0])
    visited = set()
    parent  = {}
    # Stack — DFS এর মূল data structure
    stack   = [start]
    # Current active path (backtracking দেখানোর জন্য)
    active_path = set()

    yield {
        "grid_updates": {start: "frontier"},
        "done": False, "found": False, "stat": None,
        "info": f"DFS starting from {start} — pushing to stack"
    }

    while stack:
        cur = stack.pop()   # Stack এর উপর থেকে নাও (LIFO)

        if cur in visited:
            continue

        visited.add(cur)
        active_path.add(cur)

        r, c = cur

        # Backtracking detect করি — যদি cur এর parent এর neighbour না হয়
        if cur in parent:
            p = parent[cur]
            pr, pc = p
            # Active path trim করি যদি দরকার হয়
            if abs(r - pr) + abs(c - pc) > 1:
                active_path = {cur}

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
                "info": f"Path found via DFS! Length: {len(path)} cells"
            }
            return

        # চারদিকের প্রতিবেশী — DFS এর জন্য reverse order (নিচ → ডান → উপর → বাম)
        # এতে visualization এ depth-first movement স্পষ্ট বোঝা যায়
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            nb = (nr, nc)

            if (0 <= nr < rows and 0 <= nc < cols
                    and nb not in visited
                    and grid[nr][nc] != "wall"):
                parent[nb] = cur
                stack.append(nb)
                yield {
                    "grid_updates": {nb: "frontier", cur: "visited"},
                    "done": False, "found": False, "stat": "visit",
                    "info": f"DFS: going deeper → ({nr},{nc}) | stack depth: {len(stack)}"
                }

        if cur != start:
            # Backtracking step — dead end এ ফিরে আসছি
            is_dead_end = not any(
                (0 <= r+dr < rows and 0 <= c+dc < cols
                 and (r+dr, c+dc) not in visited
                 and grid[r+dr][c+dc] != "wall")
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]
            )
            if is_dead_end:
                yield {
                    "grid_updates": {cur: "visited"},
                    "done": False, "found": False, "stat": None,
                    "info": f"Dead end at ({r},{c}) — backtracking..."
                }
            else:
                yield {
                    "grid_updates": {cur: "visited"},
                    "done": False, "found": False, "stat": None,
                    "info": f"Visited ({r},{c})"
                }

    yield {
        "grid_updates": {}, "done": True, "found": False,
        "stat": None, "info": "No path found! Destination is unreachable."
    }
