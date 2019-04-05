# trassir_script_framework

Фреймворк для скриптов автоматизации [Trassir](https://www.dssl.ru/)

## Getting Started

Для правильной работы методов фреймворка - обновите 
**Trassir** до *v4.1.131435* или новее.

### Installing

Передите в настрйоки Trassir -> Автоматизация -> Новый скрипт

Скопируйте в редакторв содержимое файла 
[trassir_script_framework.py](trassir_script_framework.py)

Измените автора ``AATrubilin`` и имя скрипта ``trassir_script_framework`` и версию ``0.1b``

```python
# -*- coding: utf-8 -*-
"""
<parameters>
    <company>AATrubilin</company>
    <title>trassir_script_framework</title>
    <version>0.1b</version>
</parameters>
"""
```

### Examples

```python
>>> # Вывод имени текущего скрипта
>>> name = BaseUtils.get_script_name()
>>> host.message(name)
'Новый скрипт'
```

```python
>>> # Создание/поиск шаблона с именем "New template"
>>> template = Template("New template")
>>>
>>> # Добавление минибраузера со вкладкой google.com
>>> template.content = "minibrowser(0,htmltab(,https://www.google.com/))"
>>> template.show(1)
```

Больше примеров:
 * в папке [examples](examples);
 * в [базе знаний](https://confluence.trassir.com/display/WD/Script+DSSL) DSSL;
 * в [документации](https://www.dssl.ru/files/trassir/manual/ru/setup-rules-examples.html) к ПО;
 * в [документации](https://trassir_script_framework.readthedocs.io/) к фреймворку.

## Authors

* **A.A.Trubilin** - [AATrubilin](https://github.com/AATrubilin)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details
