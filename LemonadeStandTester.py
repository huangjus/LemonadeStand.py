# Author: Justin Huang
# GitHub username: huangjus
# Date: 4/11/23
# Description: This code defines classes to model a lemonade stand business, including MenuItem, SalesForDay, and
# LemonadeStand, as well as a custom exception InvalidSalesItemError. These classes manage menu items, sales records,
# and profit calculations. The code also provides unit tests using the unittest module to ensure the classes function
# correctly, covering aspects like adding menu items, recording sales, and handling invalid sales items.

import unittest
from lemonade_stand import MenuItem, SalesForDay, LemonadeStand, InvalidSalesItemError


class TestLemonadeStandClasses(unittest.TestCase):

    def test_menu_item(self):
        item = MenuItem('lemonade', 0.5, 1.5)
        self.assertEqual(item.get_name(), 'lemonade')
        self.assertEqual(item.get_wholesale_cost(), 0.5)
        self.assertEqual(item.get_selling_price(), 1.5)

    def test_sales_for_day(self):
        sales = {'lemonade': 5, 'cookie': 2}
        day = SalesForDay(0, sales)
        self.assertEqual(day.get_day(), 0)
        self.assertEqual(day.get_sales_dict(), sales)

    def test_lemonade_stand_add_menu_item(self):
        stand = LemonadeStand('Lemons R Us')
        item = MenuItem('lemonade', 0.5, 1.5)
        stand.add_menu_item(item)
        self.assertIn('lemonade', stand._menu)

    def test_lemonade_stand_enter_sales_for_today(self):
        stand = LemonadeStand('Lemons R Us')
        item = MenuItem('lemonade', 0.5, 1.5)
        stand.add_menu_item(item)
        sales = {'lemonade': 5}
        stand.enter_sales_for_today(sales)
        self.assertEqual(len(stand._sales_of_menu_item_for_day), 1)

    def test_lemonade_stand_invalid_sales_item_error(self):
        stand = LemonadeStand('Lemons R Us')
        item = MenuItem('lemonade', 0.5, 1.5)
        stand.add_menu_item(item)
        sales = {'nori': 3}
        with self.assertRaises(InvalidSalesItemError):
            stand.enter_sales_for_today(sales)


if __name__ == '__main__':
    unittest.main()
