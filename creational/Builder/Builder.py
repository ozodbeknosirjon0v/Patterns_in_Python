from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional


class DrinkKind(Enum):
    ESPRESSO = "ESPRESSO"
    GREEN_TEA = "GREEN_TEA"
    CAPPUCCINO = "CAPPUCCINO"



 # Yig'iladigan mahsulot

class Order:

    def __init__(self) -> None:
        self.name: str = ""
        self.drink: Optional[DrinkKind] = None
        self.dessert: str = ""
        self.price: int = 0

    def __str__(self) -> str:
        drink = self.drink.name if self.drink is not None else None
        return (
            f"Order{{name='{self.name}', drink={drink}, "
            f"dessert='{self.dessert}', price={self.price}}}"
        )


# Abstract builder: qanday yig'ish kerakligi haqida ko'rsatilgan


class OrderBuilder(ABC):

    def __init__(self) -> None:
        self._order: Optional[Order] = None

    def create_order(self) -> OrderBuilder:
        self._order = Order()
        return self

    @abstractmethod
    def build_name(self) -> OrderBuilder:
        ...

    @abstractmethod
    def build_drink(self) -> OrderBuilder:
        ...

    @abstractmethod
    def build_dessert(self) -> OrderBuilder:
        ...

    @abstractmethod
    def build_price(self) -> OrderBuilder:
        ...

    def get_order(self) -> Order:
        if self._order is None:
            raise RuntimeError("Avval create_order() ni chaqiring")
        return self._order


class BreakfastOrderBuilder(OrderBuilder):
    def build_name(self) -> OrderBuilder:
        self.get_order().name = "Nonushta kombo"
        return self

    def build_drink(self) -> OrderBuilder:
        self.get_order().drink = DrinkKind.ESPRESSO
        return self

    def build_dessert(self) -> OrderBuilder:
        self.get_order().dessert = "Kruassan"
        return self

    def build_price(self) -> OrderBuilder:
        self.get_order().price = 25000
        return self


class BusinessLunchOrderBuilder(OrderBuilder):
    def build_name(self) -> OrderBuilder:
        self.get_order().name = "Biznes lanch"
        return self

    def build_drink(self) -> OrderBuilder:
        self.get_order().drink = DrinkKind.GREEN_TEA
        return self

    def build_dessert(self) -> OrderBuilder:
        self.get_order().dessert = "Tiramisu"
        return self

    def build_price(self) -> OrderBuilder:
        self.get_order().price = 60000
        return self


# Director: yig'ish tartibini biladi

class Cashier:

    def __init__(self) -> None:
        self._builder: Optional[OrderBuilder] = None

    def set_builder(self, builder: OrderBuilder) -> None:
        self._builder = builder

    def build_order(self) -> Order:
        if self._builder is None:
            raise RuntimeError("Avval set_builder() ni chaqiring")
        return (
            self._builder.create_order()
            .build_name()
            .build_drink()
            .build_dessert()
            .build_price()
            .get_order()
        )


if __name__ == "__main__":
    cashier = Cashier()

    cashier.set_builder(BreakfastOrderBuilder())
    print(cashier.build_order())

    cashier.set_builder(BusinessLunchOrderBuilder())
    print(cashier.build_order())
