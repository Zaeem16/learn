from project import mode_selector, play_game, run_mode, play_again
from project import systemExitError, modeError
from project import my_countries
from unittest.mock import patch
import pytest


def main():
    test_play_again()
    test_play_game()
    test_mode_selector()
    test_run_mode()

def test_play_again():
    with patch('builtins.input', return_value="yes"):
        assert play_again() == True

    with patch('builtins.input', return_value="ok"):
        assert play_again() == False

def test_mode_selector():
    with patch('builtins.input', return_value="easy"):
        assert mode_selector() == "easy"

    with patch('builtins.input', return_value="medium"):
        assert mode_selector() == "medium"

    with patch('builtins.input', return_value="Hard"):
        assert mode_selector() == "hard"

    with patch('builtins.input', return_value="ImpossIble"):
        assert mode_selector() == "impossible"

    with patch('builtins.input', return_value="q"):
        with pytest.raises(systemExitError):
            mode_selector()

    with patch('builtins.input', return_value="no"):
        with pytest.raises(modeError):
            mode_selector()


def test_play_game():
    with patch("builtins.input", return_value="United states"), patch("random.choice", return_value="United States"):
        game = play_game(5)
        output = next(game)
        expected_output = "\nHint 1: " + my_countries["United States"][0]
        assert output == expected_output

    with patch("builtins.input", return_value="afghanistan"), patch("random.choice", return_value="Afghanistan"):
        game = play_game(3)
        output = next(game)
        expected_output = "\nHint 1: " + my_countries["Afghanistan"][0]
        assert output == expected_output


def test_run_mode():
    with pytest.raises(systemExitError):
        with patch('builtins.print') as mock_print, patch('project.play_game', return_value=['event1', 'event2']), patch('project.play_again', side_effect=[True, False]), patch('project.mode_selector', return_value='easy'):
            run_mode('easy')

if __name__ == "__main__":
    main()
