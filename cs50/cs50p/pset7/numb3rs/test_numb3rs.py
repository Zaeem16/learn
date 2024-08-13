from numb3rs import validate


def main():
    test_first_byte()
    test_five_bytes()


def test_first_byte():
    assert validate("1.300.400.500") == False
    assert validate("45....") == False


def test_five_bytes():
    assert validate("1.1.1.1.1") == False
    assert validate("23.31.165.93.100") == False


if __name__ == "__main__":
    main()
