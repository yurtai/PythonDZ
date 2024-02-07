from logger import input_data, print_data 
from functions_new import edit_data, delete_data

def interface():
    print("Здравствуйте! Вы попали на специальный бот от Geekbrains! \n\n1 - запись данных; \n2 - вывод данных; \n3 - изменение данных; \n4 - удаление данных")
    command = int(input("введите число: "))

    while command not in [1, 2, 3, 4]:
        print("неправильный ввод")
        command = int(input("введите число: "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        edit_data()
    elif command == 4:
        delete_data()

