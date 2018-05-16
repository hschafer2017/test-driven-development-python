def tests_are_equal(a, b): 
    assert a == b, "Expected {0}, got {1}".format(a,b)


def test_greater(a, b):
    assert b < a, "Expected {5 > 3}, got {3 < 5}".format(b, a)

print("Success")


