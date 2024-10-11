[English](https://github.com/gimpelgit/customcolor/blob/main/README.md) | [**Русский**](https://github.com/gimpelgit/customcolor/blob/main/README-ru.md)

# Customcolor

[![license](https://img.shields.io/pypi/l/customcolor.svg)](https://pypi.org/project/customcolor/)
[![Current version on PyPI](http://img.shields.io/pypi/v/customcolor.svg)](https://pypi.org/project/customcolor/)
[![python versions](https://img.shields.io/pypi/pyversions/customcolor.svg)](https://pypi.org/project/customcolor/)

```Customcolor``` — это библиотека для цветного вывода информации о запущенных тестах в консоли при использовании стандартного модуля python ```unittest```.

Если вы не используете PyCharm, а используете например среду VS Code, то вы могли заметить, что при большом количестве тестов, вы не можете глазами достаточно быстро найти, какой именно тест у вас провалился, а также вам может быть даже трудно увидеть, где заканчивается вывод информации о провальном тесте. Это может затруднить анализ результатов тестирования и выявление ошибок. Вот почему вы можете использовать библиотеку ```customcolor```

## Платформы

```Customcolor``` предназначена для использования на операционных системах Windows и Linux.

Вы также можете попробовать использовать ее на MacOS, просто она там не тестировалась. Если у вас всё же получится ее запустить, дайте знать — я с радостью обновлю этот пункт!

## Установка

Скачать ```customcolor``` легко, так как он доступен на PyPI. Вы можете установить его с помощью следующей команды:
```console
pip install customcolor
```

## Использование

Фактически всё, что делает библиотека это создает класс ```ColorTestRunner```, который вы в дальнейшем можете передать в стандартную функцию ```unittest.main()```.

### Пример

Допустим ваш проект имеет следующую структуру

![](https://raw.githubusercontent.com/gimpelgit/customcolor/refs/heads/main/img/testproj.png)

А в файле ```test_calc.py``` содержится следующий код

```py
import unittest
from customcolor.runner import ColorTestRunner

from utils.calc import *


class MyTest(unittest.TestCase):

    def test_failed(self):
        """Тест, который провалился"""
        self.assertEqual(add(3, 6), 11)

    def test_error(self):
        """Тест ошибки"""
        raise ValueError("Неожиданная ошибка")

    def test_ok(self):
        """Тест, который прошел"""
        self.assertEqual(add(2, 2), 4)


if __name__ == "__main__":
    unittest.main(testRunner=ColorTestRunner(verbosity=2))
```

Тогда, если вы запустить тест привычным для вас образом, то есть командой

```console
python -m unittest -v tests.test_calc
```

вы не увидите цветного вывода. Это связано с тем, что в данном случае ```unittest``` использует классы по умолчанию ```TextTestRunner```, и ```TextTestResult```.

Чтобы **запустить тест с цветным выводом**, вам следует использовать команду

```console
python -m tests.test_calc
```

### Вывод без использования библиотеки и с использованием

|   |   |
|---|---|
|<img src="https://raw.githubusercontent.com/gimpelgit/customcolor/refs/heads/main/img/ru-old.png" width="350">|<img src="https://raw.githubusercontent.com/gimpelgit/customcolor/refs/heads/main/img/ru-new.png" width="350">|


## Дополнительно

Так как данная библиотека не имеет зависимостей, то есть полностью написана на голом python, то пришлось реализовать функции цветной печати, которые являются оберткой над стандартным ```print```

А значит, если вы установите библиотеку, вы получите возможность использовать цветной вывод в консоли без необходимости устанавливать дополнительные модули. Хотя количество цветов вас может не удовлетворить.

### Пример

```py
from customcolor.colors import *


print_dark_yellow("DARK_YELLOW")
print_yellow("YELLOW")
print_gray("GRAY")
print_light_gray("LIGHT_GRAY")
print_white("WHITE")
print_black("BLACK")
print_dark_blue("DARK_BLUE")
print_blue("BLUE")
print_dark_red("DARK_RED")
print_red("RED")
print_dark_green("DARK_GREEN")
print_green("GREEN")
print_dark_magenta("DARK_MAGENTA")
print_magenta("MAGENTA")
print_dark_cyan("DARK_CYAN")
print_cyan("CYAN")

color_print("GREEN", color=TextColor.GREEN)
```

### Вывод в cmd

<img src="https://raw.githubusercontent.com/gimpelgit/customcolor/refs/heads/main/img/print_func.png" width="130">