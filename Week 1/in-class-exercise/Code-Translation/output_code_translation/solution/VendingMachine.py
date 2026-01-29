from typing import Dict, Any


class VendingMachine:
    def __init__(self):
        self.inventory_: Dict[str, Dict[str, float]] = {}
        self.balance_: float = 0.0

    def add_item(self, item_name: str, price: float, quantity: int) -> None:
        if not self.restock_item(item_name, quantity):
            self.inventory_[item_name] = {"price": price, "quantity": float(quantity)}

    def insert_coin(self, amount: float) -> float:
        self.balance_ += amount
        return self.balance_

    def purchase_item(self, item_name: str) -> Any:
        if item_name in self.inventory_:
            item = self.inventory_[item_name]
            if item["quantity"] > 0 and self.balance_ >= item["price"]:
                self.balance_ -= item["price"]
                item["quantity"] -= 1
                return self.balance_
        return False

    def restock_item(self, item_name: str, quantity: int) -> bool:
        if item_name in self.inventory_:
            self.inventory_[item_name]["quantity"] += float(quantity)
            return True
        return False

    def display_items(self) -> str:
        if not self.inventory_:
            return "false"

        lines = []
        for name, data in self.inventory_.items():
            lines.append(f"{name} - ${data['price']} [{data['quantity']}]")
        return "\n".join(lines)

    def inventory(self) -> Dict[str, Dict[str, float]]:
        return dict(self.inventory_)

    def set_inventory(self, x: Dict[str, Dict[str, float]]) -> None:
        self.inventory_ = x

    def set_balance(self, y: float) -> None:
        self.balance_ = y
