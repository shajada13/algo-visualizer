import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.algorithms.graph.bfs import bfs_steps, NODES
from app.algorithms.graph.dfs import dfs_steps
from app.algorithms.graph.dijkstra import dijkstra_steps


def all_nodes_visited(steps):
    final = steps[-1]
    return set(final.get("visited", [])) == set(NODES)


def test_bfs_visits_all_nodes():
    steps = bfs_steps("A")
    assert all_nodes_visited(steps)
    print(f"  BFS: {len(steps)} steps, all nodes visited ✓")


def test_bfs_starts_with_source():
    steps = bfs_steps("A")
    first_visit = next(s for s in steps if s.get("current"))
    assert first_visit["current"] == "A"
    print(f"  BFS starts at A ✓")


def test_dfs_visits_all_nodes():
    steps = dfs_steps("A")
    assert all_nodes_visited(steps)
    print(f"  DFS: {len(steps)} steps, all nodes visited ✓")


def test_dijkstra_visits_all_nodes():
    steps = dijkstra_steps("A")
    assert all_nodes_visited(steps)
    print(f"  Dijkstra: {len(steps)} steps ✓")


def test_steps_have_required_fields():
    for fn in [bfs_steps, dfs_steps, dijkstra_steps]:
        steps = fn("A")
        for s in steps:
            assert "nodes" in s
            assert "visited" in s
            assert "text" in s
    print("  All graph steps have required fields ✓")
