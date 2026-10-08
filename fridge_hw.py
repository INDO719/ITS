import datetime
from decimal import Decimal


DATE_FORMAT = "%Y-%m-%d"

def add(items, title, amount, expiration_date=None):

    if title not in items:
        items[title] = []

    if expiration_date:
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()

    info = {"amount": Decimal(amount), "expiration_date": expiration_date}
    items[title].append(info)

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

    add(goods, "Печеньки", 20, "2025-08-10")
    add(goods, "Печеньки", 20)
    print(goods)

if __name__ == '__main__':
    main()
