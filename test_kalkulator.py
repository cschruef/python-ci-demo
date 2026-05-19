import pytest

from kalkulator import addiere, teile


def test_addiere_gibt_summe_zurueck():
    assert addiere(2, 3) == 5


def test_teile_normal():
    assert teile(10, 2) == 5


def test_teile_durch_null_wirft_fehler():
    with pytest.raises(ValueError):
        teile(10, 0)