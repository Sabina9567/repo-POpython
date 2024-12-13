import doctest

class Bathtub:
    def __init__(self, capacity_volume: float, current_volume: float):
        """
        Создание и подготовка к работе объекта Ванна

        :param capacity_volume: Объем ванны (в литрах).
        :param current_volume: Текущий объем воды в ванне (в литрах).

        Примеры:
        >>> bathtub = Bathtub(1000, 0)  # Инициализация пустой ванны
        """
        if not isinstance(capacity_volume, (int, float)) or capacity_volume <= 0:
            raise TypeError("Объем ванны должен быть положительным числом.")
        if not isinstance(current_volume, (int, float)) or current_volume < 0:
            raise TypeError("Текущий объем воды должен быть числом.")
        if current_volume > capacity_volume:
            raise ValueError("Текущий объем воды не может превышать вместимость ванны.")

        self.capacity_volume = capacity_volume
        self.current_volume = current_volume

    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли ванна.

        :return: True, если ванна пуста, False иначе.

        >>> bathtub = Bathtub(1000, 0)
        >>> bathtub.is_empty()
        True
        """
        return self.current_volume == 0

    def add_water(self, water_amount: float) -> None:
        """
        Добавляет воду в ванну.

        :param water_amount: Объем добавляемой воды (в литрах).
        :raises ValueError: если добавляемый объем воды приводит к переполнению ванны.
        Примеры:
        >>> bathtub = Bathtub(1000, 500)
        >>> bathtub.add_water(500)
        """
        if not isinstance(water_amount, (int, float)) or water_amount <= 0:
            raise TypeError("Добавляемый объем воды должен быть положительным числом.")

        new_volume = self.current_volume + water_amount
        if new_volume > self.capacity_volume:
            raise ValueError("Добавление воды приведет к переполнению ванны.")
        self.current_volume = new_volume

    def drain_water(self, water_amount: float) -> None:
        """
        Спускает воду из ванны.

        :param water_amount: Объем воды для слива (в литрах).
        :raises ValueError: если объем воды для слива больше текущего объема.
        Примеры:
        >>> bathtub = Bathtub(1000, 1000)
        >>> bathtub.drain_water(600) # Слить 600 литров
        """
        if not isinstance(water_amount, (int, float)) or water_amount <= 0:
            raise TypeError("Объем воды для слива должен быть положительным числом.")

        if water_amount > self.current_volume:
            raise ValueError("Нельзя слить больше воды, чем есть в ванне.")
        self.current_volume -= water_amount


if __name__ == "__main__":
    doctest.testmod()