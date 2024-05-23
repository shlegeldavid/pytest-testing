from funcy import compact
import pytest


@pytest.fixture
def coll():
    return ['One', True, 3, [1, 'hexlet', [0]], 'cat', {}, '', [], False]


def test_compact(coll):
    result = compact(coll)
    assert result == ['One', True, 3, [1, 'hexlet', [0]], 'cat']

def test_fill_empty_coll(fill):
    collection = []
    fill(collection, '*', 1, 3)
    assert collection == []


def test_fill_full_change(collection, fill):
    fill(collection, 1)
    assert collection == [1, 1, 1, 1]


def test_fill_high_end(collection, fill):
    fill(collection, '*', 0, 10)
    assert collection == ['*', '*', '*', '*']


def fill(coll, value, begin=0, end=len(coll)):
    if coll == []:
        return []
    if begin > len(coll):
        return coll
    if begin < 0:
        return coll
    if end < 0:
        return coll
    if end > len(coll):
        end = len(coll)
    