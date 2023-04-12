# Author: Justin Huang
# GitHub username: huangjus
# Date: 4/11/23
# Description: This code defines three classes for a lemonade stand: MenuItem, SalesForDay, and LemonadeStand.
# The MenuItem class represents a menu item, SalesForDay represents the sales for a particular day, and
# LemonadeStand represents the stand itself. It has methods for adding menu items, recording sales, getting the
# number of items sold on a given day, getting the total number of a particular item sold over time, getting the
# total profit on a particular item over time, and getting the total profit on all items sold over time.

class MenuItem:
    """Represents a menu item to be offered for sale at the lemonade stand."""

    def __init__(self, name, wholesale_cost, selling_price):
        """Initializes a new MenuItem object with the given name, wholesale cost, and selling price."""

        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """Returns the name of this MenuItem object."""

        return self._name

    def get_wholesale_cost(self):
        """Returns the wholesale cost of this MenuItem object."""

        return self._wholesale_cost

    def get_selling_price(self):
        """Returns the selling price of this MenuItem object."""

        return self._selling_price


class SalesForDay:
    """Represents the sales for a particular day."""

    def __init__(self, day, sales_dict):
        """Initializes a new SalesForDay object with the given day and sales dictionary."""

        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """Returns the day of this SalesForDay object."""

        return self._day

    def get_sales_dict(self):
        """Returns the sales dictionary of this SalesForDay object."""

        return self._sales_dict


class InvalidSalesItemError(Exception):
    pass


class LemonadeStand:
    """Represents a lemonade stand."""

    def __init__(self, name):
        """Initializes a new LemonadeStand object with the given name."""

        self._name = name
        self._current_day = 0
        self._menu = {}
        self._sales_of_menu_item_for_day = []

    def get_name(self):
        """Returns the name of this LemonadeStand object."""

        return self._name

    def add_menu_item(self, menu_item):
        """Adds the given MenuItem object to the menu dictionary of this LemonadeStand object."""

        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, sales_dict):
        """Records the sales for today and updates the sales record of this LemonadeStand object."""

        for item_name in sales_dict:
            if item_name not in self._menu:
                raise InvalidSalesItemError(f"{item_name} is not in the menu.")

        sales_for_today = SalesForDay(self._current_day, sales_dict)
        self._sales_of_menu_item_for_day.append(sales_for_today)
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day, menu_item_name):
        """Returns the number of the given menu item sold on the given day."""

        sales_for_day = self._sales_of_menu_item_for_day[day]
        sales_dict_for_day = sales_for_day.get_sales_dict()

        if menu_item_name in sales_dict_for_day:
            return sales_dict_for_day[menu_item_name]
        else:
            return 0

    def total_sales_for_menu_item(self, menu_item_name):
        """Returns the total number of the given menu item sold over the history of the stand."""

        total_sales = 0
        for sales_for_day in self._sales_of_menu_item_for_day:
            sales_dict_for_day = sales_for_day.get_sales_dict()
            if menu_item_name in sales_dict_for_day:
                total_sales += sales_dict_for_day[menu_item_name]

        return total_sales

    def total_profit_for_menu_item(self, menu_item_name):
        """Returns the total profit on the given menu item over the history of the stand."""

        total_profit = 0
        menu_item = self._menu.get(menu_item_name)
        if menu_item:
            for sales_for_day in self._sales_of_menu_item_for_day:
                sales_dict_for_day = sales_for_day.get_sales_dict()
                if menu_item_name in sales_dict_for_day:
                    total_profit += (sales_dict_for_day[menu_item_name] *
                                     (menu_item.get_selling_price() - menu_item.get_wholesale_cost()))

        return total_profit

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
