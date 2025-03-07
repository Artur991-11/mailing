from tkinter import Tk, Label
from PIL import Image, ImageTk

root = Tk()

   # Загрузка изображения с использованием Pillow
Bell_image = Image.open("bell.png")
Bell_image = Bell_image.resize((128, 128))  # Убедитесь, что вы задаете нужный размер
Bell_image = ImageTk.PhotoImage(Bell_image)  # Преобразование изображения для Tkinter

   # Создание виджета Label с изображением
Bell_label = Label(image=Bell_image, bg="#ffffff")
Bell_label.pack()

root.mainloop()