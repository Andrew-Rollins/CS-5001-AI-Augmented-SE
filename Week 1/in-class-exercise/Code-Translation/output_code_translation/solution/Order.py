from dataclasses import dataclass

@dataclass
class Dish:
    dish: str
    price: float
    count: int


class Order:
    def __init__(self):
        self.menu: list[Dish] = []
        self.selected_dishes: list[Dish] = []
        self.sales: dict[str, float] = {}

    def add_dish(self, dish: Dish) -> bool:
        for menu_dish in self.menu:
            if dish.dish == menu_dish.dish:
                if menu_dish.count < dish.count:
                    return False
                else:
                    menu_dish.count -= dish.count
                    break
        self.selected_dishes.append(dish)
        return True

    def calculate_total(self) -> float:
        total = 0.0
        for dish in self.selected_dishes:
            multiplier = self.sales.get(dish.dish)
            if multiplier is not None:
                total += dish.price * dish.count * multiplier
        return total

    def checkout(self) -> float:
        if not self.selected_dishes:
            return 0.0
        total = self.calculate_total()
        self.selected_dishes.clear()
        return total
