"""#   Задача #1 – шифр Цезаря

import string
from pprint import pprint

RU_ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ANG_ALPHABET = string.ascii_uppercase


def caesar_cipher(message: str, step: int) -> str:
    encrypted_message = ""
    language = RU_ALPHABET if message[0].upper() in RU_ALPHABET else ANG_ALPHABET

    for let in message:
        if let == " ":
            encrypted_message += " "
            continue

        idx = language.index(let.upper()) + abs(step) % len(language) * (step // abs(step))
        if len(language) - 1:
            idx %= len(language)

        if let.isupper():
            encrypted_message += language[idx]
        else:
            encrypted_message += language[idx].lower()

    return encrypted_message


message = "Hello World"
shift = 17
x = caesar_cipher(message, shift)
print(f"{x} | {caesar_cipher(x, -shift)}")


#   Задача #2 – олимпиада

def check_winners(scores: list[int], student_score: int) -> None:
    winners = [scores.pop(scores.index(max(scores))) for _ in range(3)]
    print("Вы в тройке победителей!" if student_score in winners else "Вы не попали в тройку победителей.")


scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
student_score = 20

check_winners(scores, student_score)


#   Задача #3 – пироженки и коробочки

def print_pack_report(amount: int) -> None:
    for n in range(amount, 0, -1):
        pass

    is_3 = amount % 3 == 0
    is_5 = amount % 5 == 0

    if is_3 and is_5:
        print(f"{amount} - расфасуем по 3 или по 5")
    elif is_3:
        print(f"{amount} - расфасуем по 3")
    elif is_5:
        print(f"{amount} - расфасуем по 5")
    else:
        print(f"{amount} - не заказываем!")


print_pack_report(30)
print_pack_report(6)
print_pack_report(55)
print_pack_report(13)

#   Задача #4 – сложные пароли

import string
import random
from typing import Optional


def generate_password(length: int, lowercase: bool,
                      uppercase: bool, special: bool, nums: bool) -> Optional[str | None]:
    if length == 0:
        print("Вы не указали длину")
        return

    alph = ""
    if lowercase:
        alph += string.ascii_lowercase
    if uppercase:
        alph += string.ascii_uppercase

    if special:
        alph += "!@#$%^&*()_"

    if nums:
        alph += "0123456789"

    if not alph:
        print("Пароль должен содержать символы.")
        return

    password = "".join([random.choice(alph) for _ in range(length)])

    return password


print("Сгенерируйте свой пароль")
length_pass = int(input("Введите длину пароля: "))
lower_pass = input("В пароле будет нижний регистр? (да/нет): ")
upper_pass = input("В пароле будет верхний регистр?(да/нет): ")
spec_pass = input("В пароле будут специальные символы?(да/нет): ")
nums_pass = input("В пароле будут цифры?(да/нет): ")

is_lower = lower_pass == "да"
is_upper = upper_pass == "да"
is_spec = spec_pass == "да"
is_nums = nums_pass == "да"

password = generate_password(length_pass, is_lower, is_upper, is_spec, is_nums)
if password is not None:
    print(f"Ваш пароль: {password}")

#   Задача #5 – римский конвертер

alph_rn = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
           "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

alph_nr = {value: key for key, value in alph_rn.items()}


def from_roman_to_numeral_converter(number: str) -> int:
    result = 0

    for sym in number[:]:
        if sym in ("IV", "IX", "XL", "XC", "CD", "CM"):
            result += alph_rn[sym]
            number = number.replace(alph_rn[sym], "")

    for sym in number:
        result += alph_rn[sym]

    return result


def from_numeral_to_roman_converter(number: int) -> str:
    if number > 3999:
        raise ValueError("Нельзя передавать числа большие 3999")

    result = ""

    for dec in range(1, 5):
        rem = number % 10 ** dec

        if rem == 0:
            continue
        elif rem in (4, 9, 40, 90, 400, 900):
            result += alph_nr[rem]
            number -= rem
        else:
            if rem / 10 ** (dec - 1) > 5:
                result += alph_nr[5 * 10 ** (dec - 1)]
                rem -= 5 * 10 ** (dec - 1)

            result += alph_nr[10 ** (dec - 1)] * (rem // 10 ** (dec - 1))

    return result[::-1]


print(from_roman_to_numeral_converter("MMMXXXL"))
print(from_numeral_to_roman_converter(3080))
"""


#   Задача #6 – виселица


gallows = [
    ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["|", " ", " ", " ", "|", " ", " ", " ", "|"],
    ["|", " ", " ", " ", "|", " ", " ", " ", "|"],
    ["|", " ", " ", "(", " ", ")", " ", " ", "|"],
    ["|", " ", " ", "/", "|", chr(92), " ", " ", "|"],
    ["|", " ", " ", "/", " ", chr(92), " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", "|"]
]

attempts = [
    [(6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (6, 8), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), "|", 1],
    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), "_", 1],
    [(1, 4), (2, 4), "|", 1],
    [(3, 3), (3, 5), "(", ")", 2],
    [(4, 4), "|", 1],
    [(4, 3), (4, 5), "/", chr(92), 2],
    [(5, 3), (5, 5), "/", chr(92), 2]
]


