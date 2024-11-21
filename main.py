import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password(length, use_lowercase, use_digits, use_special):
    chars = ""
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%"

    if not chars:
        messagebox.showwarning("Warning", "Выберите хотя бы один тип символов!")
        return ""

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def on_generate():
    length = int(entry_length.get())
    use_lowercase = var_lowercase.get()
    use_digits = var_digits.get()
    use_special = var_special.get()

    password = generate_password(length, use_lowercase, use_digits, use_special)
    label_result.config(text=password)


# Создание основного окна
root = tk.Tk()
root.title("Генератор паролей")

# Поле ввода длины пароля
label_length = tk.Label(root, text="Длина пароля:")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()
entry_length.insert(0, "12")  # Значение по умолчанию

# Чекбоксы для выбора параметров
var_lowercase = tk.BooleanVar()
checkbox_lowercase = tk.Checkbutton(root, text="Включить нижний регистр [a-z]", variable=var_lowercase)
checkbox_lowercase.pack()

var_digits = tk.BooleanVar()
checkbox_digits = tk.Checkbutton(root, text="Включить цифры [0-9]", variable=var_digits)
checkbox_digits.pack()

var_special = tk.BooleanVar()
checkbox_special = tk.Checkbutton(root, text="Включить спецсимволы [!@#$%]", variable=var_special)
checkbox_special.pack()

# Кнопка генерации пароля
button_generate = tk.Button(root, text="Сгенерировать пароль", command=on_generate)
button_generate.pack()

# Метка для отображения результата
label_result = tk.Label(root, text="", font=("Helvetica", 16))
label_result.pack()

# Запуск основного цикла приложения
root.mainloop()
