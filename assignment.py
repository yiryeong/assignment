class InventoryAllocator:
    def __init__(self):
        self.result = []

    def solution(self, order, warehouse_list):
        for warehouse in warehouse_list:
            warehouse_inventory = warehouse['inventory']
            get_product_condition = {}
            for product, count in order.items():
                if product in warehouse_inventory.keys() and count != 0 and warehouse_inventory[product] != 0:
                    get_product_count_in_warehouse = min(count, warehouse_inventory[product])
                    order[product] = 0 if get_product_count_in_warehouse == count else count - warehouse_inventory[product]
                    get_product_condition[product] = get_product_count_in_warehouse

            if get_product_condition:
                self.result.append({warehouse['name']: get_product_condition})

            if all(value == 0 for value in order.values()):
                break

        return self.result


if __name__ == '__main__':
    IA = InventoryAllocator()
    result = IA.solution({'apple': 5, 'banana': 5, 'orange': 5},
                         [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}},
                          {'name': 'dm', 'inventory': {'banana': 5, 'orange': 10}}])
    print(result)
