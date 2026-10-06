import os
from deep_translator import GoogleTranslator


class PathWork:
    def __init__(self, start_point='C:\\Users\\'):
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

                    translate_file = self.translator.translate(file_without_t)

                    if file_without_t.lower() == path or translate_file.lower() == path:
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
    def close(self, name, type, status):
        if not status:
            print(f"{name} закрыт")
