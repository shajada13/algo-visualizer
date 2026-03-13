import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.algorithms.sorting.bubble_sort import bubble_sort_steps
from app.algorithms.sorting.insertion_sort import insertion_sort_steps, selection_sort_steps
from app.algorithms.sorting.merge_sort import merge_sort_steps
from app.algorithms.sorting.quick_sort import quick_sort_steps


SAMPLE = [5, 3, 8, 1, 9, 2, 7, 4]
EXPECTED_SORTED = sorted(SAMPLE)


def final_array(steps):
    return steps[-1]["array"]


def test_bubble_sort():
    steps = bubble_sort_steps(SAMPLE)
    assert final_array(steps) == EXPECTED_SORTED
    assert len(steps) > 0
    print(f"  bubble_sort: {len(steps)} steps ✓")


def test_insertion_sort():
    steps = insertion_sort_steps(SAMPLE)
    assert final_array(steps) == EXPECTED_SORTED
    print(f"  insertion_sort: {len(steps)} steps ✓")


def test_selection_sort():
    steps = selection_sort_steps(SAMPLE)
    assert final_array(steps) == EXPECTED_SORTED
    print(f"  selection_sort: {len(steps)} steps ✓")


def test_merge_sort():
    steps = merge_sort_steps(SAMPLE)
    assert final_array(steps) == EXPECTED_SORTED
    print(f"  merge_sort: {len(steps)} steps ✓")


def test_quick_sort():
    steps = quick_sort_steps(SAMPLE)
    assert final_array(steps) == EXPECTED_SORTED
    print(f"  quick_sort: {len(steps)} steps ✓")


def test_already_sorted():
    arr = [1, 2, 3, 4, 5]
    assert final_array(bubble_sort_steps(arr)) == arr


def test_single_element():
    arr = [42]
    steps = bubble_sort_steps(arr)
    assert final_array(steps) == [42]


def test_two_elements_reversed():
    arr = [9, 1]
    assert final_array(bubble_sort_steps(arr)) == [1, 9]
