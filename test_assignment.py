import unittest
from assignment import InventoryAllocator


class Testing(unittest.TestCase):
    def setUp(self) -> None:
        self.inventory = InventoryAllocator()

    # assignment Examples 1
    def test_examples_one(self):
        order = {'apple': 1}
        warehouses = [{'name': 'owd', 'inventory': {'apple': 1}}]
        result = self.inventory.solution(order, warehouses)
        self.assertEqual(result, [{'owd': {'apple': 1}}])

    # assignment Examples 2
    def test_examples_two(self):
        order = {'apple': 1}
        warehouses = [{'name': 'owd', 'inventory': {'apple': 0}}]
        result = self.inventory.solution(order, warehouses)
        self.assertEqual(result, [])

    # assignment Examples 3
    def test_examples_there(self):
        order = {'apple': 10}
        warehouses = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
        result = self.inventory.solution(order, warehouses)
        self.assertEqual(result, [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}])

    # There is no order products in any warehouse => return []
    def test_no_matching_product_in_all_warehouses(self):
        order = {'banana': 10}
        warehouses = [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 3}}, {'name': 'dm', 'inventory': {'orange': 3}}]
        result = self.inventory.solution(order, warehouses)
        self.assertEqual(result, [])

    # if Order is empty will be return empty list
    def test_empty_order(self):
        order = {}
        warehouses = [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 3}}]
        result = self.inventory.solution(order, warehouses)
        self.assertEqual(result, [])

    # Get all order products in first warehouse
    def test_get_products_in_first_warehouse(self):
        order = {'apple': 2, 'orange': 3}
        warehouses = [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 3}}, {'name': 'dm', 'inventory': {'orange': 3}}]
        result = self.inventory.solution(order, warehouses)
        self.assertEqual(result, [{'owd': {'apple': 2, 'orange': 3}}])

    # Get order products in multiple warehouses
    def test_get_products_in_multi_warehouse(self):
        order = {'apple': 5, 'banana': 5, 'orange': 5}
        warehouses = [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}}, {'name': 'dm', 'inventory': {'banana': 5, 'orange': 10}}]
        result = self.inventory.solution(order, warehouses)
        self.assertEqual(result, [{'owd': {'apple': 5, 'orange': 5}}, {'dm': {'banana': 5}}])

    # Order volume is higher than warehouse stock
    def test_orders_volume_higher_warehouse_stock(self):
        order = {'apple': 15, 'banana': 15, 'orange': 15}
        warehouses = [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}}, {'name': 'dm', 'inventory': {'banana': 5, 'orange': 10}}]
        result = self.inventory.solution(order, warehouses)
        self.assertEqual(result, [{'owd': {'apple': 5, 'orange': 10}}, {'dm': {'banana': 5, 'orange': 5}}])
