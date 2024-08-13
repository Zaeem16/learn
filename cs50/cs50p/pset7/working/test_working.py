from working import convert
import pytest


def main():
    test_off_hour()
    test_off_minutes()
    test_to()
    test_out_of_range()


def test_off_hour():
    assert convert("9:00 AM to 9 PM") == "09:00 to 21:00"
    assert convert("3:00 PM to 5:53 PM") == "15:00 to 17:53"

def test_off_minutes():
    assert convert("3:00 PM to 5:53 PM") == "15:00 to 17:53"
    assert convert("12:30 AM to 8 AM") == "00:30 to 08:00"

def test_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM from 5 PM")

def test_out_of_range():
    with pytest.raises(ValueError):
        convert("13:21 PM to 1:00 PM")
    with pytest.raises(ValueError):
        convert("11:70 AM to 2:30 PM")
