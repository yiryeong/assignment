import unittest
from assignment import InventoryAllocator


class Testing(unittest.TestCase):
    def setUp(self) -> None:
        self.inventory = InventoryAllocator()
