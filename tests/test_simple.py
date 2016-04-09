from nose.tools import assert_equal

import properties.simple as simple


def test_full_name():
    a = simple.A('John', "Smith")
    assert_equal(a.full_name, "John Smith")
