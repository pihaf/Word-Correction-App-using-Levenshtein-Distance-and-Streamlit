from levenshtein_distance import levenshtein_distance

def test_levenshtein_distance():
    assert levenshtein_distance('hola', 'hello') == 3