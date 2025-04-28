# Функции 
+ Добавление команд
+ Работа с файлами

# Как добавить команду?
1. Перейдите в папку `explode/addins`.
2. Создайте файл с именем `<имя функции>.py`.
3. Напишите скрипт, который будет выполнять требуемые действия.
4. Для запуска введите в терминал команду:
   ![image](https://github.com/user-attachments/assets/39e37b30-b587-42c5-aeea-6a405c658155)

# Готовые команды в `addins`
![image](https://github.com/user-attachments/assets/a3295aa3-c818-4518-932f-9ff381afb88b)

# Что такое Explode?
Explode — это программа для создания функций для терминала. Можно работать с файлами, не зная Batch. Все просто!

# Пример использования Explode
Команда:
```
explode -addin HACKED_BIOS
```
![image](https://github.com/user-attachments/assets/05b48571-eec9-461f-8289-0e9613f82610)

---

Команда:
```
explode -addin list
```
Показывает функции из папки `addins`.

Как работает `list`:
```python
import os
print("List of addins for explode:", os.listdir("./addins"))
```

---

Команда:
```
explode
```
Вывод:
```
Welcome to explode.exe!
Commands:
    -run     Run Python code (1 line)
    -newfile Create file with text (1 line)
    -readfile Read file
    -addin   Run functions from addins/
```

---
# Explode-installer
Установка:

Скачайте файл explode-installer.exe

Добавьте в explode/

Как пользаватся:
скачайте нужный архив 
и вот следушие команды который вам нужно ввести:
![image](https://github.com/user-attachments/assets/351c57f0-6a02-46fd-8f29-da290073d41e)
теперь вы можете открыть через
```
explode -addin <имя>
```
# Спасибо, что скачали Explode!
