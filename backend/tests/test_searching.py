import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.algorithms.searching.binary_search import binary_search_steps, linear_search_steps


SAMPLE = [3, 7, 1, 9, 4, 6, 8, 2]


def test_linear_search_found():
    steps = linear_search_steps(SAMPLE, 9)
    found = [s for s in steps if s.get("found", -1) >= 0]
    assert len(found) > 0
    assert SAMPLE[found[-1]["found"]] == 9
    print(f"  linear_search (found): {len(steps)} steps ✓")


def test_linear_search_not_found():
    steps = linear_search_steps(SAMPLE, 99)
    found = [s for s in steps if s.get("found", -1) >= 0]
    assert len(found) == 0
    print(f"  linear_search (not found): {len(steps)} steps ✓")


def test_binary_search_found():
    steps = binary_search_steps(SAMPLE, 7)
    found = [s for s in steps if s.get("found", -1) >= 0]
    assert len(found) > 0
    sorted_arr = sorted(SAMPLE)
    assert sorted_arr[found[-1]["found"]] == 7
    print(f"  binary_search (found): {len(steps)} steps ✓")


def test_binary_search_not_found():
    steps = binary_search_steps(SAMPLE, 50)
    found = [s for s in steps if s.get("found", -1) >= 0]
    assert len(found) == 0
    print(f"  binary_search (not found): {len(steps)} steps ✓")


def test_binary_search_fewer_steps_than_linear():
    large = list(range(1, 101))
    linear_steps = linear_search_steps(large, 99)
    binary_steps = binary_search_steps(large, 99)
    assert len(binary_steps) < len(linear_steps)
    print(f"  binary < linear steps: {len(binary_steps)} vs {len(linear_steps)} ✓")
