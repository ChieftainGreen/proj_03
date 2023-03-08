"""Youtube downloader"""

# план развития:
# 0. скопировать https://www.youtube.com/watch?v=cWmGXWlKKzE
# 1. базовый функционал в режиме диалога - ввод url, скачивание, сохранение в файл, вывод имени
# 2. обрезка url, проверка имени файла, может быть сообщения об ошибках
# 2.1 старт по энтеру при вооде url - готово, on_submit в TextField
# 3 GUI - готово сразу
# 3.1 progress bar, сообщения о выполнении
# 4 сборка в exe-файл


import backend
import gui

gui.run_backend = backend.get_video
gui.run_gui()