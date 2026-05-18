#!/usr/bin/env python3
from __future__ import annotations
from abc import ABC, abstractmethod


class Beverage(ABC):
    """Abstract base class for beverages"""

    @abstractmethod
    def cost(self) -> int:
        """Return the cost of the beverage in cents"""
        pass

    @abstractmethod
    def description(self) -> str:
        """Return the description of the beverage"""
        pass


class Coffee(Beverage):
    """Concrete beverage: plain coffee"""

    def cost(self) -> int:
        return 50

    def description(self) -> str:
        return "Coffee"


class MilkDecorator(Beverage):
    """Decorator that adds milk to a beverage"""

    def __init__(self, inner: Beverage) -> None:
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 10

    def description(self) -> str:
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Decorator that adds sugar to a beverage"""

    def __init__(self, inner: Beverage) -> None:
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 5

    def description(self) -> str:
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Decorator that adds caramel to a beverage"""

    def __init__(self, inner: Beverage) -> None:
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 15

    def description(self) -> str:
        return self._inner.description() + " + caramel"


def main() -> None:
    # Plain coffee with milk
    beverage1 = MilkDecorator(Coffee())
    print(f"{beverage1.description()} {beverage1.cost()}")

    # Coffee with sugar and milk
    beverage2 = MilkDecorator(SugarDecorator(Coffee()))
    print(f"{beverage2.description()} {beverage2.cost()}")

    # Coffee with sugar, milk, and caramel
    beverage3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(f"{beverage3.description()} {beverage3.cost()}")


if __name__ == "__main__":
    main()
