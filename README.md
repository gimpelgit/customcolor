[**English**](https://github.com/gimpelgit/customcolor/blob/main/README.md) | [Русский](https://github.com/gimpelgit/customcolor/blob/main/README-ru.md)

# Customcolor

[![license](https://img.shields.io/pypi/l/customcolor.svg)](https://pypi.org/project/customcolor/)
[![Current version on PyPI](http://img.shields.io/pypi/v/customcolor.svg)](https://pypi.org/project/customcolor/)
[![python versions](https://img.shields.io/pypi/pyversions/customcolor.svg)](https://pypi.org/project/customcolor/)

```Customcolor``` is a library for colorful output of test run information in the console when using Python's built-in ```unittest``` module.

If you're not using PyCharm but, for example, an environment like VS Code, you may have noticed that with a large number of tests, it can be difficult to quickly spot which test has failed. Moreover, it might be hard to see where the output of the failed test ends. This can make it harder to analyze test results and identify issues. That's why you might want to use the ```customcolor``` library.

## Platforms

```Customcolor``` is designed for use on Windows and Linux operating systems.

You may also try to use it on macOS, though it hasn't been tested there. If you manage to get it running, let me know — I'd be happy to update this section!

## Installation

Downloading ```customcolor``` is easy since it's available on PyPI. You can install it with the following command:

```console
pip install customcolor
```

## Usage

In essence, all the library does is create a ```ColorTestRunner``` class, which you can pass to the standard ```unittest.main()``` function.

### Example

Suppose your project has the following structure:

![](https://raw.githubusercontent.com/gimpelgit/customcolor/refs/heads/main/img/testproj.png)

And the file ```test_calc.py``` contains the following code:

```py
import unittest
from customcolor.runner import ColorTestRunner

from utils.calc import *


class MyTest(unittest.TestCase):

    def test_failed(self):
        """Test that fails"""
        self.assertEqual(add(3, 6), 11)

    def test_error(self):
        """Test that raises an error"""
        raise ValueError("Unexpected error")

    def test_ok(self):
        """Test that passes"""
        self.assertEqual(add(2, 2), 4)


if __name__ == "__main__":
    unittest.main(testRunner=ColorTestRunner(verbosity=2))
```

If you run the test the usual way, like this:

```console
python -m unittest -v tests.test_calc
```

you won't see colored output. This is because in this case, ```unittest``` uses the default classes ```TextTestRunner``` and ```TextTestResult```.

To **run the test with colored output**, you should use the command:

```console
python -m tests.test_calc
```

### Output without the library vs with the library

|   |   |
|---|---|
|<img src="https://raw.githubusercontent.com/gimpelgit/customcolor/refs/heads/main/img/en-old.png" width="350">|<img src="https://raw.githubusercontent.com/gimpelgit/customcolor/refs/heads/main/img/en-new.png" width="350">|


## Additional Features

Since this library has no dependencies and is written entirely in pure Python, it includes color print functions, which are wrappers around the standard ```print``` function.

This means if you install the library, you can use colored console output without needing to install any additional modules. However, the number of available colors might be limited for your needs.

### Example

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

### Output in cmd

<img src="https://raw.githubusercontent.com/gimpelgit/customcolor/refs/heads/main/img/print_func.png" width="130">

