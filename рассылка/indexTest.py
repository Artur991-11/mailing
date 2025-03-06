import tkinter as tk

def text_changed(event):
    """Функция, вызываемая при изменении текста. Обновляет переменную words."""
    global words  # Используем global, если words объявлена вне функции
    text_content = text_widget.get("1.0", tk.END).strip()  # Получаем текст
    words = text_content.split()  # Разделяем текст на слова
    print(f"Слова: {words}")  # Отладочный вывод

# Создаем окно Tkinter
root = tk.Tk()
root.title("Слова из текстового поля в переменной")

# Создаем текстовое поле
text_widget = tk.Text(root, width=40, height=10, wrap="word")
text_widget.pack(padx=10, pady=10)

# Привязываем событие KeyRelease к текстовому полю
text_widget.bind("<KeyRelease>", text_changed)

# Инициализируем переменную words (обязательно!)
words = []

root.mainloop()