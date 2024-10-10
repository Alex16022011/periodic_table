import sys

sys.path.append('.')
from customtkinter import *

counter = 0
lbl_error = None  # Инициализируем lbl_error как None

def send_data(window, *args, **kwargs) -> list:
    """
    Обрабатывает данные из полей ввода и выводит ошибку, если поля заполнены некорректно.

    Args:
        window: Окно, в котором отображается ошибка.
        *args: Список полей ввода.

    Returns:
        Список обработанных данных или 'Error' в случае ошибки.
    """
    global counter
    global lbl_error
    number, name, letter, pronounce, atom_number, met_ne_met = [i.get() for i in args]

    # Проверка на корректность ввода
    if number.isdigit() and name.isalpha() and  letter.isalpha() and pronounce.isalpha() and atom_number.isdigit() and met_ne_met.isalpha():
        if counter == 1:  # Удаляем предыдущее сообщение об ошибке
            lbl_error.destroy()
            counter = 0
        # Очистка полей ввода
        for i in args:
            i.delete(0, END)
        return [number, name, letter, pronounce, atom_number, met_ne_met]  # Возвращаем данные
    else:
        # Отображение ошибки
        lbl_error = CTkLabel(master=window, text='Заполните правильно все поля!', font=('Arial', 25), bg_color='green', fg_color='red')
        lbl_error.grid(row=3, column=1, columnspan=4, padx=(10, 10), pady=(30, 30))
        counter = 1
        return 'Error'  # Возвращаем 'Error'