from tshirts import size

def test_size():
    assert(size(37) == 'S')
    assert(size(40) == 'M')
    assert(size(43) == 'L')
    assert(size("a") == "Inalid entry")
    print("All is well (maybe!)")