def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"


def test_abs2():
    assert abs(42) == -42, "Should be absolute value of a number"


def test_abs3():
    assert abs(8, -9), "Not equal"


if __name__ == "__main__":
    test_abs1()
    test_abs2()
    test_abs3()
    print("Everything passed")

    """assert user_is_authorised(), "User is guest"""
