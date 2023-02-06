def test_one_plus_one():
    assert 1 + 1 == 2


def test_python_version():
    import sys
    assert sys.version_info >= (3, 9)


# todo: implement poetry version check, should be >= 1.3.1
