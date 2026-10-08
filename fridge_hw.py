import datetime
from decimal import Decimal
from typing import Optional


DATE_FORMAT = "%Y-%m-%d"

def add(items: dict[str, list],
        title: str,
        amount: Optional[float | int],
        expiration_date: Optional[str | None]=None):

    if title not in items:
        items[title] = []

    if expiration_date:
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()

    info = {"amount": Decimal(amount), "expiration_date": expiration_date}
    items[title].append(info)

def add_by_note(items: dict[str, list],
                note: str):

    note = note.split()
    expiration_date = None

    if '-' in note[-1]:
        expiration_date = note.pop()

    amount = note[-1]
    title = " ".join(note[:-1])

    add(items, title, amount, expiration_date)


def find(items: dict[str, list],
         needle: str) -> list[str]:

    needle = needle.lower()

    result = []

    for item in items.keys():
        if needle in item.lower():
            result.append(item)

    return result

def amount(items: dict[str, list],
           needle: str) -> Decimal:

    needle = needle.lower()

    list_of_needles = find(items, needle)

    result = Decimal('0')
    for item in list_of_needles:

        for batch in items[item]:
            result += batch["amount"]

    return result


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

    add_by_note(goods, 'Пицца 4 Сыра 2 2023-07-15')
    add_by_note(goods, 'Ваниль 2 де ваниль 22 2')
    print(goods)

    print(find(goods, "ни"))

    print(amount(goods, "пельмени"))

if __name__ == '__main__':
    main()
