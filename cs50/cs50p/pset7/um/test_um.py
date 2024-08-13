from um import count

def main():
    test_um_as_sub_str()
    test_um_spaces()
    test_um_CASE_insensitive()


def test_um_as_sub_str():
    assert count("YUMMY GUMMY") == 0
    assert count("Sum of num + num = NUM") == 0

def test_um_spaces():
    assert count("UM, um.") == 2
    assert count(":um: 'UM'") == 2

def test_um_CASE_insensitive():
    assert count("UM UM UM UM um ") == 5
    assert count("Um uM {UM} um") == 4



if __name__ == "__main__":
    main()
