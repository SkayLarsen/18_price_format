# Price Formatter

Скрипт приводит запись цены товара в конкретный, удобный для отображения формат.  
К примеру, запись вида 3245.000000 будет приведена к более наглядному виду: 3 245   
В случае, если преобразование записи выполнить не удаётся, выводится сообщение "Ошибка".

Допускает два варианта использования:
* Прямой запуск из консоли
```bash
python format_price.py price
```
* Импортирование функции проверки в сторонний скрипт:

```
from format_price import format_price
```

Также, включён набор тестов для проверки корректности работы скрипта. Тесты доступны в файле tests.py
```
python tests.py
```

Примеры вывода скрипта:

```bash
python format_price.py 12502,279
12 502.28
python format_price.py 24r7.12
Ошибка

```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
