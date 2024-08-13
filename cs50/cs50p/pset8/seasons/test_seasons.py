from seasons import main, Birthday
import pytest

def test_calculate_difference_valid_date():
    birthday = Birthday("2008-10-26")
    result = birthday.calculate_difference()
    expected = "Eight million, two hundred sixty-two thousand, seven hundred twenty minutes"
    assert result == expected

def test_calculate_difference_invalid_date():
    with pytest.raises(SystemExit) as e:
        birthday = Birthday("February 6th, 1998")
        assert birthday.calculate_difference() == "Invalid date"
def test_main():
    birthday = Birthday("1990-12-30")
    assert birthday.calculate_difference() == "Seventeen million, six hundred thirty-seven thousand, one hundred twenty minutes"


if __name__ == "__main__":
    pytest.main()
