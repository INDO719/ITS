

class Employee:
    """
    Базовый класс сотрудника.

    Attributes:
        id (int): Идентификатор сотрудника.
        name (str): Имя сотрудника.
        base_money (float): Базовая заработная плата.
    """

    def __init__(self, id: int, name: str, base_money: float) -> None:
        """
        Инициализирует сотрудника.

        Args:
            id (int): Идентификатор сотрудника.
            name (str): Имя сотрудника.
            base_money (float): Базовая заработная плата.

        Returns:
            None
        """

        self.id = id
        self.name = name
        self.base_money = base_money

    def calculate_salaries(self) -> float:
        """
        Возвращает заработную плату сотрудника.

        Returns:
            float: Базовая заработная плата.

        Example:
            >>> Employee(0, "Alex", 50_000).calculate_salaries()
            50000
        """

        return self.base_money


class Manager(Employee):
    """
    Менеджер с бонусом к базовой заработной плате.

    Attributes:
        bonus (float): Бонус менеджера.
    """

    def __init__(self, id: int, name: str, base_money: float, bonus: float) -> None:
        """
        Инициализирует менеджера.

        Args:
            id (int): Идентификатор сотрудника.
            name (str): Имя сотрудника.
            base_money (float): Базовая заработная плата.
            bonus (float): Бонус менеджера.

        Returns:
            None
        """

        super().__init__(id, name, base_money)
        self.bonus = bonus

    def calculate_salaries(self) -> float:
        """
        Возвращает заработную плату менеджера.

        Returns:
            float: Базовая заработная плата плюс бонус.

        Example:
            >>> Manager(1, "Ivan", 50_000, 10_000).calculate_salaries()
            60000
        """
        return self.base_money + self.bonus


class Developer(Employee):
    """
    Разработчик, зарплата которого зависит от количества проектов.

    Attributes:
        project_sum (int): Количество проектов.
    """

    def __init__(self, id: int, name: str, base_money: float, project_sum: int) -> None:
        """
        Инициализирует разработчика.

        Args:
            id (int): Идентификатор сотрудника.
            name (str): Имя сотрудника.
            base_money (float): Базовая заработная плата.
            project_sum (int): Количество проектов.

        Returns:
            None
        """

        super().__init__(id, name, base_money)
        self.project_sum = project_sum

    def calculate_salaries(self) -> float:
        """
        Возвращает заработную плату разработчика.

        Returns:
            float: Базовая заработная плата плюс оплата за проекты.

        Example:
            >>> Developer(1, "Eva", 50_000, 5).calculate_salaries()
            100000
        """

        return self.base_money + self.project_sum * 10_000