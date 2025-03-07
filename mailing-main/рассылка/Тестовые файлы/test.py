from tkinter import Tk, Text, END, Label, Frame
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import ttk

root = Tk()
root.title("расссылка интерфейс 1")
root.geometry("800x450")

image_path = r"C:\Users\admin\Desktop\mailing-main\рассылка\Тестовые файлы\Bacgraund.png"
image = Image.open(image_path)
background_image = ImageTk.PhotoImage(image)
background_label = Label(root, image=background_image)

#root.wm_attributes("-transparentcolor", "white")

logo_path = r"C:\Users\admin\Desktop\mailing-main\рассылка\Тестовые файлы\logo.jpg"
logo_image = Image.open(logo_path)
new_size = (80, 80)
resized_image = logo_image.resize(new_size, Image.LANCZOS)
logo_image_tk = ImageTk.PhotoImage(resized_image)

#bell = r"C:\Users\admin\Desktop\mailing-main\рассылка\Тестовые файлы\bell.png"
#Bell_image = Image.open(bell)
#new_size = (80, 80)
#resized_Bell = Bell_image.resize(new_size, Image.LANCZOS)
#Bell_image_image_tk = ImageTk.PhotoImage(resized_Bell)


Bell_image = Image.open("bell.png")
Bell_image = Bell_image.resize((30, 30))  
Bell_image = ImageTk.PhotoImage(Bell_image)  

Bell_label = Label(image=Bell_image, bg="#ffffff")



frameOne = tk.Frame(root, bg="#4aaa91")



frame = Frame(root, bg="#ffffff")
decor_strip = tk.Frame(root, bg="#3d3d3d")
text_widget = Text(root, width=35, height=10, wrap="word")
TextPassOne = Text(root, width=20, height=5, wrap="word")
TextPassTwo= Text(root, width=20, height=5, wrap="word")

def create_transparent_text():
    width, height = 200, 50
    image = Image.new("RGBA", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 20) 
    text1 = "Бизнес"
    text2 = "Технология"
    Bis = draw.textbbox((0, 0), text1, font=font)[2] - draw.textbbox((0, 0), text1, font=font)[0]
    draw.text((10, 30), text1, font=font, fill=(0, 0, 0, 255)) 
    draw.text((10 + Bis, 30), text2, font=font, fill=(0, 0, 0, 150)) 
    return ImageTk.PhotoImage(image)

text_image = create_transparent_text()

label = tk.Label(root, highlightthickness=0, image=text_image)
logo_label = Label(frame, image=logo_image_tk, bg="#ffffff")
Bell_label = Label(image=Bell_image, bg="#d9dadc")
logo_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
button = tk.Button(root, border=5, text="Отправить", padx=10, bg="#45ae90", fg="white", font=10)
ButtonOne = tk.Button(root, border=2, text="Вставить", padx=10, bg="#4f4f4f", fg="white", font=3)
ButtonTwo = tk.Button(root, border=2, text="Вставить", padx=10, bg="#4f4f4f", fg="white", font=3)
LabelText = tk.Label(root, text="текст сообщения", bg="#dadbdd", font=(7))

#LabelName = Label(frame, bg="#ffffff", text="БИЗНЕС ТЕХНОЛОГИИ", font=("Arial", 14))
#LabelNameOne = Label(frame, bg="#ffffff", text="Ваша уверенность в следующем шаге", font=("Arial", 10))
languages = ["Авто сервисы", "Электроника", "Одежда", "Еда"]
combobox = ttk.Combobox(values=languages)

LabelText.place(relx=0.15, rely=0.43, anchor="n")
background_label.place(relwidth=1, relheight=1)
label.place(relx=0.5, rely=0.0, anchor="center")
ButtonOne.place(relx=0.7, rely=0.55, anchor="center")
ButtonTwo.place(relx=0.7, rely=0.75, anchor="center")
button.place(relx=0.35, rely=0.9, anchor="n")
combobox.place(relx=0.17, rely=0.9, anchor="n")
frame.place(relx=0.0, rely=0.0, relwidth=1, height=110)
decor_strip.place(relx=0.0, rely=0.22, relwidth=1, height=20)
#LabelName.grid(row=0, column=1, sticky="w", padx=(0, 10))
#LabelNameOne.grid(row=1, column=1, sticky="W", padx=(0, 10), pady=(0, 0))
frame.grid_rowconfigure(0, weight=1)  
frame.grid_columnconfigure(0, weight=1)  
frame.grid_columnconfigure(1, weight=1)  
text_widget.place(relx=0.25, rely=0.5, anchor="n")
frameOne.pack(pady=20)
Bell_label.place(relx=0.09, rely=0.33, anchor="n")
TextPassOne.place(relx=0.75, rely=0.4)
TextPassTwo.place(relx=0.75, rely=0.6)
#TextPassOne.pack(padx=10, pady=10)
#Bell_label.place(relx=0.5, rely=0.5)
#TextPassTwo.pack(padx=10, pady=10)
root.mainloop()