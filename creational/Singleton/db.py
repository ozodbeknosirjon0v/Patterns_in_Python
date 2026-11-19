import threading
from typing import ClassVar, Optional


# Singleton: butun dastur bo'yicha faqat bitta nusxa mavjud bo'ladi.

class Database:

    _instance: ClassVar[Optional["Database"]] = None
    _lock: ClassVar[threading.Lock] = threading.Lock()
    _allow_creation: ClassVar[bool] = False

    def __init__(self) -> None:
        if not Database._allow_creation:
            raise RuntimeError(
                "Database() ni to'g'ridan-to'g'ri chaqirib bo'lmaydi. "
                "Database.get_instance() dan foydalaning."
            )
        print("DB ga ulanilmoqda...")
        self._connected = True

    @classmethod
    def get_instance(cls) -> "Database":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._allow_creation = True
                    try:
                        cls._instance = cls()
                    finally:
                        cls._allow_creation = False
        return cls._instance

    def query(self, sql: str) -> None:
        print(f"Bajarildi: {sql}")


if __name__ == "__main__":
    db1 = Database.get_instance()
    db2 = Database.get_instance()

    db1.query("SELECT * FROM users")
    print(db1 is db2)
