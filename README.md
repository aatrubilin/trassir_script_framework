[![GitHub release](https://img.shields.io/github/release/aatrubilin/trassir_script_framework.svg)](trassir_script_framework.py)
![GitHub last commit](https://img.shields.io/github/last-commit/aatrubilin/trassir_script_framework.svg)
[![Documentation Status](https://readthedocs.org/projects/trassir-script-framework/badge/?version=latest)](https://trassir-script-framework.readthedocs.io/ru/latest/?badge=latest)
[![Build Status](https://travis-ci.org/AATrubilin/trassir_script_framework.svg?branch=master)](https://travis-ci.org/AATrubilin/trassir_script_framework)
[![License](https://img.shields.io/github/license/aatrubilin/trassir_script_framework.svg)](LICENSE.md)
[<img src="https://www.dssl.ru/upload/aspro.optimus/69d/logo.svg" height="20">](https://www.dssl.ru/)

# trassir_script_framework

Фреймворк для скриптов автоматизации [Trassir](https://www.dssl.ru/)

## Getting Started

Для правильной работы методов фреймворка - обновите 
**Trassir** до *v4.1.131435* или новее.

### Installing

Перейдите в настройки Trassir -> Автоматизация -> Новый скрипт

Скопируйте в редактор содержимое файла 
[trassir_script_framework.py](trassir_script_framework.py)

Измените автора ``AATrubilin``, имя скрипта ``trassir_script_framework`` и версию ``0.2b``

```python
# -*- coding: utf-8 -*-
"""
<parameters>
    <company>AATrubilin</company>
    <title>trassir_script_framework</title>
    <version>0.2b</version>
</parameters>
"""
```

### Examples

```python
>>> # Вывод имени текущего скрипта
>>> script_name = BaseUtils.get_script_name()
>>> script_name
'Новый скрипт'
```

```python
>>> # Поиск объекта канала "AC-D2141IR3 Склад"
>>> channels = Channels()
>>> my_channel = channels.get_enabled("AC-D2141IR3 Склад")[0]
>>>
>>> # Сохранение скриншота
>>> shot_saver = ShotSaver()
>>> shot_saver.shot(my_channel.full_guid)
'D:/DSSL/Trassir-4.1-Client/shots\AC-D2141IR3 Склад (2019.04.12 15-24-34).jpg'
```

Больше примеров и информации:
 * в папке [examples](examples);
 * в [документации](https://trassir-script-framework.readthedocs.io) к фреймворку;
 * в [базе знаний](https://confluence.trassir.com/display/WD/Script+DSSL) DSSL;
 * в [документации](https://www.dssl.ru/files/trassir/manual/ru/setup-rules-examples.html) к ПО.
 

## Authors

* **A.A.Trubilin** - [AATrubilin](https://github.com/AATrubilin)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details
