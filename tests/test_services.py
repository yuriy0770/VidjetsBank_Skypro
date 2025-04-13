
import pytest

from src.services import simple_search

from tests.conftest import data1

def test_simple(data):
    assert data == simple_search('Супермаркеты')


def test_simple7(data1):
    assert data1 == f"Не правильно передан параметр"


def test_simple1(data):
    assert data != simple_search('    ')


@pytest.mark.parametrize("q", [('Супермаркеты'),
                               ("Фастфуд")])
def test_simple2(q):
    assert isinstance(simple_search(q), str)


@pytest.mark.parametrize("q", [('          '),
                               ("!!!!!!"),
                               ("ugiugiugugu")])
def test_simple3(q):
    assert simple_search(q) == '[]'
