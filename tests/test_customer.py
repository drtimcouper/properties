from nose.tools import assert_equal, assert_raises

import properties.customer as customer


def test_customer_orders():
    c = customer.Customer('Fred')
    assert_equal(c.orders, customer.ORDERS)


def test_better_customer_orders():
    c = customer.BetterCustomer('Fred')
    assert_equal(c.orders, customer.ORDERS)


def test_better_customer_orders_readonly():
     c = customer.BetterCustomer('Fred')
     with assert_raises(AttributeError) as err:
        c.orders = 'stuff'
     assert_equal(str(err.exception), "can't set attribute" )
