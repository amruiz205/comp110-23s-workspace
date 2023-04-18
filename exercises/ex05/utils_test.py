"""List utility functions!"""
__author__ = "730599859"

from exercises.ex05.utils import only_evens, concat, sub 


def test_only_evens_2() -> None:
    """Test the only_evens function!"""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_3() -> None:
    """Test the only_evens function!"""
    x: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(x) == [2, 4, 6]


def test_only_evens_three_terms() -> None:
    """Test the only_evens function!"""
    x: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(x) == [2, 4, 6]


def test_concat_empty() -> None:
    """Test the concat function with an empty list."""
    x: list[int] = []
    
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_5_terms() -> None:
    """Test the concat function."""
    x: list[int] = [1, 2]
   
    y: list[int] = [3, 4, 5]
    assert concat(x, y) == [1, 2, 3, 4, 5]


def test_concat_7terms() -> None:
    """Test the concat function."""
    x: list[int] = [1, 2, 3, 4]
    y: list[int] = [5, 6, 7]
    
    assert concat(x, y) == [1, 2, 3, 4, 5, 6, 7]


def test_sub_empty() -> None:
    """Test the sub function for an empty list."""
    x: list[int] = [1, 2, 3, 4]
    
    y: int = 1
    z: int = 0
    assert sub(x, y, z) == []


def test_sub_two_terms() -> None:
    """Test the sub function for two terms."""
    x: list[int] = [1, 2, 3, 4]
    y: int = 1

    z: int = 3
    assert sub(x, y, z) == [2, 3]


def test_sub_three_terms() -> None:
    """Test the sub function for 3 terms."""
    x: list[int] = [1, 2, 3, 4]
    y: int = 0
    z: int = 3

    assert sub(x, y, z) == [1, 2, 3]
