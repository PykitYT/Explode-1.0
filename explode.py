import sys
import os

# Функция для загрузки и выполнения скриптов из папки addins
def load_addin(command_name):
    addins_folder = 'addins'
    addin_path = os.path.join(addins_folder, f'{command_name}.py')

    # Проверяем, существует ли файл
    if os.path.exists(addin_path):
        try:
            # Выполняем скрипт из папки addins
            exec(open(addin_path).read())
            print(f"Команда {command_name} успешно выполнена.")
        except Exception as e:
            print(f"Ошибка при выполнении команды из addins: {e}")
    else:
        print(f"Команда {command_name} не найдена в папке addins!")

# Получаем входной параметр
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Присваиваем переменной inputs строку, которую ввел пользователь
        inputs = " ".join(sys.argv[1:])
        
        # Разделяем строку на части по пробелу
        inputs = inputs.split()
        
        # Получаем тип команды
        command_type = inputs[0]
        
        # Удаляем команду из списка аргументов
        del inputs[0]
        
        if command_type == "-run":
            # Выполняем команду, если она существует в inputs[0]
            try:
                # Мы используем exec, но стоит быть осторожным с этим методом
                exec(" ".join(inputs))
            except Exception as e:
                print(f"Ошибка при выполнении кода: {e}")
        elif command_type == "-newfile":
            name = input("Name> ")
            text = input("Text> ")
            with open(name, "w") as file:
                file.write(text)
        elif command_type == "-readfile":
            name = input("Name> ")
            with open(name, 'r') as file:
                print(file.read())
        elif command_type == "-addin":
            if len(inputs) > 0:
                # Выполняем команду из папки addins
                load_addin(inputs[0])
        else:
            print("Invalid type!")
        
        # Место для других команд
        # Например, можно добавить другие команды:
        # elif inputs[0] == "multiply":
        #    ...  # Код для выполнения умножения

    else:
        print("""
Welcome to explode.exe!
Commands:
    -run Run python code (1 line)
    -newfile Create file with text (1 line)
    -readfile Read file
    -addin Run functions from addins/
""")
