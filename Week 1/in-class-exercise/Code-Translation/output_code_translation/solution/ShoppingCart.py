from typing import Dict, Tuple


class ShoppingCart:
    def __init__(self) -> None:
        self.items: Dict[str, Tuple[float, int]] = {}

    def add_item(self, item: str, price: float, quantity: int = 1) -> None:
        # Overwrite existing entry or add new one
        self.items[item] = (price, quantity)

    def remove_item(self, item: str, quantity: int = 1) -> None:
        if item in self.items:
            price, qty = self.items[item]
            qty -= quantity
            if qty <= 0:
                del self.items[item]
            else:
                self.items[item] = (price, qty)

    def view_items(self) -> Dict[str, Tuple[float, int]]:
        # Return a shallow copy to mimic C++ returning by value
        return self.items.copy()

    def total_price(self) -> float:
        total = 0.0
        for price, qty in self.items.values():
            total += price * qty
        return total
