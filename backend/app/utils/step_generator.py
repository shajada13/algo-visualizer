"""
Utility helpers for building animation step payloads.
"""


def make_step(array, active=-1, compared=-1, sorted_indices=None, found=-1,
              code_line=0, text="", **extras):
    """Build a standardized animation step dict."""
    step = {
        "array": list(array),
        "active": active,
        "compared": compared,
        "sorted": sorted_indices or [],
        "found": found,
        "code_line": code_line,
        "text": text,
    }
    step.update(extras)
    return step


def make_graph_step(nodes, edges, visited, current, queue, code_line, text):
    """Build a graph animation step dict."""
    return {
        "nodes": nodes,
        "edges": edges,
        "visited": list(visited) if not isinstance(visited, list) else visited,
        "current": current,
        "queue": list(queue),
        "code_line": code_line,
        "text": text,
    }
