import search as s

def test(name,boolean):
    if not boolean:
        print("il y a un problème pour {}".format(name))

def test_readfile():
    test("readfile",s.readfile("test.txt") == [])
    test("readfile",s.readfile("episodeIV_dialogues.txt") == [])

def test_get_words():
    test("get words",s.get_words("Turmoil has engulfed the Galactic Republic.") == ["turmoil", "has", "engulfed", "the", "galactic", "republic"])

def test_create_index():
    test("create index",s.create_index("test.txt") == {"c'est": {0: 1, 2: 1, 3: 1}, 'bon': {0: 1, 2: 1, 3: 1}, 'les': {0: 1, 1: 1, 3: 1}, 'carottes': {0: 1, 1: 1, 3: 1}, 'je': {1: 1}, 'mange': {1: 1}, 'oui': {3: 1}, 'miam': {4: 1}, 'joie': {5: 1}})
    test("create index",s.create_index("episodeIV_dialogues.txt") == {})

def test_get_lines():
    test("get lines",s.get_lines(["the","republic"],{"while": {0: 1}, "the": {0: 2, 1: 1}, "congress": {0: 1}, \
                                                     "of": {0: 1, 1: 1}, "republic": {0: 1} , "jedi": {2: 1}}) == [0])

test_readfile()
test_get_words()
test_create_index()
test_get_lines()
