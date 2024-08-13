from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar._capacity == 12
    assert jar._size == 0

    jar = Jar(20)
    assert jar._capacity == 20
    assert jar._size == 0

    with pytest.raises(ValueError):
        jar = Jar(-1)

    with pytest.raises(ValueError):
        jar = Jar("twelve")




def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()

    jar.deposit(2)
    assert str(jar) == "🍪🍪"

    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.deposit(13)

    with pytest.raises(ValueError):
        jar.deposit("cat")

    with pytest.raises(ValueError):
        jar.deposit(-1)



def test_withdraw():
    jar = Jar()

    jar.deposit(10)
    jar.withdraw(6)
    assert str(jar) == "🍪🍪🍪🍪"

    jar.deposit(3)
    jar.withdraw(3)
    assert str(jar) == "🍪🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.deposit(9)
        jar.withdraw(10)

    with pytest.raises(ValueError):
        jar.deposit(3)
        jar.withdraw("one")
