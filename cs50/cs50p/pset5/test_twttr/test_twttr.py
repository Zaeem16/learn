from twttr import shorten

def test_no_vowel():
    assert shorten("hmd") == "hmd"

def test_capital():
    assert shorten("AHMAD") == "HMD"

def test_lower():
    assert shorten("ahmad") == "hmd"

def test_numstr():
    assert shorten("Ahmad 1") == "hmd 1"

def test_upper():
    assert shorten("ahmad") != "HMD"
    
def test_grammar():
    assert shorten("hello, World!") != "hll Wrld"



