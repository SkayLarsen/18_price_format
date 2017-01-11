# Price Formatter

Скрипт приводит запись цены товара в конкретный, удобный для отображения формат.

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

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
