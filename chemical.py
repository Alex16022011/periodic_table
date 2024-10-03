import sys

sys.path.append('.')
from customtkinter import *
from list_of_data import list_of_elements
from functions import send_data

root = CTk()

root.geometry('1150x500+50+100')
root.resizable(0, 0)
root.config(bg='green')


def get_a_file():
    pass


def destroy_all_from_screen(root, method: str) -> None:
    method = method.lower()
    list1 = []
    if method == 'pack':
        list1 = root.pack_slaves()
    elif method == 'grid':
        list1 = root.grid_slaves()
    elif method == 'place':
        list1 = root.slaves()
    for i in list1:
        i.destroy()


def program():

    name_0 = CTkLabel(master=root, text='Номер', font=('Arial', 25), bg_color='green', fg_color='green')
    name_0.grid(row=0, column=0, padx=(10, 10))

    name_1 = CTkLabel(master=root, text='Название', font=('Arial', 25), bg_color='green', fg_color='green')
    name_1.grid(row=0, column=1, padx=(10, 10))

    name_2 = CTkLabel(master=root, text='Обозначение', font=('Arial', 25), bg_color='green', fg_color='green')
    name_2.grid(row=0, column=2, padx=(10, 10))

    name_3 = CTkLabel(master=root, text='Произношение', font=('Arial', 25), bg_color='green', fg_color='green')
    name_3.grid(row=0, column=3, padx=(10, 10))

    name_4 = CTkLabel(master=root, text='Атомный номер', font=('Arial', 25), bg_color='green', fg_color='green')
    name_4.grid(row=0, column=4, padx=(10, 10))

    name_5 = CTkLabel(master=root, text='Металл/Не металл', font=('Arial', 25), bg_color='green', fg_color='green')
    name_5.grid(row=0, column=5, padx=(10, 10))





    number = CTkEntry(master=root, font=('Arial', 25), bg_color='green', corner_radius=300)
    number.grid(row=1, column=0, padx=(10, 10))

    name = CTkEntry(master=root, font=('Arial', 25), bg_color='green', corner_radius=300)
    name.grid(row=1, column=1, padx=(10, 10))

    letter = CTkEntry(master=root, font=('Arial', 25), bg_color='green', corner_radius=300)
    letter.grid(row=1, column=2, padx=(10, 10))

    pronounce = CTkEntry(master=root, font=('Arial', 25), bg_color='green', corner_radius=300)
    pronounce.grid(row=1, column=3, padx=(10, 10))

    atom_number = CTkEntry(master=root, font=('Arial', 25), bg_color='green', corner_radius=300)
    atom_number.grid(row=1, column=4, padx=(10, 10))

    met_ne_met = CTkEntry(master=root, font=('Arial', 25), bg_color='green', corner_radius=300)
    met_ne_met.grid(row=1, column=5, padx=(10, 10))

    send = CTkButton(master=root, text='Отправить', font=('Arial', 25), bg_color='green', corner_radius=300, command=lambda: send_data(root,
                                                                                                                                    number, 
                                                                                                                                    name, 
                                                                                                                                    letter, 
                                                                                                                                    pronounce, 
                                                                                                                                    atom_number,
                                                                                                                                    met_ne_met))

    send.grid(row=2, column=2, columnspan=2, pady=(40, 0))


get_a_file()
destroy_all_from_screen(root, 'grid')
program()

root.mainloop()