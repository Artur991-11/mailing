import tkinter as tk
from tkinter import Grid
import tkinter.messagebox
import pyperclip 
from PIL import Image, ImageTk, ImageDraw
from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio
import os
from functools import partial  
import pandas as pd
import openpyxl


#os.environ['TCL_LIBRARY'] = r"c:\Users\Artur\Desktop\рассылка\.venv\Lib\site-packages"
#def create_gradient_image(width, height, color1, color2, orientation="vertical"):
##    image = Image.new("RGB", (width, height), color1)
 #   draw = ImageDraw.Draw(image)
#   steps = 256
  #  if orientation == "vertical":
   #     for i in range(steps):
    #        r = int(int(color1[1:3], 16) * (steps - i) / steps + int(color2[1:3], 16) * i / steps)
     #       g = int(int(color1[3:5], 16) * (steps - i) / steps + int(color2[3:5], 16) * i / steps)
      #      b = int(int(color1[5:7], 16) * (steps - i) / steps + int(color2[5:7], 16) * i / steps)
       #     color = (r, g, b)
        #    y1 = int(i * height / steps)
         #   y2 = int((i + 1) * height / steps)
          #  draw.rectangle((0, y1, width, y2), fill=color)
    #elif orientation == "horizontal":
     #   for i in range(steps):
      #      r = int(int(color1[1:3], 16) * (steps - i) / steps + int(color2[1:3], 16) * i / steps)
       #     g = int(int(color1[3:5], 16) * (steps - i) / steps + int(color2[3:5], 16) * i / steps)
        #    b = int(int(color1[5:7], 16) * (steps - i) / steps + int(color2[5:7], 16) * i / steps)
         #   color = (r, g, b)
          #  x1 = int(i * width / steps)
           # x2 = int((i + 1) * width / steps)
           # draw.rectangle((x1, 0, x2, height), fill=color)
   # else:
    #    raise ValueError("Недопустимая ориентация.  Допустимые значения: 'vertical' или 'horizontal'")
    #return image




def insert_text():
    """Вставляет текст из буфера обмена в текстовое поле."""
    try:
        clipboard_content = pyperclip.paste()
        text_widget.insert(tk.INSERT, clipboard_content)
    except pyperclip.PyperclipException:
        tk.messagebox.showerror("Ошибка", "Не удалось получить доступ к буферу обмена. Установите xclip или xsel.")


file_path = r"C:\Users\Artur\Desktop\рассылка\testMailing.xlsx"

try:
    df = pd.read_excel(file_path)

    
    first_column = df.iloc[:, 0]
    first_column_list = first_column.tolist()


except FileNotFoundError:
    print(f"Ошибка: Файл '{file_path}' не найден.")
except pd.errors.EmptyDataError:
    print(f"Ошибка: Файл '{file_path}' пуст или не содержит данных.")
except Exception as e:
    print(f"Произошла ошибка при чтении файла '{file_path}': {e}")

root = tk.Tk()
root.title("Mailing")
root.geometry("800x500")


width = 800
height = 500
#gradient_image = create_gradient_image(width, height, "#37474f", "#E0E0E0", orientation="horizontal")
#gradient_photo = ImageTk.PhotoImage(gradient_image)
#gradient_label = tk.Label(root, image=gradient_photo)
#gradient_label.image = gradient_photo
#gradient_label.grid(row=0, column=0, columnspan=3, sticky="ew")


frame = tk.Frame(root, padx=50, pady=30, bg="#E3DAC9")
frame.grid(row=1, column=0, columnspan=3, sticky="nsew")

label = tk.Label(frame, text="Business Technology Mailing List_1", bg="#E3DAC9", font=("Ferro Rosso", 15))
label.grid(row=0, column=0, sticky="w", padx=10)



#def text_changed(event):
 #   """Функция, вызываемая при изменении текста."""
 #   global text_content
#    text_content = text_widget.get("1.0", tk.END).strip()
#    print(f"Текст изменен: {text_content}")



def text_changed(event):
    global text_content
    """Функция, вызываемая при изменении текста. Обновляет переменную words."""
    global words  # Используем global, если words объявлена вне функции
    text_content = text_widget.get("1.0", tk.END).strip()  # Получаем текст
    words = text_content.split()  # Разделяем текст на слова
    print(f"Слова: {words}")  # Отладочный вывод


# Создаем текстовое поле
text_widget = tk.Text(root, width=40, height=10, wrap="word")
text_widget.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # row и column укажите нужные вам

# Привязываем событие KeyRelease к текстовому полю
text_widget.bind("<KeyRelease>", text_changed)
async def send_message_to_multiple_users(client, message, recipients):
    """Отправляет сообщение списку получателей."""
    for recipient in recipients:
        try:
            await client.send_message(recipient, message)
            print(f"Сообщение отправлено пользователю: {recipient}")
        except Exception as e:
            print(f"Ошибка отправки пользователю {recipient}: {e}")



async def main():
    api_id = 22638043
    api_hash = 'de57d44ad69ff08cd19359ed5e87fba9'
    session_name = "myTelegram"
    device_model = 'B560 HD3'
    system_version = "22H2"
    app_version = '5.11.1.0'

    #recipients = [
    #    "@Harius_Harris",
    #    "@Volzhets",
    #    -1002117735497
    #]
    #message = "Привет! сообщение рассылается нескольким пользовалтелям, пока что только сс заранее заговленным в ручную списком!"


    session_string = os.environ.get(session_name)

    client = TelegramClient(StringSession(session_string), api_id, api_hash,
                            system_version=system_version,
                            device_model=device_model,
                            app_version=app_version)

    async with client:
        await client.connect() 

        if not await client.is_user_authorized():
            print("Пользователь не авторизован.  Необходимо пройти аутентификацию.")
            return
        await send_message_to_multiple_users(client, text_content, first_column)
    print("Отправка завершена.")

def run_async_main():
    asyncio.run(main())
button1 =  tk.Button(frame, text="xnj nj", command=insert_text)
button1.grid(row=1, column=2)
button = tk.Button(frame, pady=8, padx=10, font=("EB Garamond", 15), text="send", bg="#E3DAC9", command=run_async_main)
button.grid(row=1, column=1, sticky="e", padx=10)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)  
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()