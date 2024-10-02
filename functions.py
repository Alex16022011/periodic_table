def send_data(*args, **kwargs) -> list:
    # print(f'{args=}\n{kwargs=}')
    number, name, letter, pronounce, atom_number = args 
    if number.isdigit() and name.isalpha() and  letter.isalpha() and pronounce.isalpha() and atom_number.isdigit():
        return [number,
            name,
            letter,
            pronounce,
            atom_number]
    print('error')
    return 'Error'