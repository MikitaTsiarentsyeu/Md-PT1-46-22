import unittest


class TestData(unittest.TestCase):
    def setUp(self) -> None:
        import data
        self.data = data


        base = {
            'wh': [
                {'product_id': 'f123454-888', 'category': 'fruit', 'product_name': 'apples', 'price': 2, 'quantity': 54},
                {'product_id': 'f543221-098', 'category': 'fruit', 'product_name': 'bananas', 'price': 1.5, 'quantity': 45},
            ],
            'cart': [],
            'orders': [],
        }
        self.data.base = base

        self.test_dict = {'product_id': 'f123454-888',
                          'category': 'fruit',
                          'product_name': 'apples',
                          'price': 2, 'quantity': 54}

    def tearDown(self) -> None:
        base = {
            'wh': [
                {'product_id': 'f123454-888', 'category': 'fruit', 'product_name': 'apples', 'price': 2, 'quantity': 54},
                {'product_id': 'f543221-098', 'category': 'fruit', 'product_name': 'bananas', 'price': 1.5, 'quantity': 45},
            ],
            'cart': [],
            'orders': [],
        }
        self.data.base = base

    def test_get_wh_products(self):
        self.assertIsInstance(self.data.get_wh_products(), list)
        self.assertEqual(len(self.data.get_wh_products()), 2)

    def test_get_wh_product_by_id(self):

        self.assertTrue(self.data.get_wh_product_by_id('f123454-888') == self.test_dict)
        self.assertIsNone(self.data.get_wh_product_by_id(''))

    def test_get_categories_of_products(self):
        self.assertEqual(len(self.data.get_categories_of_products()), 1)
        self.assertIsInstance(self.data.get_categories_of_products(), list)
        self.assertTrue('fruit' in self.data.get_categories_of_products())

    def test_get_cart_products(self):
        self.assertFalse(self.data.get_cart_products())
        self.assertIsInstance(self.data.get_cart_products(), list)

    def test_get_order_products(self):
        self.assertFalse(self.data.get_order_products())
        self.assertIsInstance(self.data.get_order_products(), list)

    def test_get_wh_products_by_category(self):
        temp_data = self.data.get_wh_products_by_category('fruit')
        self.assertEqual(len(temp_data), 2)
        self.assertIsInstance(temp_data, list)
        self.assertIsInstance(temp_data[0], dict)
        self.assertEqual(temp_data[0], self.test_dict)

    def test_set_wh_products_value(self):
        self.data.set_wh_products_value('f123454-888', 30)
        d = self.data.get_wh_product_by_id('f123454-888')
        self.assertEqual(d['quantity'], 30)

    def test_add_cart_products(self):
        self.data.add_product_to_cart('f123454-888')
        self.assertEqual(len(self.data.base['cart']), 1)
        self.assertEqual(self.data.base['cart'][0], self.test_dict)

    def test_add_order_products(self):
        self.data.add_orders_products('f123454-888')
        self.assertEqual(len(self.data.base['orders']), 1)
        self.assertEqual(self.data.base['orders'][0], self.test_dict)

    def test_set_cart_products_value(self):
        self.data.add_product_to_cart('f123454-888')
        self.data.set_cart_products_value('f123454-888', 30)
        self.assertEqual(self.data.base['cart'][0]['quantity'], 30)

    def test_set_orders_products_value(self):
        self.data.add_orders_products('f123454-888')
        self.data.set_orders_products_value('f123454-888', 30)
        self.assertEqual(self.data.base['orders'][0]['quantity'], 30)

    def test_delete_cart_product(self):
        self.assertEqual(len(self.data.base['cart']), 0, 'cart is not empty')
        self.data.add_product_to_cart('f123454-888')
        self.assertEqual(len(self.data.base['cart']), 1, 'cart is empty')
        self.data.delete_cart_product('f123454-888')
        self.assertEqual(len(self.data.base['cart']), 0, 'cart is not cleared')

    def test_clear_cart_products(self):
        self.data.add_product_to_cart('f123454-888')
        self.assertEqual(len(self.data.base['cart']), 1)
        self.data.clear_cart_products()
        self.assertEqual(len(self.data.base['cart']), 0)

    def test_clear_orders_products(self):
        self.data.add_orders_products('f123454-888')
        self.assertEqual(len(self.data.base['orders']), 1)
        self.data.clear_orders_products()
        self.assertEqual(len(self.data.base['orders']), 0)

    def test_copy_cart_to_orders(self):
        self.data.add_product_to_cart('f123454-888')
        self.assertEqual(len(self.data.base['cart']), 1, 'cart is empty')
        self.assertEqual(len(self.data.base['orders']), 0, 'orders do not empty')
        self.data.copy_cart_to_orders()
        self.assertEqual(len(self.data.base['cart']), 1, 'cart is empty')
        self.assertEqual(len(self.data.base['orders']), 1, 'orders is empty')

        self.assertEqual(self.data.get_order_products()[0], self.test_dict)

    def test_get_id_by_products(self):
        product_id = self.data.get_id_by_product_name('apples')
        self.assertEqual(product_id, 'f123454-888')



class TestBL(unittest.TestCase):
    def setUp(self) -> None:
        import bl
        self.bl = bl

    def test_add_product_to_cart(self):
        self.bl.data.add_product_to_cart('f123454-888')
        self.bl.data.set_cart_products_value('f123454-888', delta=+4)
        self.bl.data.set_wh_products_value('f123454-888', delta=-4)



if __name__ == "__main__":
    unittest.main()
