from nose.tools import assert_equal

import properties.customer as customer


def test_customer():
    a = customer.Customer('Fred')
    assert_equal(a.orders, customer.ORDERS)
