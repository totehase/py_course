import module_useful_funcs as m


# m.is_even
def test_is_even_40_true():
    assert m.is_even(40) == True


def test_is_even_1_false():
    assert m.is_even(1) == False


def test_is_even_neg_1_fasle():
    assert m.is_even(-1) == False


def test_is_even_neg_8_true():
    assert m.is_even(8) == True


# m.my_pow
def test_my_pow_4_true():
    assert m.my_pow(4) == 16

def test_my_pow_3_true():
    assert m.my_pow(3) == 9

def test_my_pow_1_true():
    assert m.my_pow(1) == 1


# m.nameUpper