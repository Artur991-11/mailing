import tkinter as tk
import tkinter.messagebox
import pyperclip  # Для работы с буфером обмена (clipboard)

def insert_text():
    """Вставляет текст из буфера обмена в текстовое поле."""
    try:
        clipboard_content = pyperclip.paste()
        text_widget.insert(tk.INSERT, clipboard_content)
    except pyperclip.PyperclipException:
        tk.messagebox.showerror("Ошибка", "Не удалось получить доступ к буферу обмена. Установите xclip или xsel.")


root = tk.Tk()
root.title("Вставить текст")

# Создание текстового поля
text_widget = tk.Text(root, wrap=tk.WORD, width=50, height=10)
text_widget.pack(pady=10)

# Создание кнопки "Вставить текст"
insert_button = tk.Button(root, text="Вставить текст", command=insert_text)
insert_button.pack(pady=5)

root.mainloop()