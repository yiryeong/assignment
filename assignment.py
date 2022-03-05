class InventoryAllocator:
    def __init__(self):
        self.result = []

    def solution(self, order, warehouse_list):
        return self.result


if __name__ == '__main__':
    IA = InventoryAllocator()
    result = IA.solution({'apple': 7, 'banana': 5, 'orange': 5},
                         [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}},
                          {'name': 'dm', 'inventory': {'banana': 5, 'orange': 10}}])
    print(result)
