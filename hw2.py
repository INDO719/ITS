#   Задача #1 – шифр Цезаря

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

def roman_numeral_converter()


