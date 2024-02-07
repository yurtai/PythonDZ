from data_create import name_data, surname_data, phone_data, address_data

def remove_empty_lines(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if line.strip():  # проверяем, что строка не пустая
            modified_lines.append(line)

    with open(file_name, "w") as file:
        for line in modified_lines:
            file.write(line)

def edit_data():
    remove_empty_lines("data_first_var.csv")
    remove_empty_lines("data_second_var.csv")
    choice = int(input("Выберите вариант:\n1 - Изменить данные в первом файле\n2 - Изменить данные во втором файле\n"))
    while choice != 1 and choice != 2:
        print("Неправильный ввод")
        choice = int(input("Выберите вариант:\n1 - Изменить данные в первом файле\n2 - Изменить данные во втором файле\n"))

    if choice == 1:
        with open("data_first_var.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()        

        print("Доступные данные для изменения:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите изменить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки, которую хотите изменить: "))

        new_data = input("Введите новые данные: ") 

        data[line_number-1] = new_data + " \n"

        with open("data_first_var.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Спасибо, изменения сохранены")

    elif choice == 2:
        with open("data_second_var.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()            

        print("Доступные данные для изменения:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите изменить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки, которую хотите изменить: "))

        new_data = name_data() + "; " + surname_data() + "; " + phone_data() + "; " + address_data()

        data[line_number-1] = new_data + "\n"

        with open("data_second_var.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Спасибо, изменения сохранены")


def delete_data():
    choice = int(input("Выберите вариант:\n1 - Удалить данные из первого файла\n2 - Удалить данные из второго файла\n"))
    while choice != 1 and choice != 2:
        print("Неправильный ввод")
        choice = int(input("Выберите вариант:\n1 - Удалить данные из первого файла\n2 - Удалить данные из второго файла\n"))

    if choice == 1:
        with open("data_first_var.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()

        print("Доступные данные для удаления:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите удалить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки, которую хотите удалить: "))

        del data[line_number-1]

        with open("data_first_var.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Спасибо, данные удалены")

    elif choice == 2:
        with open("data_second_var.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()

        print("Доступные данные для удаления:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите удалить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки, которую хотите удалить: "))

        del data[line_number-1]

        with open("data_second_var.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Спасибо, данные удалены")

