from plates import is_valid

def main():
    test_alphabet()
    test_lenght()
    test_number_placement()
    test_zero_placement()
    test_alphanumeric()

def test_alphabet():
    assert is_valid("123go") == False
    assert is_valid("50") == False

def test_lenght():
    assert is_valid("gozaeem") == False
    assert is_valid("go") == True
    assert is_valid("C") == False

def test_number_placement():
    assert is_valid("HI2all") == False
    assert is_valid("HIto3") == True
    assert is_valid("469see") == False

def test_zero_placement():
    assert is_valid("go0123") == False
    assert is_valid("go1230") == True

def test_alphanumeric():
    assert is_valid("pys10!") == False
    assert is_valid("CSgo??") == False
    assert is_valid("go 5 ") == False
    assert is_valid("hello,") == False
    assert is_valid("good.") == False

