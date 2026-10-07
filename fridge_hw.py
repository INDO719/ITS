import datetime
from decimal import Decimal


DATE_FORMAT = "%Y-%m-%d"

def add(items, title, amount, expiration_date=None):
    pass

def add_by_note(items, note):
    pass

def find(items, needle):
    pass

def amount(items, needle):
    pass

def main():
    goods = {
        "Пельмени Универсальные": [
            {"amount": Decimal("0.5"),
             "expiration_date": datetime.date(2023, 7, 15)},
            {"amount": Decimal("2"),
             "expiration_date": datetime.date(2023, 8, 1)}
        ],
        "Вода": [
            {"amount": Decimal("1.5"),
             "expiration_date": None}
        ]
    }

if __name__ == '__main__':
    main()
