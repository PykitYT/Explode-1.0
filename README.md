# Функции 
+ Добавление команд
+ Работа с файлами
# Как добавить команду?
Переходите в папку explode/addins
Создайте <имя функции>.py
Напишите скрипт который спрашавает
Для запуска введите в терминал:
![image](https://github.com/user-attachments/assets/39e37b30-b587-42c5-aeea-6a405c658155)
# Готовые команды в addins
![image](https://github.com/user-attachments/assets/a3295aa3-c818-4518-932f-9ff381afb88b)
# Что такое explode?
Explode - программа для создания функцей для терминала. Можно работать с файлами, не зная batch. Все просто!
# Пример как пользаватся Explode
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
Показавает функции из addins.
Как работает list:
```
import os
print("List of addins for explode:", os.listdir("./addins:))
```
---
Команда:
```
explode
```
Вывод:

Welcome to explode.exe!
Commands:
    -run Run python code (1 line)
    -newfile Create file with text (1 line)
    -readfile Read file
    -addin Run functions from addins/

---
# Спасибо, то что скачали Explode!
