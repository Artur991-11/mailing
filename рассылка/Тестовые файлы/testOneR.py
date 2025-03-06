#import tkinter as tk
#root = tk.Tk()
#root.title("Mailing")
#root.geometry("800x500")
import tkinter as tk
from PIL import Image, ImageTk

def set_background(window, image_path):
    """Устанавливает фоновое изображение для окна Tkinter с использованием Canvas."""
    try:
        img = Image.open(image_path)
        bg_image = ImageTk.PhotoImage(img)  # PIL Image -> Tkinter PhotoImage

        # Создаем Canvas, заполняющий все окно
        bg_canvas = tk.Canvas(window, width=bg_image.width(), height=bg_image.height())
        bg_canvas.pack(fill="both", expand=True) # Заполняет окно и растягивается при изменении размера

        # Устанавливаем изображение на Canvas
        bg_canvas.create_image(0, 0, image=bg_image, anchor="nw") # anchor="nw" для верхнего левого угла

        # Сохраняем ссылку на bg_image, чтобы сборщик мусора ее не удалил. Важно!
        bg_canvas.bg_image = bg_image  # Храним ссылку

        # Обеспечиваем, чтобы элементы располагались поверх фона
        return bg_canvas
    except FileNotFoundError:
        print(f"Ошибка: Изображение не найдено по пути: {image_path}")
        return None  # Или создайте пустой Canvas, если хотите продолжить

def add_widget_to_background(background_canvas, widget):
    """Добавляет виджет на задний фон."""
    background_canvas.create_window(0, 0, window=widget, anchor="nw")

# Пример использования
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Фон с Canvas")

    # Устанавливаем размер окна
    root.geometry("800x600")

    # Устанавливаем фоновое изображение. Замените "path/to/your/image.jpg" на реальный путь
    background_canvas = set_background(root, "path/to/your/image.jpg")

    if background_canvas:
        # Создаем виджет, который будем размещать на фоне
        label = tk.Label(root, text="Текст поверх фона", bg="white", font=("Arial", 16))
        add_widget_to_background(background_canvas, label) #размещаем лейбл

        # Запускаем главный цикл обработки событий
        root.mainloop()
    else:
        print("Не удалось установить фон.  Завершение программы.")