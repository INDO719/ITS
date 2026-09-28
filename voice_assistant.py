import os

import asyncio
import threading

import tkinter as tk
from tkinter.constants import CENTER

import speech_recognition as sr
import pyttsx3 as pt

from deep_translator import GoogleTranslator


class PathWork:
    def __init__(self, start_point='C:\\Users\\Kilin_Ivan\\'):
        self.start_point = start_point
        self.list_of_path = [self.start_point]
        self.list_of_types = ['.txt', '.docx', '.doc', '.rtf', '.odt', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.svg', '.mp3', '.wav', '.aac', '.flac', 'mp4', '.avi', '.mvk', '.mov', '.exe', '.bat', '.sh', '.zip', '.rar', '.7z', '.pdf', '.html', '.htm', '.csv', '.xml', '.json', '.torrent', '']

        self.translator = GoogleTranslator(source='ru', target='en')

    def search(self, path):
        list_of_dirs = os.listdir(self.list_of_path[-1])

        for file in list_of_dirs:
            for type in self.list_of_types:
                if type in file:
                    type_of_file = type
                    file_without_t = file.replace(type_of_file, '')

                    file_translate = self.translator.translate(file_without_t)

                    if file_without_t.lower() == path or file_translate.lower() == path:
                        self.list_of_path.append(os.path.join(self.list_of_path[-1], file_without_t+type_of_file))
                        return 0

    def open(self, path):
        self.search(path)

        if self.list_of_path[-1]:
            os.startfile(self.list_of_path[-1])

    def go_back(self):
        if len(self.list_of_path) > 1:
            if self.list_of_path[-2]:
                os.startfile(self.list_of_path[-2])
                self.list_of_path.pop()
        else:
            back_path = "\\".join(self.list_of_path[0].split("\\")[:2])
            os.startfile(back_path)

    def delete_make(self, name, type, destroy=False):
        path = os.path.join(self.list_of_path[-1], name)

        if type == 0:
            if not destroy:
                if not os.path.exists(path):
                    os.makedirs(path)
                    print("Папка создана")
            else:
                if os.path.exists(path):
                    os.rmdir(path)
                    print("Папка удалена")
        elif type == 1:
            if not destroy:
                if not os.path.exists(path):
                    with open(path, "w") as file:
                        print("Файл создан")
            else:
                if os.path.exists(path):
                    os.remove(path)
                    print("Файл удален")

class Assistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()

        self.engine = pt.init()

        self.file_work = PathWork()

        self.is_computer = False

        #Списки команд
        self.list_of_appeals = ['инду', 'end', 'indoor', 'инда', 'эндер', 'эндо', 'inde', 'индо', 'indo']

        self.list_work_with_file = ['открой компьютер', 'зайди в компьютер']

        self.list_of_open = ['открой файл', 'запусти файл', 'зайди в файл', 'открой папку', 'зайди в папку']

        self.list_make_f = ['создай файл', 'сделай файл']
        self.list_delete_f = ['удали файл', 'сотри файл', 'уничтожь файл']

        self.list_make_d = ['создай папку', 'сделай папку']
        self.list_delete_d = ['удали папку', 'сотри папку', 'уничтожь папку']

    async def audio(self, phrase):
        self.engine.say(phrase)
        self.engine.runAndWait()

    async def listen_to_user(self, phrase="", is_appeal=False):
        with sr.Microphone() as source:
            print(phrase)
            audio = self.recognizer.listen(source, 10, 20)

        try:
            speech = self.recognizer.recognize_google(audio, language="ru-Ru").lower()
            return speech
        except sr.UnknownValueError:
            print("Не смогли распознать речь")
        except sr.RequestError as e:
            print("Нет подключения к сети")

    async def translate(self):
        while True:
            speech_from_listening = await self.listen_to_user("Говорите")

            if speech_from_listening in self.list_of_appeals:
                speech_after_appeal = await self.listen_to_user("Да, я вас слушаю", True)
                print(speech_after_appeal)
                await self.answer_to_user(speech_after_appeal)

    async def answer_to_user(self, phrase):
        if not self.is_computer:
            if phrase in self.list_work_with_file:
                print("Открываю компьютер")
                self.file_work.open('')
                self.is_computer = True
        else:
            if phrase in self.list_of_open:
                print("Открываю")
                file = await self.listen_to_user("Что вы хотите открыть?")
                self.file_work.open(file)
            elif phrase in self.list_make_f:
                print("Создаю файл")
            elif phrase in self.list_delete_f:
                print("Удаляю файл")
            elif phrase in self.list_make_d:
                print("Создаю папку")
            elif phrase in self.list_delete_d:
                print("Удаляю папку")
            else:
                print("Команда не распознана")

class Window:
    def __init__(self, title, width, height, resizable=False):
        self.title = title
        self._width = width
        self._height = height

        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry(f"{self._width}x{self._height}")
        self.window.resizable(resizable, resizable)

        self.assistant = Assistant()
        self.loop = asyncio.new_event_loop()  # Создаем новый цикл событий

    def setup(self):
        txt_wl = "Добро Пожаловать!"
        txt_welcome = tk.Label(text=txt_wl, font=("Arial Black", 20), justify=CENTER)
        txt_welcome.pack()

        # Обработчик для кнопки (синхронная обертка)
        def start_listening():
            asyncio.run_coroutine_threadsafe(self.assistant.translate(), self.loop)

        btn_start = tk.Button(text="Запуск", width=15, height=2, font=("Arial Black", 15), background="#7DF49D", activebackground="#B1F9C5", command=start_listening)  # Используем синхронную обертку
        btn_start.place(x=90, y=70)

        btn_setting = tk.Button(text="Настройки", width=15, height=2, font=("Arial Black", 15), background="#D3D3D3", activebackground="#E0E0E0")
        btn_setting.place(x=90, y=170)

        # Запускаем цикл asyncio в отдельном потоке
        threading.Thread(target=self.loop.run_forever, daemon=True).start()


def main():
    window = Window('Voice Assistant', 400, 300)
    window.setup()
    window.window.mainloop()
    window.loop.call_soon_threadsafe(window.loop.stop)  # Корректное завершение

if __name__ == '__main__':
    main()
