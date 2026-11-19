from abc import ABC, abstractmethod

class ArtDeco(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Chair(ArtDeco):
    def prepare(self):
        return "Chair"


class Sofe(ArtDeco):
    def prepare(self):
        return "Sofa"

class CofeTable(ArtDeco):
    def prepare(self):
        return "CofeTable"



class Victorian(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Armchair(Victorian):
    def prepare(self):
        return "Armchair"

class Sette(Victorian):
    def prepare(self):
        return "Sette"


class ConsoleTable(Victorian):
    def prepare(self):
        return "ConsoleTable"


class ModernTable(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Rug(ModernTable):
    def prepare(self):
        return "Rug"

class LargeRug(ModernTable):
    def prepare(self):
        return "LargeRug"

class OvalTable(ModernTable):
    def prepare(self):
        return "OvalTable"



class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


class ArtDecoFactory(FurnitureFactory):
    def create_chair(self):
        return Chair()

    def create_sofa(self):
        return Sofe()

    def create_table(self):
        return CofeTable()


class VictorianFactory(FurnitureFactory):
    def create_chair(self):
        return Armchair()

    def create_sofa(self):
        return Sette()

    def create_table(self):
        return ConsoleTable()


class ModernFactory(FurnitureFactory):
    def create_chair(self):
        return Rug()

    def create_sofa(self):
        return LargeRug()

    def create_table(self):
        return OvalTable()


def furnish_room(factory: FurnitureFactory):
    for item in (factory.create_chair(), factory.create_sofa(), factory.create_table()):
        print(item.prepare())


if __name__ == '__main__':

    furnish_room(ArtDecoFactory())


    furnish_room(VictorianFactory())


    furnish_room(ModernFactory())
