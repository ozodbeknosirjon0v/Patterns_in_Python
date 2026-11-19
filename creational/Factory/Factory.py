from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def preparation(self):
        pass

class Cofe(Product):
    def preparation(self):
        return "Late"

class Tea(Product):
    def preparation(self):
        return "GreenTea"


class ProductShop(ABC):
    @abstractmethod
    def create(self) -> Product:
        pass

class CofeShop(ProductShop):
    def create(self) -> Cofe:
        return Cofe()


class TeaShop(ProductShop):
    def create(self) -> Tea:
        return Tea()


if __name__ == "__main__":
    creator = CofeShop()
    cofe = creator.create()
    print(cofe.preparation())

    creator = TeaShop()
    tea = creator.create()
    print(tea.preparation())



