from fuel import convert, gauge
import pytest

def main():
    test_int()
    test_Value_Error()
    test_Zero_Division()
    test_percent()
    test_E()
    test_F()

def test_int():
    assert convert("1/2") == 50
    assert convert("31/40") == 78

def test_Value_Error():
    with pytest.raises(ValueError):
        convert("40/31")
        convert("70/40")

def test_Zero_Division():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
        convert("0/0")

def test_percent():
    assert gauge(convert("23/41")) == "56%"
    assert gauge(convert("15/30")) == "50%"

def test_E():
    assert gauge(convert("1/100")) == "E"
    assert gauge(convert("3/421")) == "E"

def test_F():
    assert gauge(convert("37/37")) == "F"
    assert gauge(convert("99/100")) == "F"

