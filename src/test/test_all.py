from levenshtein_distance import levenshtein_distance
from main import load_vocab

def test_levenshtein_distance():
    assert levenshtein_distance('hola', 'hello') == 3

def test_load_vocab():
    vocabs = load_vocab(file_path='data/vocab.txt')
    assert len(vocabs) > 0
    assert all(isinstance(word, str) for word in vocabs)