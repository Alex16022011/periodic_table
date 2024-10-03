from customtkinter import *

counter = 0

def send_data(window, *args, **kwargs) -> list:
    global counter
    lbl_error = CTkLabel(master=window, text='Заполните правильно все поля!', font=('Arial', 25), bg_color='green', fg_color='red')
    # print(f'{args=}\n{kwargs=}')
    number, name, letter, pronounce, atom_number, met_ne_met = [i.get() for i in args]
    if number.isdigit() and name.isalpha() and  letter.isalpha() and pronounce.isalpha() and atom_number.isdigit() and met_ne_met.isalpha():
        if counter == 1:
            lbl_error.destroy()
        for i in args:
            i.delete(0, END)
        return [number,
            name,
            letter,
            pronounce,
            atom_number]
    lbl_error.grid(row=3, column=1, columnspan=4, padx=(10, 10), pady=(30, 30))
    counter = 1
    print('error')
    return 'Error'

