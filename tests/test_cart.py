import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=10.0)))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", cost=10.0)))

    def test_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Test DVD", cost=100.0))
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(-10)

    def test_sort_by_title(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Zootopia", cost=15.0))
        cart.add_dvd(DigitalVideoDisc("Aladdin", cost=20.0))
        cart.sort_by_title()
        self.assertEqual(cart.items[0].title, "Aladdin")
        self.assertEqual(cart.items[1].title, "Zootopia")

    def test_sort_by_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Expensive DVD", cost=50.0))
        cart.add_dvd(DigitalVideoDisc("Cheap DVD", cost=10.0))
        cart.sort_by_cost()
        self.assertEqual(cart.items[0].cost, 10.0)
        self.assertEqual(cart.items[1].cost, 50.0)


if __name__ == "__main__":
    unittest.main()
