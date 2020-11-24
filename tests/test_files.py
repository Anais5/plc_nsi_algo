from algo.struct.files import File1, File2, File3, File4

def test_len():
    assert False # à remplacer...

def test_enfiler():
    assert False

def test_defiler():
    assert False

def test_str():
    assert False

@pytest.fixture()
def file_quatre():
    f = File4(5)
    f.enfiler(1)
    f.enfiler(2)
    f.enfiler(3)
    return f

file_quatre_bis = file_quatre

@pytest.mark.parametrize("origine, attendu", [(file_quatre_bis, "1 -> 2 -> 3"),
                                              (file_quatre_bis.enfiler(4).depiler(), "2 -> 3 -> 4")])
def test_file_quatre_bis(origine, attendu):
    assert str(origine) == attendu

def test_file_quatre():
    assert not file_quatre.est_vide()
    assert file_quatre.defiler == 1
    file_quatre.enfiler(4)
    file_quatre.enfiler(5)
    file_quatre.enfiler(6)
    assert len(file_quatre) == 5
    assert file_quatre.defiler == 2