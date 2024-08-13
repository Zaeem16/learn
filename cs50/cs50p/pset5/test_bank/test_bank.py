from bank import value

def main():
    test_return_0()
    test_return_20()
    test_return_100()


def test_return_0():
    assert value("hello") == 0
    assert value("hello to") == 0
    assert value("HELLO TO") == 0
    assert value("heLlO") == 0


def test_return_20():
    assert value("hey") == 20
    assert value("HOW YOU DOING?") == 20
    assert value("hI, how are you?") == 20

def test_return_100():
    assert value("good morning") == 100
    assert value("What is happening?") == 100
    assert value("Well done!") == 100


