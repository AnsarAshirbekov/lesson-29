# а) Сделать набросок дизайна программы в figma / paint для программы, которая делает
# запрос на сайт jsonplaceholder.
# б) Разработать эту программу на библиотеке pyqt6 в стиле ООП.
# в) Реализовать сохранение полученных объектов в папку.

# Проделываем все тоже самое, что и в задаче предыдущей домашки, но только с использованием вместо tkinter PyQt6

import requests
import os
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton

# Создаем главный класс окна, который будет наследоваться от класса QMainWindow, который в свою очередь предоставляет
# функционал для создания оконных интерфейсов
class MainWindow(QMainWindow):
    # Создаем конструктор
    def __init__(self):
        # Перенимаем функционал от родительского класса..
        super().__init__()
        # и устанавливаем все то, что будет находиться внутри окна:
        # Установка заголовка окна
        self.setWindowTitle('JSON download')
        # Установка размера окна (200x100) первые две цифры это координаты по х и у
        self.setGeometry(100, 100, 200, 100)
        # Создание основного виджета
        self.widget = QWidget()
        # Прописываем ему установку с верхнего края окна, можно установить и посередине, прописав .setCentralWidget()
        self.setMenuWidget(self.widget)
        # Создание главного макета, то есть расположение элементов внутри виджета, QVBoxLayout - элементы будут 
        # распологаться по вертикали (V), QHBoxLayout - по горизонатали (Н) 
        self.main_layout = QVBoxLayout()
        # Прописываем установку макета внутри виджета
        self.widget.setLayout(self.main_layout)
        # Создаем бирку
        self.label = QLabel()
        # Прописываем текст для бирки
        self.label.setText('Загрузка JSON')
        # Устанавливаем бирку внутри макета
        self.main_layout.addWidget(self.label)
        # Создаем кнопку
        self.button = QPushButton('Загрузить')
        # Устанавливаем кнопку внутри макета
        self.main_layout.addWidget(self.button)
        # Привязываем к кнопке по клику срабатывание функции json_download
        self.button.clicked.connect(self.json_download)

    # Прописываем функцию для создания папки с JSON-файлами
    def json_download(self):
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        data = response.json()
        current_dir = os.getcwd()
        folder_name = 'JSON Folder'
        path = os.path.join(current_dir, folder_name)
        os.makedirs(path, exist_ok=True)
        for d in data:
            file_name = f'data_{d["id"]}.json'
            file_path = os.path.join(path, file_name)
            with open(file_path, 'w') as file:
                json.dump(d, file)

# Чтобы открыть и использовать это окно, нужно создать для него приложение, которое будет его запускать в рамках какого-то
# цикла событий. Для этого создаем объект приложения и передаем ему пустой список. Обычно он принимает аргументы командной
# строки - sys.argv , но так как у нас простейшее приложение, не принимающее никаких аргументов, то можно передать пустой
# список как заглушку
app = QApplication([])
# Теперь после того, как мы инициализировали приложение, у нас появилась его среда, внутри которой мы можем прописывать 
# окна и виджеты и все они будут регистрироваться в контексте текущего экземпляра QApplication
# Теперь создаем окно
window = MainWindow()
# Отображаем его
window.show()
# Затем запускаем основной цикл событий, который управляет всеми событиями пользовательского интерфейса (например, 
# нажатиями клавиш, движениями мыши и т. д.) и поддерживает приложение активным, пока оно не будет закрыто.
app.exec()