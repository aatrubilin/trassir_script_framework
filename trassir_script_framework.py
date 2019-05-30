# -*- coding: utf-8 -*-
"""
<parameters>
    <company>AATrubilin</company>
    <title>trassir_script_framework</title>
    <version>0.5</version>
</parameters>
"""

import re
import os
import ssl
import time
import host
import json
import pickle
import base64
import ftplib
import urllib
import urllib2
import httplib
import logging
import threading
import subprocess

from Queue import Queue
from functools import wraps
from collections import deque
from xml.etree import ElementTree
from datetime import datetime, date, timedelta
from __builtin__ import object as py_object

VERSION = {"TITLE": "trassir_script_framework", "VERSION": 0.5}

# _SERVICE_VERSION = 0.42
tbot_service = """
    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
"""

host.exec_encoded(tbot_service)


class ScriptError(Exception):
    """Base script exception"""

    pass


class HostLogHandler(logging.Handler):
    """ Trassir main log handler """

    def __init__(self, host_api=host):
        super(HostLogHandler, self).__init__()
        self._host_api = host_api

    def emit(self, record):
        msg = self.format(record)
        self._host_api.log_message(msg)


class PopupHandler(logging.Handler):
    """ Trassir popup handler """

    def __init__(self, host_api=host):
        super(PopupHandler, self).__init__()
        self._host_api = host_api
        self._popups = {
            "CRITICAL": host_api.error,
            "FATAL": host_api.error,
            "ERROR": host_api.error,
            "WARN": host_api.alert,
            "WARNING": host_api.alert,
            "INFO": host_api.message,
            "DEBUG": host_api.message,
            "NOTSET": host_api.message,
        }

    def emit(self, record):
        msg = self.format(record)
        popup = self._popups.get(record.levelname, self._host_api.message)
        popup(msg)


class MyFileHandler(logging.Handler):
    """ My file handler """

    def __init__(self, file_path, max_mbytes=10240):
        super(MyFileHandler, self).__init__()
        self._file_path = file_path
        self._max_mbytes = max_mbytes * 1024

    def _check_size(self):
        if not os.path.isfile(self._file_path):
            return
        if os.stat(self._file_path).st_size > self._max_mbytes:
            old_file_path = self._file_path + ".old"
            if os.path.isfile(old_file_path):
                os.remove(old_file_path)
            os.rename(self._file_path, old_file_path)

    def emit(self, record):
        self._check_size()
        msg = self.format(record)
        with open(self._file_path, "a") as log_file:
            log_file.write(msg + "\n")


class BaseUtils:
    """Base utils for your scripts"""

    _host_api = host
    _FOLDERS = {obj[1]: obj[3] for obj in host.objects_list("Folder")}
    _TEXT_FILE_EXTENSIONS = [".txt", ".csv", ".log"]
    _LPR_FLAG_BITS = {
        "LPR_UP": 0x00001,
        "LPR_DOWN": 0x00002,
        "LPR_BLACKLIST": 0x00004,
        "LPR_WHITELIST": 0x00008,
        "LPR_INFO": 0x00010,
        "LPR_FIRST_LANE": 0x01000,
        "LPR_SECOND_LANE": 0x02000,
        "LPR_THIRD_LANE": 0x04000,
        "LPR_EXT_DB_ERROR": 0x00020,
        "LPR_CORRECTED": 0x00040,
    }
    _IMAGE_EXT = [".png", ".jpg", ".jpeg", ".bmp"]
    _HTML_IMG_TEMPLATE = """<img src="data:image/png;base64,{img}" {attr}>"""

    _SCR_DEFAULT_NAMES = [
        "Yeni skript",
        "Unnamed Script",
        "უსახელო სკრიპტი",
        "Жаңа скрипт",
        "Script nou",
        "Новый скрипт",
        "Yeni skript dosyası",
        "Новий скрипт",
        "未命名脚本",
    ]

    def __init__(self):
        pass

    # noinspection PyUnusedLocal
    @staticmethod
    def do_nothing(*args, **kwargs):
        """Ничего не делает.

        Returns:
            :obj:`bool`: ``True``
        """
        return True

    @classmethod
    def run_as_thread_v2(cls, locked=False, daemon=True):
        """Декоратор для запуска функций в отдельном потоке.

        Args:
            locked (:obj:`bool`, optional): Если :obj:`True` - запускает поток с блокировкой
                доступа к ресурсам. По умолчанию :obj:`False`
            daemon (:obj:`bool`, optional): Устанавливает значение :obj:`threading.Thread.daemon`.
                По умолчанию :obj:`True`

        Examples:
            >>> import time
            >>>
            >>>
            >>> @BaseUtils.run_as_thread_v2()
            >>> def run_count_timer():
            >>>     time.sleep(1)
            >>>     host.stats()["run_count"] += 1
            >>>
            >>>
            >>> run_count_timer()
        """
        lock = threading.Lock()

        def wrapped(fn):
            @wraps(fn)
            def run(*args, **kwargs):
                def raise_exc(err):
                    # noinspection PyShadowingNames
                    args = list(err.args)
                    args[0] = "[{}]: {}".format(fn.__name__, args[0])
                    err.args = args
                    raise err

                def locked_fn(*args_, **kwargs_):
                    lock.acquire()
                    try:
                        return fn(*args_, **kwargs_)
                    except Exception as err:
                        cls._host_api.timeout(1, lambda: raise_exc(err))
                    finally:
                        lock.release()

                def unlocked_fn(*args_, **kwargs_):
                    try:
                        return fn(*args_, **kwargs_)
                    except Exception as err:
                        cls._host_api.timeout(1, lambda: raise_exc(err))

                t = threading.Thread(
                    target=locked_fn if locked else unlocked_fn,
                    args=args,
                    kwargs=kwargs,
                )
                t.daemon = daemon
                t.start()
                return t

            return run

        return wrapped

    @staticmethod
    def run_as_thread(fn):
        """Декоратор для запуска функций в отдельном потоке.

        Returns:
            :obj:`threading.Thread`: Функция в отдельном потоке

        Examples:
            >>> import time
            >>>
            >>>
            >>> @BaseUtils.run_as_thread
            >>> def run_count_timer():
            >>>     time.sleep(1)
            >>>     host.stats()["run_count"] += 1
            >>>
            >>>
            >>> run_count_timer()
        """

        @wraps(fn)
        def run(*args, **kwargs):
            t = threading.Thread(target=fn, args=args, kwargs=kwargs)
            t.daemon = True
            t.start()
            return t

        return run

    @staticmethod
    def catch_request_exceptions(func):
        """Catch request errors"""

        @wraps(func)
        def wrapped(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except urllib2.HTTPError as e:
                return e.code, "HTTPError: {}".format(e.code)
            except urllib2.URLError as e:
                return e.reason, "URLError: {}".format(e.reason)
            except httplib.HTTPException as e:
                return e, "HTTPException: {}".format(e)
            except ssl.SSLError as e:
                return e.errno, "SSLError: {}".format(e)

        return wrapped

    @staticmethod
    def win_encode_path(path):
        """Изменяет кодировку на ``"cp1251"`` для WinOS.

        Args:
            path (:obj:`str`): Путь до файла или папки

        Returns:
            :obj:`str`: Декодированый путь до файла или папки

        Examples:
            >>> path = r"D:\Shots\Скриншот.jpeg"
            >>> os.path.isfile(path)
            False
            >>> os.path.isfile(BaseUtils.win_encode_path(path))
            True
        """
        if os.name == "nt":
            try:
                path = path.decode("utf8").encode("cp1251")
            except UnicodeDecodeError:
                pass

        return path

    @staticmethod
    def is_file_exists(file_path, tries=1):
        """Проверяет, существует ли файл.

        Проверка происходит в течении ``tries`` секунд.

        Warning:
            | Запускайте функцию только в отдельном потоке если ``tries > 1``
            | Вторая и последующие проверки производятся с ``time.sleep(1)``

        Args:
            file_path (:obj:`str`): Полный путь до файла
            tries (:obj:`int`, optional): Количество проверок. По умолчанию ``tries=1``

        Returns:
            :obj:`bool`: ``True`` if file exists, ``False`` otherwise

        Examples:
            >>> BaseUtils.is_file_exists("_t1server.settings")
            True
        """
        file_path_encoded = BaseUtils.win_encode_path(file_path)
        if os.path.isfile(file_path) or os.path.isfile(file_path_encoded):
            return True
        for x in xrange(tries - 1):
            time.sleep(1)
            if os.path.isfile(file_path) or os.path.isfile(file_path_encoded):
                return True
        return False

    @staticmethod
    def is_folder_exists(folder):
        """Проверяет существование папки и доступ на запись.

        Args:
            folder (:obj:`str`): Путь к папке.

        Raises:
            IOError: Если папка не существует

        Examples:
            >>> BaseUtils.is_folder_exists("/test_path")
            IOError: Folder '/test_path' is not exists
        """

        if not os.path.isdir(folder):
            raise IOError("Folder '{}' is not exists".format(folder))

        readme_file = os.path.join(folder, "readme.txt")
        with open(readme_file, "w") as f:
            f.write(
                "If you see this file - Trassir script have no access to remove it!"
            )
        os.remove(readme_file)

    @classmethod
    def is_template_exists(cls, template_name):
        """Проверяет существование шаблона

        Args:
            template_name (:obj:`str`): Имя шаблона

        Returns:
            :obj:`bool`: :obj:`True` если шаблон существует, иначе :obj:`False`
        """
        if template_name in [
            tmpl_.name for tmpl_ in cls._host_api.settings("templates").ls()
        ]:
            return True
        return False

    @classmethod
    def cat(cls, filepath, check_ext=True):
        """Выводит на отображение текстовую инфомрацию.

        Tip:
            - *WinOS*: открывает файл программой по умолчанию
            - *TrassirOS*: открывает файл в терминале с помощью утилиты `cat`

        Note:
            | Доступные расширения файлов: ``[".txt", ".csv", ".log"]``
            | Если открываете файл с другим расширением установите ``check_ext=False``

        Args:
            filepath (:obj:`str`): Полный путь до файла
            check_ext (:obj:`bool`, optional): Если ``True`` - проверяет расширение файла.
                По умолчанию ``True``

        Examples:
            >>> BaseUtils.cat("/home/trassir/ Trassir 3 License.txt")
        .. image:: images/base_utils.cat.png

        Raises:
            :class:`TypeError`: Если ``check_ext=True`` расширение файла нет в списке :obj:`_TEXT_FILE_EXTENSIONS`
        """

        if check_ext:
            _, ext = os.path.splitext(filepath)
            if ext not in cls._TEXT_FILE_EXTENSIONS:
                raise TypeError(
                    "Bad file extension: {}. To ignore this: set check_ext=False".format(
                        ext
                    )
                )

        if os.name == "nt":
            os.startfile(filepath)
        else:
            subprocess.Popen(
                [
                    "xterm -fg black -bg white -geometry 90x35 -fn "
                    "-misc-fixed-medium-r-normal--18-120-100-100-c-90-iso10646-1 -e bash -c \"cat '{}'; "
                    "read -n 1 -s -r -p '\n\nPress any key to exit'; exit\"".format(
                        filepath
                    )
                ],
                shell=True,
                close_fds=True,
            )

    @classmethod
    def _json_serializer(cls, data):
        """JSON serializer for objects not serializable by default"""
        if isinstance(data, (datetime, date)):
            return data.isoformat()

        elif isinstance(data, cls._host_api.ScriptHost.SE_Settings):
            return "settings('{}')".format(data.path)

        elif isinstance(data, cls._host_api.ScriptHost.SE_Object):
            return "object('{}')".format(data.guid)

        return type(data).__name__

    @classmethod
    def to_json(cls, data, **kwargs):
        """Сериализация объекта в JSON стрку

        Note:
            Не вызывает ошибку при сериализации объектов :obj:`datetime`,
            :obj:`date`, :obj:`SE_Settings`, :obj:`SE_Object`

        Args:
            data (:obj:`obj`): Объект для сериализации

        Returns:
            :obj:`str`: JSON строка

        Examples:
            >>> obj = {"now": datetime.now()}
            >>> json.dumps(obj)
            TypeError: datetime.datetime(2019, 4, 2, 18, 01, 33, 881000) is not JSON serializable
            >>> BaseUtils.to_json(obj, indent=None)
            '{"now": "2019-04-02T18:01:33.881000"}'
        """

        return json.dumps(data, default=cls._json_serializer, **kwargs)

    @staticmethod
    def ts_to_datetime(ts):
        """Конвертирует timestamp в :obj:`datetime` объект

        Args:
            ts (:obj:`int`): Timestamp

        Returns:
            :obj:`datetime`: Datetime объект
        """
        if ts > 1e10:
            ts_sec = int(ts / 1e6)
            ts_ms = int(ts - ts_sec * 1e6)
        else:
            ts_sec = int(ts)
            ts_ms = 0

        return datetime.fromtimestamp(ts_sec) + timedelta(microseconds=ts_ms)

    @classmethod
    def lpr_flags_decode(cls, flags):
        """Преобразует флаги события AutoTrassir

        Приводит флаги события человекочитаемый список

        Note:
            Список доступных флагов:

            - ``LPR_UP`` - Направление движения вверх
            - ``LPR_DOWN`` - Направление движения вниз

            - ``LPR_BLACKLIST`` - Номер в черном списке
            - ``LPR_WHITELIST`` - Номер в черном списке
            - ``LPR_INFO`` - Номер в информационном списке

            - ``LPR_FIRST_LANE`` - Автомобиль двигается по первой полосе
            - ``LPR_SECOND_LANE`` - Автомобиль двигается по второй полосе
            - ``LPR_THIRD_LANE`` - Автомобиль двигается по третей полосе

            - ``LPR_EXT_DB_ERROR`` - Ошибка во внешнем списке
            - ``LPR_CORRECTED`` - Номер исправлен оператором

        Args:
            flags (:obj:`int`): Биты LPR события. Как правило аргумент :obj:`ev.flags`
                события :obj:`SE_LprEvent` AutoTrassir. Например :obj:`536870917`

        Returns:
            List[:obj:`str`]: Список флагов

        Examples:
            >>> BaseUtils.lpr_flags_decode(536870917)
            ['LPR_UP', 'LPR_BLACKLIST']
        """
        return [bit for bit, code in cls._LPR_FLAG_BITS.iteritems() if (flags & code)]

    @classmethod
    def image_to_base64(cls, image):
        """Создает base64 из изображения

        Args:
            image (:obj:`str`): Путь к изображению или изображение

        Returns:
            :obj:`str`: Base64 image

        Examples:
            >>> BaseUtils.image_to_base64(r"manual\en\cloud-devices-16.png")
            'iVBORw0KGgoAAAANSUhEUgAAB1MAAAH0CAYAAABo5wRhAAAACXBIWXMAAC4jA...'
            >>> BaseUtils.image_to_base64(open(r"manual\en\cloud-devices-16.png", "rb").read())
            'iVBORw0KGgoAAAANSUhEUgAAB1MAAAH0CAYAAABo5wRhAAAACXBIWXMAAC4jA...'
        """
        _, ext = os.path.splitext(image)

        if ext.lower() in cls._IMAGE_EXT:
            image = cls.win_encode_path(image)
            if not BaseUtils.is_file_exists(image):
                return ""

            with open(image, "rb") as image_file:
                image = image_file.read()

        return base64.b64encode(image)

    @classmethod
    def base64_to_html_img(cls, image_base64, **kwargs):
        """Возвращает base64 изображение в `<img>` html теге

        Args:
            image_base64 (:obj:`str`): Base64 image
            **kwargs: HTML `<img>` tag attributes. Подробнее на `html.com
                <https://html.com/tags/img/#Attributes_of_img>`_

        Returns:
            :obj:`str`: html image

        Examples:
            >>> base64_image = BaseUtils.image_to_base64(r"manual\en\cloud-devices-16.png")
            >>> html_image = BaseUtils.base64_to_html_img(base64_image, width=280, height=75)
            >>> html_image
            '<img src="data:image/png;base64,iVBORw0KGgoAA...Jggg==" width="280" height="75">'
            >>> host.message(html_image)

                .. image:: images/popup_sender.image.png
        """
        html_img = cls._HTML_IMG_TEMPLATE.format(
            img=image_base64,
            attr=" ".join(
                '%s="%s"' % (key, value) for key, value in kwargs.iteritems()
            ),
        )
        return html_img

    @staticmethod
    def save_pkl(file_path, data):
        """Сохраняет данные в `.pkl` файл

        Args:
            file_path (:obj:`str`): Путь до файла
            data: Данные для сохранения

        Returns:
            :obj:`str`: Абсолютный путь до файла

        Examples:
            >>> data = {"key": "value"}
            >>> BaseUtils.save_pkl("saved_data.pkl", data)
            'D:\\DSSL\\Trassir-4.1-Client\\saved_data.pkl'

        """
        if not file_path.endswith(".pkl"):
            file_path = file_path + ".pkl"

        with open(file_path, "wb") as opened_file:
            pickle.dump(data, opened_file)

        return os.path.abspath(file_path)

    @staticmethod
    def load_pkl(file_path, default_type=dict):
        """Загружает данные из `.pkl` файла

        Args:
            file_path (:obj:`str`): Путь до файла
            default_type (optional):
                Тип данных, возвращаемый при неудачной загрузке данных из файла.
                По умолчанию :obj:`dict`

        Returns:
            Данные из файла или :obj:`default_type()`

        Examples:
            >>> BaseUtils.load_pkl("fake_saved_data.pkl")
            {}
            >>> BaseUtils.load_pkl("fake_saved_data.pkl", default_type=list)
            []
            >>> BaseUtils.load_pkl("fake_saved_data.pkl", default_type=int)
            0
            >>> BaseUtils.load_pkl("fake_saved_data.pkl", default_type=str)
            ''
            >>> BaseUtils.load_pkl("saved_data.pkl")
            {'key': 'value'}
        """

        if not file_path.endswith(".pkl"):
            file_path = file_path + ".pkl"

        data = default_type()

        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as opened_file:
                    data = pickle.load(opened_file)
            except (EOFError, IndexError, ValueError, TypeError):
                """ dump file is empty or broken """

        return data

    @classmethod
    def get_object(cls, obj_id):
        """Возвращает объект Trassir, если он доступен, иначе ``None``

        Args:
            obj_id (:obj:`str`): Guid объекта или его имя

        Returns:
            :obj:`ScriptHost.SE_Object`: Объект Trassir или ``None``

        Examples:
            >>> obj = BaseUtils.get_object("EZJ4QnbC")
            >>> if obj is None:
            >>>     host.error("Object not found")
            >>> else:
            >>>     host.message("Object name is {0.name}".format(obj))
        """
        if not isinstance(obj_id, (str, unicode)):
            raise TypeError(
                "Expected str or unicode, got '{}'".format(type(obj_id).__name__)
            )
        obj = cls._host_api.object(obj_id)
        try:
            obj.name
        except EnvironmentError:
            """Object not found"""
            obj = None
        return obj

    @classmethod
    def get_object_name_by_guid(cls, guid):
        """Возвращает имя объекта Trassir по его guid

        Tip:
            Можно использовать:

            - guid объекта ``"CFsuNBzt"``
            - guid объекта + guid сервера ``"CFsuNBzt_pV4ggECb"``

        Args:
            guid (:obj:`str`): Guid объекта Trassir

        Returns:
            :obj:`str`: Имя объекта, если объект найден, иначе ``guid``

        Examples:
            >>> BaseUtils.get_object_name_by_guid("EZJ4QnbC")
            'AC-D2141IR3'
            >>> BaseUtils.get_object_name_by_guid("EZJ4QnbC-")
            'EZJ4QnbC-'
        """
        guid = guid.split("_", 1)[0]
        obj = cls.get_object(guid)
        if obj is None:
            name = guid
        else:
            name = obj.name
        return name

    @classmethod
    def get_full_guid(cls, obj_id):
        """Возвращает полный guid объекта

        Args:
            obj_id (:obj:`str`): Guid объекта или его имя

        Returns:
            :obj:`str`: Полный guid объекта
        """

        tr_obj = cls.get_object(obj_id)
        if tr_obj is not None:
            for obj in cls._host_api.objects_list(""):
                if tr_obj.guid == obj[1]:
                    return "{}_{}".format(obj[1], cls._FOLDERS.get(obj[3], obj[3]))

    @classmethod
    def get_operator_gui(cls):
        """Возвращает объект интерфейса оператора

        Returns:
            :obj:`OperatorGUI`: Объект интерфейса оператора

        Raises:
            ScriptError: Если не удается загрузить интерфейс

        Examples:
            Открыть интерфейс Trassir а мониторе №1

            >>> operator_gui = BaseUtils.get_operator_gui()
            >>> operator_gui.raise_monitor(1)
        """
        obj = cls.get_object("operatorgui_{}".format(cls._host_api.settings("").guid))
        if obj is None:
            raise ScriptError("Failed to load operator gui")
        return obj

    @classmethod
    def get_server_guid(cls):
        """Возвращает guid текущего сервра

        Returns:
            :obj:`str`: Guid сервера

        Examples:
            >>> BaseUtils.get_server_guid()
            'client'
        """
        return cls._host_api.settings("").guid

    @classmethod
    def get_script_name(cls):
        """Возвращает имя текущего скрипта

        Returns:
            :obj:`str`: Имя скрипта

        Examples:
            >>> BaseUtils.get_script_name()
            'Новый скрипт'
        """
        return cls._host_api.stats().parent()["name"] or __name__

    @classmethod
    def get_screenshot_folder(cls):
        """Возвращает путь до папки скриншотов

        При этом производит проверку папки методом
        :meth:`BaseUtils.is_folder_exists`

        Returns:

            :obj:`str`: Полный путь к папке скриншотов

        Examples:
            >>> BaseUtils.get_screenshot_folder()
            '/home/trassir/shots'
        """
        folder = cls._host_api.settings("system_wide_options")["screenshots_folder"]
        cls.is_folder_exists(folder)
        return folder

    @classmethod
    def get_logger(
        cls,
        name=None,
        host_log="WARNING",
        popup_log="ERROR",
        file_log=None,
        file_name=None,
    ):
        """Возвращает логгер с предустановленными хэндлерами

        Доступные хэндлеры:
            - *host_log*: Пишет сообщения в основной лог сервера _t1server.log
            - *popup_log*: Показывает всплывающие сообщения ``message/alert/error``
            - *file_log*: Пишет сообщения в отдельный файл в папку скриншотов

        Для каждого хэндлера можно установить разный уровень логирования

        По умолчанию ``host_log="WARNING"`` и ``popup_log="ERROR"``

        Note:
            Имя файла лога можно указать с расширение ".log" или без.

        See Also:
            `Logging levels на сайте docs.python.org
            <https://docs.python.org/2/library/logging.html#logging-levels>`_

        Args:
            name (:obj:`str`, optional): Имя логгера, должно быть уникальным для
                каждого скрипта. По умолчанию :obj:`None`, и равно guid скрипта.
            host_log (:obj:`str`, optional): Уровень логирования в основной лог.
                По умолчанию ``"WARNING"``
            popup_log (:obj:`str`, optional): Уровень логирования во всплывающих
                сообщениях. По умолчанию ``"ERROR"``
            file_log (:obj:`str`, optional): Уровень логирования в отдельный файл
                По умолчанию :obj:`None`
            file_name (:obj:`str`, optional): Имя файла для логирования.
                По умолчанию :obj:`None` и равно ``<имени скрипта>.log``

        Returns:
            :obj:`logging.logger`: Логгер

        Examples:
            >>> logger = BaseUtils.get_logger()
            >>> logger.warning("My warning message")
            >>> try:
            >>>     # noinspection PyUnresolvedReferences
            >>>     do_something()
            >>> except NameError:
            >>>     logger.error("Function is not defined", exc_info=True)
        """
        logger_ = logging.getLogger(name or __name__)
        logger_.setLevel("DEBUG")

        if logger_.handlers:
            for handler in logger_.handlers[:]:
                handler.close()
                logger_.removeHandler(handler)

        if host_log:
            host_handler = HostLogHandler()
            host_handler.setLevel(host_log)
            if name:
                host_formatter = logging.Formatter(
                    "[%(levelname)-8s] %(lineno)-4s <%(funcName)s> - %(name)s: %(message)s"
                )
            else:
                host_formatter = logging.Formatter(
                    "[%(levelname)-8s] %(lineno)-4s <%(funcName)s> - %(message)s"
                )
            host_handler.setFormatter(host_formatter)
            logger_.addHandler(host_handler)

        if popup_log:
            popup_handler = PopupHandler()
            popup_handler.setLevel(popup_log)
            popup_formatter = logging.Formatter(
                fmt="<b>[%(levelname)s]</b> Line: %(lineno)s<br><i>%(message).630s</i>"
            )
            popup_handler.setFormatter(popup_formatter)
            logger_.addHandler(popup_handler)

        if file_log:
            if file_name is None:
                file_name = cls.get_script_name()

            if not file_name.endswith(".log"):
                file_name = "{}.log".format(file_name)

            file_path = os.path.join(cls.get_screenshot_folder(), file_name)
            file_path = cls.win_encode_path(file_path)

            file_handler = MyFileHandler(file_path)
            file_handler.setLevel(file_log)
            if name:
                file_formatter = logging.Formatter(
                    fmt="%(asctime)s [%(levelname)-8s] %(lineno)-4s <%(funcName)s> - %(name)s: %(message)s",
                    datefmt="%Y/%m/%d %H:%M:%S",
                )
            else:
                file_formatter = logging.Formatter(
                    fmt="%(asctime)s [%(levelname)-8s] %(lineno)-4s <%(funcName)s> - %(message)s",
                    datefmt="%Y/%m/%d %H:%M:%S",
                )
            file_handler.setFormatter(file_formatter)
            logger_.addHandler(file_handler)

        return logger_

    @classmethod
    def set_script_name(cls, fmt=None, script_name=None):
        """Автоматически изменяет имя скрипта

        Новое имя скрипта создается на основе `параметров
        <https://www.dssl.ru/files/trassir/manual/ru/setup-script-parameters.html>`_
        скрипта. По желанию можно изменить шаблон имени. По умолчанию
        :obj:`"[{company}] {title} v{version}"`

        Note:
            Имя изменяется только если сейчас у скрипта стандартное имя,
            например :obj:`"Новый скрипт"` или :obj:`"Unnamed Script"` и др.

        Args:
            fmt (:obj:`str`, optional): Шаблон имени скрипта. По умолчанию :obj:`None`
            script_name (:obj:`str`, optional): Имя скрипта. Если не задано - парсит
                имя из параметров. По умолчанию :obj:`None`

        Examples:
            >>> BaseUtils.set_script_name()
            'AATrubilin - trassir_script_framework v0.4'

            >>> BaseUtils.set_script_name(fmt="{title}")
            'trassir_script_framework'
        """
        if cls._host_api.stats().parent()["name"] in cls._SCR_DEFAULT_NAMES:
            if script_name is None:
                try:
                    root = ElementTree.fromstring(__doc__)
                except ElementTree.ParseError:
                    root = None

                if root is None:
                    company, title, version = None, None, None
                else:
                    company = root.find("company") if root else None
                    title = root.find("title") if root else None
                    version = root.find("version") if root else None

                if fmt is None:
                    fmt = "[{company}] {title} v{version}"

                script_name = fmt.format(
                    company="DSSL" if company is None else company.text,
                    title="Script" if title is None else title.text,
                    version="0.1" if version is None else version.text,
                )

            cls._host_api.stats().parent()["name"] = script_name

            return script_name


class Worker(threading.Thread):
    """Thread executing tasks from a given tasks queue"""

    def __init__(self, tasks):
        super(Worker, self).__init__()
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            finally:
                self.tasks.task_done()


class ThreadPool:
    """Pool of threads consuming tasks from a queue"""

    def __init__(self, num_threads, callback=None, host_api=host):
        self._host_api = host_api
        self.tasks = Queue(num_threads)
        for _ in xrange(num_threads):
            Worker(self.tasks)
        if callback is None:
            callback = BaseUtils.do_nothing
        self.callback = callback

    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()
        self._host_api.timeout(1000, self.callback)


class HTTPRequester(py_object):
    """Framework for urllib2

    See Also:
        https://docs.python.org/2/library/urllib2.html#urllib2.build_opener

    Args:
        opener (:obj:`urllib2.OpenerDirector`, optional): Обработчик запросов.
            По умолчанию :obj:`None`
        timeout (:obj:`int`, optional): Время ожидания запроса, в секундах.
            По умолчанию :obj:`timeout=10`

    Examples:
        Пример запроса к SDK Trassir

        >>> # Отключение проверки сертификата
        >>> context = ssl.create_default_context()
        >>> context.check_hostname = False
        >>> context.verify_mode = ssl.CERT_NONE
        >>>
        >>> handler = urllib2.HTTPSHandler(context=context)
        >>> opener = urllib2.build_opener(handler)
        >>>
        >>> requests = HTTPRequester(opener, timeout=20)
        >>> response = requests.get(
        >>>     "https://172.20.0.101:8080/login",
        >>>     params={"username": "Admin", "password": "12345"}
        >>> )
        >>>
        >>> response.code
        200
        >>> response.text
        '{\\n   "sid" : "T6LAAcxg",\\n   "success" : 1\\n}\\n'
        >>> response.json
        {u'success': 1, u'sid': u'T6LAAcxg'}
    """

    class Response(py_object):
        """Класс ответа от сервера

        Attributes:
            code (:obj:`str` | :obj:`int`): Код ответа сервера
            text (:obj:`str`): Текст ответа
            json (:obj:`dict` | :obj:`list`): Создает объект из json ответа
        """

        def __init__(self, *args):
            self.code, self.text = args

        @property
        def json(self):
            return json.loads(self.text)

    def __init__(self, opener=None, timeout=10):
        if opener is None:
            handler = urllib2.BaseHandler()
            opener = urllib2.build_opener(handler)
        self._opener = opener

        self.timeout = timeout

    @BaseUtils.catch_request_exceptions
    def _get_response(self, request):
        """Returns response

        Args:
            request (:obj:`urllib2.Request`): This class is an abstraction of a URL request
        """
        response = self._opener.open(request, timeout=self.timeout)
        return response.code, response.read()

    @staticmethod
    def _parse_params(**params):
        """Params get string params

        Args:
            **params (dict): Keyword arguments

        Returns:
            str: params string
        """
        return "&".join(
            "{key}={value}".format(key=key, value=value)
            for key, value in params.iteritems()
        )

    @staticmethod
    def _prepare_headers(headers):
        """Prepare headers for request"""
        if headers is None:
            headers = {}

        if "User-Agent" not in headers:
            headers["User-Agent"] = "TrassirScript"
        return headers

    def get(self, url, params=None, headers=None):
        """Создает GET запрос по указанному :obj:`url`

        Args:
            url (:obj:`str`): Url для запроса
            params (:obj:`dict`, optional): Параметры GET запроса
            headers (:obj:`dict`, optional): Заголовки запроса

        Examples:
            >>> requests = HTTPRequester()
            >>> response = requests.get(
            >>>     "http://httpbin.org/get",
            >>>     params={"PARAMETER": "TEST"},
            >>> )
            >>> response.code
            200
            >>> response.text
            '{\\n  "args": {\\n    "PARAMETER": "TEST"\\n  }, \\n ...'
            >>> response.json
            {u'args': {u'PARAMETER': u'TEST'}, ...}

        Returns:
            :class:`HTTPRequester.Response`: Response instance
        """
        if params is not None:
            url += "?{params}".format(params=self._parse_params(**params))

        headers = self._prepare_headers(headers)

        request = urllib2.Request(url, headers=headers)
        response = self._get_response(request)
        return self.Response(*response)

    def post(self, url, data=None, headers=None):
        """Создает POST запрос по указанному :obj:`url`

        Args:
            url (:obj:`str`): Url для запроса
            data (:obj:`dict`, optional): Данные POST запроса
            headers (:obj:`dict`, optional): Заголовки запроса

        Examples:
            >>> requests = HTTPRequester()
            >>> response = requests.post(
            >>>     "http://httpbin.org/post",
            >>>     data={"PARAMETER": "TEST"},
            >>>     headers={"Content-Type": "application/json"},
            >>> )
            >>> response.code
            200
            >>> response.text
            '{\\n  "args": {\\n    "PARAMETER": "TEST"\\n  }, \\n ...'
            >>> response.json
            {u'args': {u'PARAMETER': u'TEST'}, ...}

        Returns:
            :class:`HTTPRequester.Response`: Response instance
        """
        if data is None:
            data = {}

        if isinstance(data, dict):
            data = urllib.urlencode(data)

        headers = self._prepare_headers(headers)

        request = urllib2.Request(url, data=data, headers=headers)
        response = self._get_response(request)
        return self.Response(*response)


class ScriptObject(host.TrassirObject, py_object):
    """Создает объект для генерации событий

    Args:
        name (:obj:`str`, optional): Имя объекта. По умолчанию :obj:`None`
        guid (:obj:`str`, optional): Guid объекта. По умолчанию :obj:`None`
        parent (:obj:`str`, optional): Guid родительского объекта. По умолчанию :obj:`None`

    Note:
        - Имя объекта по умолчанию - :meth:`BaseUtils.get_script_name`
        - Guid объекта по умолчанию строится по шаблноу ``"{script_guid}_object"``
        - Guid родительского объекта по умолчанию -
          :meth:`BaseUtils.get_server_guid`

    Examples:
        >>> # Создаем объект
        >>> scr_obj = ScriptObject()

        >>> # Проверяем текущее состояние объекта
        >>> scr_obj.health
        'OK'

        >>> # Установить флаг возле объекта
        >>> scr_obj.check_me = True

        >>> # Сгенерировать событие с текстом
        >>> scr_obj.fire_event_v2("New event")
    """

    def __init__(self, name=None, guid=None, parent=None, host_api=host):
        super(ScriptObject, self).__init__("Script")

        self._host_api = host_api
        scr_parent = host_api.stats().parent()

        self._name = name or BaseUtils.get_script_name()
        self.set_name(self._name)

        self._guid = guid or "{}-object".format(scr_parent.guid)
        self.set_guid(self._guid)

        self._parent = parent or BaseUtils.get_server_guid()
        self.set_parent(self._parent)

        self._folder = ""

        self._health = "OK"
        self._check_me = True

        self.set_initial_state([self._health, self._check_me])

        host_api.object_add(self)

    @property
    def health(self):
        """:obj:`"OK"` | :obj:`"Error"`: Состояние объекта"""
        return self._health

    @health.setter
    def health(self, value):
        if value in ["OK", "Error"]:
            self.set_state([value, self._check_me])
            self._health = value
        else:
            raise ValueError("Expected 'OK' or 'Error', got '{}'".format(value))

    @property
    def check_me(self):
        """:obj:`bool`: Флаг ``check_me`` объекта"""
        return self._check_me

    @check_me.setter
    def check_me(self, value):
        if isinstance(value, bool) or value in [1, 0]:
            value = 1 - value
            self.set_state([self._health, value])
            self._check_me = value
        else:
            raise ValueError("Expected bool or 1|0, got '{}'".format(value))

    @property
    def name(self):
        """:obj:`str`: Имя объекта"""
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.set_name(value)
            self._name = value
        else:
            raise ValueError("Expected str, got {}".format(type(value).__name__))

    @property
    def folder(self):
        """:obj:`str`: Папка объекта"""
        return self._folder

    @folder.setter
    def folder(self, value):
        if not value:
            raise ValueError("Object guid can't be empty")

        if isinstance(value, str):
            if self._folder:
                self.change_folder(value)
            else:
                self.set_folder(value)
            self._folder = value
        else:
            raise ValueError("Expected str, got {}".format(type(value).__name__))

    def fire_event_v2(self, message, channel="", data=""):
        """Создает событие в Trassir

        Args:
            message (:obj:`str`): Сообщение события (``p1``)
            channel (:obj:`str`, optional): Ассоциированный с событием канал (``p2``)
            data (:obj:`str`, optional): Дополнительные данные (``p3``)
        """
        if not isinstance(data, str):
            data = BaseUtils.to_json(data, indent=None)

        self.fire_event("Script: %1", message, channel, data)


class ShotSaverError(ScriptError):
    """Base ShotSaver Exception"""

    pass


class ShotSaver(py_object):
    """Класс для сохранения скриншотов

    Examples:

        >>> ss = ShotSaver()
        >>> # Смена папки сохранения скриншотов по умолчанию
        >>> ss.screenshots_folder
        '/home/trassir/shots'
        >>> ss.screenshots_folder += "/my_shots"
        >>> ss.screenshots_folder
        '/home/trassir/shots/my_shots'
        >>>
        >>> # Сохранение скриншота с канала ``"e80kgBLh_pV4ggECb"``
        >>> ss.shot("e80kgBLh_pV4ggECb")
        '/home/trassir/shots/AC-D2141IR3 Склад (2019.04.03 15-58-26).jpg'
    """

    _AWAITING_FILE = 5  # Time for check file function, sec
    _SHOT_NAME_TEMPLATE = (
        "{name} (%Y.%m.%d %H-%M-%S).jpg"
    )  # Template for shot file name
    _ASYNC_SHOT_TRIES = 2  # Tries to make shot in async_shot method

    def __init__(self, host_api=host):
        self._host_api = host_api
        self._screenshots_folder = BaseUtils.get_screenshot_folder()

    @property
    def screenshots_folder(self):
        """:obj:`str`: Папка для сохранения скриншотов по умолчанию

        Устанавливает новый путь по умолчанию для сохранения скриншотов,
        если папка не существует - создает папку. Или возвращает текущий
        путь для сохранения скриншотов.

        Note:
            По молчанию :obj:`screenshots_folder`  =
            :meth:`BaseUtils.get_screenshot_folder`

        Raises:
            OSError: Если возникает ошибка при создании папки
        """
        return self._screenshots_folder

    @screenshots_folder.setter
    def screenshots_folder(self, folder):
        if not os.path.isdir(folder):
            try:
                os.makedirs(folder)
            except OSError as err:
                raise OSError("Can't make dir '{}': {}".format(folder, err))

        self._screenshots_folder = folder

    def shot(self, channel_full_guid, dt=None, file_name=None, file_path=None):
        """Делает скриншот с указанного канала

        Note:
            По умолчанию:

            - :obj:`dt=datetime.now()`
            - :obj:`file_name="{name} (%Y.%m.%d %H-%M-%S).jpg"`, где ``{name}`` - имя канала

        Args:
            channel_full_guid (:obj:`str`): Полный guid анала. Например: ``"CFsuNBzt_pV4ggECb"``
            dt (:obj:`datetime.datetime`, optional): :obj:`datetime.datetime` для скриншота.
                По умолчанию :obj:`None`
            file_name (:obj:`str`, optional): Имя файла с расширением. По умолчанию :obj:`None`
            file_path (:obj:`str`, optional): Путь для сохранения скриншота. По умолчанию :obj:`None`

        Returns:
            :obj:`str`: Полный путь до скриншота

        Raises:
            ValueError: Если в guid канала отсутствует guid сервера
            TypeError: Если ``isinstance(dt, (datetime, date)) is False``

        Examples:
            >>> ss = ShotSaver()
            >>> ss.shot("e80kgBLh_pV4ggECb")
            '/home/trassir/shots/AC-D2141IR3 Склад (2019.04.03 15-58-26).jpg'
        """
        if "_" not in channel_full_guid:
            raise ValueError(
                "Expected full channel guid, got {}".format(channel_full_guid)
            )

        if dt is None:
            ts = "0"
            dt = datetime.now()
        else:
            if not isinstance(dt, (datetime, date)):
                raise TypeError("Expected datetime, got {}".format(type(dt).__name__))
            ts = dt.strftime("%Y%m%d_%H%M%S")

        if file_name is None:
            file_name = dt.strftime(
                self._SHOT_NAME_TEMPLATE.format(
                    name=BaseUtils.get_object_name_by_guid(channel_full_guid)
                )
            )
        if file_path is None:
            file_path = self.screenshots_folder

        self._host_api.screenshot_v2_figures(
            channel_full_guid, file_name, file_path, ts
        )

        return os.path.join(file_path, file_name)

    def _async_shot(
        self, channel_full_guid, dt=None, file_name=None, file_path=None, callback=None
    ):
        """Вызывает ``callback`` после сохнанения скриншота

        * Метод работает в отдельном потоке
        * Вызывает функцию :meth:`ShotSaver.shot`
        * Ждет выполнения функции :meth:`BaseUtils.check_file` ``tries=10``
        * Вызвает ``callback`` функцию

        Args:
            channel_full_guid (:obj:`str`): Полный guid канала. Например: ``"CFsuNBzt_pV4ggECb"``
            dt (:obj:`datetime.datetime`, optional): :obj:`datetime.datetime` для скриншота.
                По умолчанию :obj:`None`
            file_name (:obj:`str`, optional): Имя файла с расширением. По умолчанию :obj:`None`
            file_path (:obj:`str`, optional): Путь для сохранения скриншота. По умолчанию :obj:`None`
            callback (:obj:`function`): Callable function
        """
        if callback is None:
            callback = BaseUtils.do_nothing

        shot_file = ""
        for _ in xrange(self._ASYNC_SHOT_TRIES):
            shot_file = self.shot(
                channel_full_guid, dt=dt, file_name=file_name, file_path=file_path
            )
            if BaseUtils.is_file_exists(
                BaseUtils.win_encode_path(shot_file), self._AWAITING_FILE
            ):
                self._host_api.timeout(100, lambda: callback(True, shot_file))
                break
        else:
            self._host_api.timeout(100, lambda: callback(False, shot_file))

    @BaseUtils.run_as_thread_v2()
    def async_shot(
        self, channel_full_guid, dt=None, file_name=None, file_path=None, callback=None
    ):
        """async_shot(channel_full_guid, dt=None, file_name=None, file_path=None, callback=None)
        Вызывает ``callback`` после сохнанения скриншота

        * Метод работает в отдельном потоке
        * Вызывает функцию :meth:`ShotSaver.shot`
        * Ждет выполнения функции :meth:`BaseUtils.check_file` ``tries=10``
        * Вызвает ``callback`` функцию

        Args:
            channel_full_guid (:obj:`str`): Полный guid канала. Например: ``"CFsuNBzt_pV4ggECb"``
            dt (:obj:`datetime.datetime`, optional): :obj:`datetime.datetime` для скриншота.
                По умолчанию :obj:`None`
            file_name (:obj:`str`, optional): Имя файла с расширением. По умолчанию :obj:`None`
            file_path (:obj:`str`, optional): Путь для сохранения скриншота. По умолчанию :obj:`None`
            callback (:obj:`function`, optional): Callable function

        Returns:
            :obj:`threading.Thread`: Thread object

        Examples:
            >>> # noinspection PyUnresolvedReferences
            >>> def callback(success, shot_path):
            >>>     # Пример callback функции
            >>>     # Args:
            >>>     #     success (bool): True если скриншот успешно сохранен, иначе False
            >>>     #     shot_path (str): Полный путь до скриншота
            >>>     if success:
            >>>         host.message("Скриншот успешно сохранен<br>%s" % shot_path)
            >>>     else:
            >>>         host.error("Ошибка сохранения скриншота <br>%s" % shot_path)
            >>>
            >>> ss = ShotSaver()
            >>> ss.async_shot("e80kgBLh_pV4ggECb", callback=callback)
            <Thread(Thread-76, started daemon 212)>
        """
        self._async_shot(
            channel_full_guid,
            dt=dt,
            file_name=file_name,
            file_path=file_path,
            callback=callback,
        )

    @BaseUtils.run_as_thread_v2()
    def pool_shot(self, shot_args, pool_size=10, end_callback=None):
        """pool_shot(shot_args, pool_size=10, end_callback=None)
        Сохраняет скриншоты по очереди.

        Одновременно в работе не более :obj:`pool_size` задачь.
        Вызывает ``callback`` после сохнанения всех скриншотов
        см. :meth:`ShotSaver.async_shot`

        Args:
            shot_args (List[:obj:`tuple`]): Аргументы для функции async_shot
            pool_size (:obj:`int`, optional): Размер пула. По умолчанию :obj:`pool_size=10`
            end_callback (:obj:`function`, optional): Вызывается после сохранения всех скриншотов

        Returns:
            :obj:`threading.Thread`: Thread object

        Examples:
            >>> from datetime import datetime, timedelta
            >>>
            >>> def end_callback():
            >>>     host.message("Все скриншоты сохранены")
            >>>
            >>> channel_guid = "e80kgBLh_pV4ggECb"
            >>> dt_now = datetime.now()
            >>> dt_range = [dt_now - timedelta(minutes=10*i) for i in xrange(12)]
            >>> dt_range
            [datetime.datetime(2019, 4, 25, 9, 38, 9, 253000), datetime.datetime(2019, 4, 25, 9, 28, 9, 253000), ...]
            >>> shot_args = []
            >>> for dt in dt_range:
            >>>     kwargs = {"dt": dt}
            >>>     shot_args.append(((channel_guid,), kwargs))
            >>>
            >>> ss = ShotSaver()
            >>> ss.pool_shot(shot_args, pool_size=10, end_callback=end_callback)
            <Thread(Thread-76, started daemon 212)>
        """
        pool = ThreadPool(pool_size, end_callback)
        for args, kwargs in shot_args:
            pool.add_task(self._async_shot, *args, **kwargs)
        pool.wait_completion()
        return pool


class VideoExporterError(ScriptError):
    """Base ShotSaver Exception"""

    pass


class VideoExporter(py_object):
    """Класс для экспорта видео

    Examples:
        Смена папки экспорта видео по умолчанию

        >>> ss = VideoExporter()
        >>> ss.export_folder
        '/home/trassir/shots'
        >>> ss.export_folder += "/my_videos"
        >>> ss.export_folder
        '/home/trassir/shots/my_videos'

        | Экспорт видео с вызовом ``callback`` функции после выполнения.
        | Начало экспорта - 120 секунд назад, продолжительность 60 сек.

        >>> # noinspection PyUnresolvedReferences
        >>> def callback(success, file_path, channel_full_guid):
        >>>     # Пример callback функции
        >>>     # Args:
        >>>     #     success (bool): True если видео экспортировано успешно, иначе False
        >>>     #     file_path (str): Полный путь до видеофайла
        >>>     #     channel_full_guid (str) : Полный guid канала
        >>>     if success:
        >>>         host.message("Экспорт успешно завершен<br>%s" % file_path)
        >>>     else:
        >>>         host.error("Ошибка экспорта<br>%s" % file_path)

        >>> ss = VideoExporter()
        >>> dt_start = datetime.now() - timedelta(seconds=120)
        >>> ss.export(callback, "e80kgBLh_pV4ggECb", dt_start)
    """

    _EXPORTED_VIDEO_NAME_TEMPLATE = (
        "{name} ({dt_start} - {dt_end}){sub}.avi"
    )  # Template for shot file name

    def __init__(self, host_api=host):
        self._host_api = host_api
        self._export_folder = BaseUtils.get_screenshot_folder()
        self._now_exporting = False
        self._queue = deque()
        self._default_prebuffer = host_api.settings("archive")["prebuffer"] + 2

    @property
    def export_folder(self):
        """:obj:`str`: Папка для экспорта видео по умолчанию

        Устанавливает новый путь по умолчанию для экспорта видео,
        если папка не существует - создает папку. Или возвращает текущий
        путь для экспорта видео.

        Note:
            По молчанию ``export_folder`` = :meth:`BaseUtils.get_screenshot_folder`

        Raises:
            OSError: Если возникает ошибка при создании папки
        """
        return self._export_folder

    @export_folder.setter
    def export_folder(self, folder):
        if not os.path.isdir(folder):
            try:
                os.makedirs(folder)
            except OSError as err:
                raise OSError("Can't make dir '{}': {}".format(folder, err))

        self._export_folder = folder

    def _get_prebuffer(self, server_guid, dt_end):
        """Get prebuffer delay

        Args:
            server_guid (str): Full channel guid include server guid

        Returns:
            int: Prebuffer delay
        """
        setting_path = "/{}/archive".format(server_guid)

        try:
            prebuffer = self._host_api.settings(setting_path)["prebuffer"] + 2
        except KeyError:
            prebuffer = self._default_prebuffer

        wait_dt_end = (int(time.mktime(dt_end.timetuple())) + prebuffer) * 1000000

        return "%.0f" % wait_dt_end

    def clear_complete_tasks(self):
        for task in self._host_api.archive_export_tasks_get():
            if task["state"] != 1:
                self._host_api.archive_export_task_cancel(
                    task["id"],  # task id from archive_export_tasks_get
                    -1,  # -1 - do not wait for result, 0 - wait forever, > 0 - wait timeout_sec seconds
                    BaseUtils.do_nothing,  # callback_success
                    BaseUtils.do_nothing,  # callback_error
                )

    def _check_queue(self):
        self._host_api.timeout(10, self.clear_complete_tasks)
        if self._queue:
            args, kwargs = self._queue.popleft()
            self._export(*args, **kwargs)

    def _export_checker(self, status, callback, file_path, channel_full_guid):
        if status == 1:
            return
        elif status in [0, 2]:
            """Export failed"""
            self._host_api.timeout(
                100, lambda: callback(False, file_path, channel_full_guid)
            )
        else:
            """Export success"""
            self._host_api.timeout(
                100, lambda: callback(True, file_path, channel_full_guid)
            )

        self._now_exporting = False
        self._check_queue()

    def _export(
        self,
        channel_full_guid,
        dt_start,
        dt_end=None,
        duration=60,
        prefer_substream=False,
        file_name=None,
        file_path=None,
        callback=None,
    ):
        """Exporting file

        Call callback(success: bool, file_path: str, channel_full_guid: str)
        when export finished, and clear tasks in trassir main control panel

        Note:
            Export task adding only when previous task finished
            You can set dt_start, dt_end, or dt_start, duration for export
            if dt_end is None: dt_end = dt_start + timedelta(seconds=duration)

        Args:
            channel_full_guid (str): Full channel guid; example: "CFsuNBzt_pV4ggECb"
            dt_start (datetime): datetime instance for export start
            dt_end (datetime, optional): datetime instance for export end; default: None
            duration (int, optional): Export duration (dt_start + duration seconds) if dt_end is None; default: 10
            prefer_substream (bool, optional): If True - export substream; default: False
            file_name (str, optional): File name with extension; default: _EXPORTED_VIDEO_NAME_TEMPLATE
            file_path (str, optional): Path to save shot; default: screenshots_folder
            callback (function, optional): Function that calling when export finished
        """

        if "_" not in channel_full_guid:
            raise ValueError(
                "Expected full channel guid, got {}".format(channel_full_guid)
            )

        if not isinstance(dt_start, (datetime, date)):
            raise TypeError("Expected datetime, got {}".format(type(dt_start).__name__))

        if dt_end:
            if not isinstance(dt_end, (datetime, date)):
                raise TypeError(
                    "Expected datetime, got {}".format(type(dt_end).__name__)
                )
        else:
            dt_end = dt_start + timedelta(seconds=duration)

        ts_start = "%.0f" % (time.mktime(dt_start.timetuple()) * 1000000)
        ts_end = "%.0f" % (time.mktime(dt_end.timetuple()) * 1000000)

        channel_guid, server_guid = channel_full_guid.split("_")

        options = {
            "prefer_substream": prefer_substream,
            "postponed_until_ts": self._get_prebuffer(server_guid, dt_end),
        }

        if file_name is None:
            file_name = self._EXPORTED_VIDEO_NAME_TEMPLATE.format(
                name=BaseUtils.get_object_name_by_guid(channel_guid),
                dt_start=dt_start.strftime("%Y.%m.%d %H-%M-%S"),
                dt_end=dt_end.strftime("%Y.%m.%d %H-%M-%S"),
                sub="_sub" if prefer_substream else "",
            )

        if file_path is None:
            file_path = self.export_folder

        exporting_path = os.path.join(file_path, file_name)

        if callback is None:
            callback = BaseUtils.do_nothing

        self._now_exporting = True

        def checker(status):
            self._export_checker(status, callback, exporting_path, channel_full_guid)

        self._host_api.archive_export(
            server_guid,
            channel_guid,
            exporting_path,
            ts_start,
            ts_end,
            options,
            checker,
        )

    def export(
        self,
        channel_full_guid,
        dt_start,
        dt_end=None,
        duration=60,
        prefer_substream=False,
        file_name=None,
        file_path=None,
        callback=None,
    ):
        """Запускает экспорт или добавляет задачу экспорта в очередь.

        После завершения экспорта вызывает ``callback`` функцию
        а также очищает список задач экспорта в панеле управления Trassir.

        Note:
            Задача экспорта добавляется только после завершения предыдущей.

        Tip:
            - Вы можете задать время начала и окончания экспорта
              ``dt_start``, ``dt_end``.
            - Или можно задать время начала экспорта ``dt_start`` и
              продолжительность экспорта (в сек.) ``duration``. По умолчнию
              ``duration=60``.
            - Если ``dt_end=None`` фунция использует ``duration`` для вычисления
              времени окончания ``dt_end = dt_start + timedelta(seconds=duration)``.

        Args:
            channel_full_guid (:obj:`str`): Полный guid канала. Например: ``"CFsuNBzt_pV4ggECb"``
            dt_start (:obj:`datetime.datetime`): :obj:`datetime.datetime` начала экспорта
            dt_end (:obj:`datetime.datetime`, optional): :obj:`datetime.datetime` окончания экспорта.
                По умолчанию :obj:`None`
            duration (:obj:`int`, optional): Продолжительность экспорта, в секундах. Используется если
                ``dt_end is None``. По умолчанию ``60``
            prefer_substream (:obj:`bool`, optional): Если ``True`` - Экспортирует субпоток.
                По умолчанию ``False``
            file_name (:obj:`str`, optional): Имя экспортируемого файла. По умолчанию :obj:`None`
            file_path (:obj:`str`, optional): Путь для экспорта. По умолчанию :obj:`None`
            callback (:obj:`function`, optional): Функция, которая вызывается после завершения экспорта.
                По умолчанию :obj:`None`
        """

        args = (channel_full_guid, dt_start)
        kwargs = {
            "dt_end": dt_end,
            "duration": duration,
            "prefer_substream": prefer_substream,
            "file_name": file_name,
            "file_path": file_path,
            "callback": callback,
        }
        if self._now_exporting:
            self._queue.append((args, kwargs))
        else:
            self._export(*args, **kwargs)


class TemplateError(ScriptError):
    """Raised by Template class"""

    pass


class GUITemplate(py_object):
    """Класс для работы с шаблонами Trassir

    При инициализации находит существующий шаблон по имени или создает новый.

    Note:
        Если вручную создать два или большее шаблона с одинаковыми именами
        данный класс выберет первый попавшийся шаблон с заданным именем.

    Warning:
            Работа с контентом шаблона может привести к падениям трассира.
            Используйте данный класс на свой страх и риск!

    Tip:
        Для понимания, как формируется контент отредактируйте любой шаблон
        вручную и посмотрите что получится в скрытых параметрах трассира
        (активируются нажатием клавиши F4 в настройках трассира)
        `Настройки/Шабоны/<Имя шаблона>/content`

        Ниже предсталвены некоторые примеры шаблонов

        - Вывод одного канала ``S0tE8nfg_Or3QZu4D``
          :obj:`gui7(DEWARP_SETTINGS,zwVj07w0,dewarp(),1,S0tE8nfg_Or3QZu4D)`
        - Вывод шаблона 4х4 с каналами двумя ``Kpid6EC0_Or3QZu4D``, ``ZRtXLrgu_Or3QZu4D``
          :obj:`gui7(DEWARP_SETTINGS,zwVj07w0,dewarp(),4,Kpid6EC0_Or3QZu4D,ZRtXLrgu_Or3QZu4D,,)`
        - Вывод шаблон с минибраузером и ссылкой на https://www.google.com/
          :obj:`minibrowser(0,htmltab(,https://www.google.com/))`

    Args:
        template_name (:obj:`str`): Имя шаблон

    Examples:
        >>> # Создаем шаблон с именем "New template" и получаем его guid
        >>> template = Template("New template")
        >>> template.guid
        'Y2YFAkeZ'


        >>> # Устанавливаем на шаблон минибраузер с ссылкой на google
        >>> template.content = "minibrowser(0,htmltab(,https://www.google.com/))"

        >>> # Изменяем имя шаблона на "Google search"
        >>> template.name = "Google search"

        >>> # Открываем шаблон на первом мониторе
        >>> template.show(1)
    """

    _DEFAULT_TEMPLATE = ""

    def __init__(self, template_name, host_api=host):
        self._name = template_name
        self._host_api = host_api
        self._operator_gui = BaseUtils.get_operator_gui()
        try:
            self._guid, self._template_settings = self._find_template_guid(
                template_name
            )
        except KeyError:
            self._guid, self._template_settings = self._init_template(template_name)

    def _find_template_guid(self, name):
        """Find template guid by name

        Args:
            name (str) : Template name

        Raises:
            KeyError if can't find template
        """
        templates = self._host_api.settings("templates")
        for template_ in templates.ls():
            if name == template_.name:
                return (
                    template_.guid,
                    self._host_api.settings("templates/{}".format(template_.guid)),
                )
        raise KeyError

    def _init_template(self, name):
        """Create new template

        Args:
            name (str) : Template name
        """
        self._host_api.object(self._host_api.settings("").guid + "T").create_template(
            name, self._DEFAULT_TEMPLATE
        )
        try:
            return self._find_template_guid(name)
        except KeyError:
            raise TemplateError("Failed to create template {}".format(self._name))

    @property
    def guid(self):
        """:obj:`str`: Guid шаблона"""
        return self._guid

    @guid.setter
    def guid(self, value):
        raise RuntimeError("You can't change object guid")

    @property
    def name(self):
        """:obj:`str`: Имя шаблона"""
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
            self._template_settings["name"] = value
        else:
            raise TypeError("Expected str, got {}".format(type(value).__name__))

    @property
    def content(self):
        """:obj:`str`: Контент шаблона"""
        return self._template_settings["content"]

    @content.setter
    def content(self, value):
        if isinstance(value, str):
            self._template_settings["content"] = value
        else:
            raise TypeError("Expected str, got {}".format(type(value).__name__))

    def delete(self):
        """Удаляет шаблон"""
        obj = BaseUtils.get_object(self.guid)
        if obj is None:
            raise TemplateError("Template object not found!")

        obj.delete_template()

    def show(self, monitor=1):
        """Открывает шаблон на указаном мониторе

        Args:
            monitor (:obj:`int`, optional): Номер монитора. По умолчанию ``monitor=1``
        """
        self._operator_gui.show(self.guid, monitor)


class TrObject(py_object):
    """Вспомогательный класс для работы с объектами Trassir

    Attributes:
        obj (:obj:`SE_Object`): Объект trassir :obj:`object('{guid}')` или :obj:`None`
        obj_methods (List[:obj:`str`]): Список методов объекта :attr:`TrObject.obj`
        name (:obj:`str`): Имя объекта или его guid
        guid (:obj:`str`): Guid объекта
        full_guid (:obj:`str`): Полный guid :obj:`{guid объекта}_{guid сервера}`
            или :obj:`None`
        type (:obj:`str`): Тип объекта, например :obj:`"RemoteServer"`, :obj:`"Channel"`,
            :obj:`"Grabber"`, :obj:`"User"`, и др.
        path (:obj:`str`): Путь в настройках или :obj:`None`
        parent (:obj:`str`): Guid родительского объекта или :obj:`None`
        server (:obj:`str`): Guid сервера или :obj:`None`
        settings (:obj:`SE_Settings`): Объект настроек ``settings('{path}')`` или :obj:`None`

    Raises:
        TypeError: Если неправильные параметры объекта
        ValueError: Если в имени объекта есть запятые
    """

    obj, name, guid, full_guid, type = None, None, None, None, None
    path, parent, server, settings = None, None, None, None

    def __init__(self, obj, host_api=host):
        self._host_api = host_api

        if isinstance(obj, host_api.ScriptHost.SE_Settings):
            self._load_from_settings(obj)
        elif isinstance(obj, tuple):
            if len(obj) == 4:
                self._load_from_tuple(obj)
            else:
                raise TypeError(
                    "Expected tuple(name, guid, type, parent), got tuple'{}'".format(
                        obj
                    )
                )
        else:
            raise TypeError("Unexpected object type '{}'".format(type(obj).__name__))

    @staticmethod
    def _check_object_name(object_name):
        """Check if object name hasn't got commas

        Args:
            object_name (str):

        Returns:
            str: object_name.strip()

        Raises:
            ValueError: If "," found in object name
        """
        if "," in object_name:
            raise ValueError(
                "Please, rename object '{}' without commas".format(object_name)
            )
        return object_name.strip()

    @staticmethod
    def _parse_server_from_path(path):
        """Parse server guid from full path

        Args:
            path (str): Full Trassir settings path;
                example: '/pV4ggECb/_persons/n68LOBhG' returns 'pV4ggECb'
        """
        try:
            server = path.split("/", 2)[1]
        except IndexError:
            server = None

        return server

    def _find_server_guid_for_object(self, object_guid):
        """Find server guid for object

        Args:
            object_guid (str): Object guid

        Returns:
            str: Server guid if server found
            None: If server not found
        """
        all_objects = {
            obj[1]: {"name": obj[0], "guid": obj[1], "type": obj[2], "parent": obj[3]}
            for obj in self._host_api.objects_list("")
        }

        def get_parent(child_guid):
            child = all_objects.get(child_guid, None)
            if child:
                if child["type"] == "Server":
                    return child["guid"]
                else:
                    return get_parent(child["parent"])
            else:
                return None

        return get_parent(object_guid)

    def _get_object_methods(self):
        """Get object methods"""
        if self.obj:
            return [method for method in dir(self.obj) if not method.startswith("__")]
        else:
            return []

    def _load_from_settings(self, obj):
        """Preparing attributes from SE_Settings object"""
        self.obj = BaseUtils.get_object(obj.guid)
        self.obj_methods = self._get_object_methods()

        try:
            obj_name = obj.name
        except KeyError:
            obj_name = obj.guid

        self.name = self._check_object_name(obj_name)
        self.guid = obj.guid
        self.type = obj.type
        self.path = obj.path
        self.server = self._parse_server_from_path(obj.path)
        self.settings = obj

        if self.server and self.server != self.guid:
            self.full_guid = "{0.guid}_{0.server}".format(self)

    def _load_from_tuple(self, obj):
        """Preparing attributes from tuple object"""
        self.obj = BaseUtils.get_object(obj[1])
        self.obj_methods = self._get_object_methods()
        self.name = self._check_object_name(obj[0])
        self.guid = obj[1]
        self.type = obj[2]
        self.parent = obj[3]
        self.server = self._find_server_guid_for_object(obj[1])

        if self.server and self.server != self.guid:
            self.full_guid = "{0.guid}_{0.server}".format(self)

    def __repr__(self):
        return "TrObject('{}')".format(self.name)

    def __str__(self):
        return "{self.type}: {self.name} ({self.guid})".format(self=self)


class ParameterError(ScriptError):
    """Ошибка в параметрах скрипта"""

    pass


class BasicObject(py_object):
    """"""

    def __init__(self, host_api=host):
        self._host_api = host_api
        self.this_server_guid = BaseUtils.get_server_guid()

    class UniqueNameError(ScriptError):
        """Имя объекта не уникально"""

        pass

    class ObjectsNotFoundError(ScriptError):
        """Не найдены объекты с заданными именами"""

        pass

    def _check_unique_name(self, objects, object_names):
        """Check if all objects name are unique

        Args:
            objects (list): Objects list from _get_objects_from_settings

        Raises:
            UniqueNameError: If some object name is not uniques
        """
        unique_names = []
        for obj in objects:
            if obj.name in object_names:
                if obj.name not in unique_names:
                    unique_names.append(obj.name)
                else:
                    raise self.UniqueNameError(
                        "Найдено несколько объектов {obj.type} с одинаковым именем '{obj.name}'! "
                        "Задайте уникальные имена".format(obj=obj)
                    )

    @staticmethod
    def _objects_str_to_list(objects):
        """Split object names if objects is str and strip each name

        Args:
            objects (str|list): Trassir object names in comma spaced string or list

        Returns:
            list: Stripped Trassir object names

        Raises:
            ScriptError: If object name selected more than once
        """
        if isinstance(objects, str):
            objects = objects.split(",")

        names = []
        for name in objects:
            strip_name = name.strip()
            if strip_name in names:
                raise ParameterError("Объект '{}' выбран несколько раз".format(name))
            names.append(strip_name)

        return names

    def _filter_objects_by_name(self, objects, object_names):
        """Filter object by names

        Args:
            objects (list): TrObject objects list
            object_names (str|list): Trassir object names in comma spaced string or list

        Raises:
            ObjectsNotFoundError: If len(object_name) != len(filtered_object)
        """
        object_names = self._objects_str_to_list(object_names)

        self._check_unique_name(objects, object_names)

        filtered_object = [obj for obj in objects if obj.name in object_names]

        if len(filtered_object) != len(object_names):
            channels_not_found = set(object_names) - set(
                obj.name for obj in filtered_object
            )

            try:
                object_type = objects[0].type
            except IndexError:
                object_type = "Unknown"

            raise self.ObjectsNotFoundError(
                "Не найдены объекты {object_type}: {names}".format(
                    object_type=object_type,
                    names=", ".join(name for name in channels_not_found),
                )
            )

        return filtered_object


class ObjectFromSetting(BasicObject):
    """"""

    def __init__(self):
        super(ObjectFromSetting, self).__init__()

    def _load_objects_from_settings(self, settings_path, obj_type, sub_condition=None):
        """Load objects from Trassir settings

        Args:
            settings_path (:obj:`str`): Trassir settings path. Example ``"scripts"``.
                Click F4 in the Trassir settings window to show hidden parameters.
            obj_type (:obj:`str` | :obj:`list`): Loading object type. Example ``"EmailAccount"``
            sub_condition (function, optional): Function with SE_Settings as argument to filter objects

        Returns:
            list: TrObject objects list
                Example [TrObject(...), TrObject(...), ...]
        """
        try:
            settings = self._host_api.settings(settings_path)
        except KeyError:
            settings = None

        objects = []
        if settings is not None:
            if isinstance(obj_type, str):
                obj_type = [obj_type]

            if sub_condition is None:
                sub_condition = BaseUtils.do_nothing

            for obj in settings.ls():
                if obj.type in obj_type:
                    if sub_condition(obj):
                        objects.append(TrObject(obj))
        return objects

    def _get_objects_from_settings(
        self,
        settings_path,
        object_type,
        object_names=None,
        server_guid=None,
        ban_empty_result=False,
        sub_condition=None,
    ):
        """Check if objects exists and returns list from _load_objects_from_settings

        Note:
             If object_names is not None - checking if all object names are unique

        Args:
            settings_path (:obj:`str`): Trassir settings path. Example ``"scripts"``.
                Click F4 in the Trassir settings window to show hidden parameters.
            object_type (:obj:`str` | :obj:`list`): Loading object type. Example ``"EmailAccount"``
            object_names (:obj:`str` | :obj:`list`, optional): Comma spaced string or
                list of object names. Default :obj:`None`
            server_guid (:obj:`str` | :obj:`list`, optional): Server guid. Default :obj:`None`
            ban_empty_result (:obj:`bool`, optional): If True - raise error if no one object found
            sub_condition (:obj:`func`, optional) : Function with SE_Settings as argument to filter objects

        Returns:
            list: Trassir list from _load_objects_from_settings

        Raises:
            ObjectsNotFoundError: If can't find channel
        """
        if object_names == "":
            raise ParameterError("'{}' не выбраны".format(object_type))

        if server_guid is None:
            server_guid = self.this_server_guid

        if isinstance(server_guid, str):
            server_guid = [server_guid]

        objects = []

        for guid in server_guid:
            objects += self._load_objects_from_settings(
                settings_path.format(server_guid=guid), object_type, sub_condition
            )

        if ban_empty_result and not objects:
            raise self.ObjectsNotFoundError(
                "Не найдено ниодного объекта '{}'".format(object_type)
            )

        if object_names is None:
            return objects

        else:
            return self._filter_objects_by_name(objects, object_names)


class Servers(ObjectFromSetting):
    """Класс для работы с серверами

    Examples:
        >>> srvs = Servers()
        >>> local_srv = srvs.get_local()
        [TrObject('Клиент')]
        >>> # Првоерим "Здоровье" локального сервера
        >>> local_srv[0].obj.state("server_health")
        'Health Problem'
    """

    def __init__(self):
        super(Servers, self).__init__()

    def get_local(self):
        """Возвращает локальный сервер (на котором запущен скрипт)

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._load_objects_from_settings("/", ["Client", "LocalServer"])

    def get_remote(self):
        """Возвращает список удаленных серверов

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._load_objects_from_settings("/", "RemoteServer")

    def get_all(self):
        """Возвращает список всех доступных серверов

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._load_objects_from_settings(
            "/", ["Client", "LocalServer", "RemoteServer"]
        )


class Channels(ObjectFromSetting):
    """Класс для работы с каналами

    See Also:
        `Каналы - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-channels-folder.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> channels = Channels()
        >>> selected_channels = channels.get_enabled("AC-D2121IR3W 2,AC-D9141IR2 1")
        >>> selected_channels
        [TrObject('AC-D2121IR3W 2'), TrObject('AC-D9141IR2 1')]
        >>>
        >>> # Включим ручную запись на выбранных каналах
        >>> for channel in selected_channels:
        >>>     channel.obj.manual_record_start()
        >>>
        >>> # Или добавим к имени канала его guid
        >>> for channel in selected_channels:
        >>>     channel.settings["name"] += " ({})".format(channel.guid)
    """

    def __init__(self, server_guid=None):
        super(Channels, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных каналов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            not_zombie = 1 - sett["archive_zombie_flag"]
            if not_zombie:
                try:
                    return self._host_api.settings(sett.cd("info")["grabber_path"])[
                        "grabber_enabled"
                    ]
                except KeyError:
                    return 0
            return 0

        return self._get_objects_from_settings(
            "/{server_guid}/channels",
            "Channel",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных каналов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            zombie = sett["archive_zombie_flag"]
            if not zombie:
                try:
                    return (
                        1
                        - self._host_api.settings(sett.cd("info")["grabber_path"])[
                            "grabber_enabled"
                        ]
                    )
                except KeyError:
                    return 1
            return 1

        return self._get_objects_from_settings(
            "/{server_guid}/channels",
            "Channel",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех каналов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/channels",
            "Channel",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Devices(ObjectFromSetting):
    """Класс для работы с ip устройствами

    See Also:
        `IP-устройства - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-ip-cameras-folder.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> devices = Devices()
        >>> enabled_devices = devices.get_enabled()
        >>> enabled_devices
        [TrObject('AC-D2121IR3W'), TrObject('AC-D5123IR32'), ...]
        >>>
        >>> # Перезагрузим все устройства
        >>> for dev in enabled_devices:
        >>>     dev.settings["reboot"] = 1
    """

    def __init__(self, server_guid=None):
        super(Devices, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных устройств

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["grabber_enabled"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/ip_cameras",
            "Grabber",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных устройств

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["grabber_enabled"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/ip_cameras",
            "Grabber",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех устройств

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/ip_cameras",
            "Grabber",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Scripts(ObjectFromSetting):
    """Класс для работы со скриптами

    See Also:
        `Скрипты - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-script-feature.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> scripts = Scripts()
        >>> all_scripts = scripts.get_all()
        >>> all_scripts
        [TrObject('Новый скрипт'), TrObject('HDD Health Monitor'), TrObject('Password Reminder')]
        >>>
        >>> # Отключим все скрипты
        >>> for script in all_scripts:
        >>>     script.settings["enable"] = 0
    """

    def __init__(self, server_guid=None):
        super(Scripts, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных скриптов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["enable"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Script",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных скриптов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["enable"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Script",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех скриптов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Script",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Rules(ObjectFromSetting):
    """Класс для работы с правилами

    See Also:
        `Правила - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-rule.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> rules = Rules()
        >>> all_rules = rules.get_all()
        >>> all_rules
        [TrObject('!Rule'), TrObject('NEW RULE'), TrObject('Новое правило')]
        >>>
        >>> # Отключим все правила
        >>> for rule in all_rules:
        >>>     rule.settings["enable"] = 0
    """

    def __init__(self, server_guid=None):
        super(Rules, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных правил

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["enable"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Rule",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных правил

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["enable"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Rule",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех правил

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен. По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Rule",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Schedules(ObjectFromSetting):
    """Класс для работы с расписаниями

    See Also:
        `Расписания - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-schedule.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> schedules = Schedules()
        >>> my_schedule = schedules.get_enabled("!Schedule")[0]
        >>> my_schedule.obj.state("color")
        'Red'
    """

    def __init__(self, server_guid=None):
        super(Schedules, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных расписаний

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["enable"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Schedule",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных расписаний

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["enable"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Schedule",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех расписаний

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Schedule",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class TemplateLoops(ObjectFromSetting):
    """Класс для работы с циклическими просмотрами шаблонов

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> tmplate_loops = TemplateLoops()
        >>> tmplate_loops.get_all()
        [TrObject('Новый циклический просмотр')]
    """

    def __init__(self, server_guid=None):
        super(TemplateLoops, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных циклических просмотров шаблонов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["enable"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "TemplateLoop",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных циклических просмотров шаблонов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["enable"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "TemplateLoop",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех циклических просмотров шаблонов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "TemplateLoop",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class EmailAccounts(ObjectFromSetting):
    """Класс для работы с E-Mail аккаунтами

    See Also:
        `Добавление учетной записи e-mail - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-email-account.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> email_accounts = EmailAccounts()
        >>> email_accounts.get_all()
        [TrObject('Новая учетная запись e-mail'), TrObject('MyAccount')]
    """

    def __init__(self, server_guid=None):
        super(EmailAccounts, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_all(self, names=None):
        """Возвращает список всех E-Mail аккаунтов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "EmailAccount",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class NetworkNodes(ObjectFromSetting):
    """Класс для работы с сетевыми подключениями

    See Also:
        `Сеть - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-network-folder.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> network_nodes = NetworkNodes("client")
        >>> network_nodes.get_enabled()
        [TrObject('QuattroStationPro (172.20.0.101)'), TrObject('NSK-HD-01 (127.0.0.1)')]
    """

    def __init__(self, server_guid=None):
        super(NetworkNodes, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных сетевых подключений

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["should_be_connected"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/network",
            "NetworkNode",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных сетевых подключений

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["should_be_connected"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/network",
            "NetworkNode",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех сетевых подключений

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/network",
            "NetworkNode",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class PosTerminals(ObjectFromSetting):
    """Класс для работы с POS Терминалами

    See Also:
        `Настройка POS-терминалов - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-pos-terminals-folder.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> pos_terminals = PosTerminals()
        >>> pos_terminals.get_disabled()
        [TrObject('Касса (1)')]
    """

    def __init__(self, server_guid=None):
        super(PosTerminals, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных POS Терминалов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["pos_enable"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/pos_folder2/terminals",
            "PosTerminal",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных POS Терминалов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["pos_enable"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/pos_folder2/terminals",
            "PosTerminal",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех POS Терминалов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/pos_folder2/terminals",
            "PosTerminal",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Users(ObjectFromSetting):
    """Класс для работы с пользователями и их группами.

    See Also:
        `Пользователи - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-users-folder.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> users = Users()
        >>> users.get_groups()
        [TrObject('TEST')]
    """

    def __init__(self, server_guid=None):
        super(Users, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_groups(self, names=None):
        """Возвращает список групп пользователей

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_settings(
            "/{server_guid}/users",
            "Group",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_users(self, names=None):
        """Возвращает список пользователей

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_settings(
            "/{server_guid}/users",
            "User",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_users_by_groups(self, group_names):
        """Возвращает список пользователей из указанных групп

        Args:
            group_names (:obj:`str` | :obj:`list`): :obj:`str` - имена групп,
                разделенные запятыми или :obj:`list` - список имен.

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        if group_names is None:
            groups = [""]
        else:
            groups = [group.guid for group in self.get_groups(names=group_names)]

        def sub_condition(sett):
            return sett["group"] in groups

        return self._get_objects_from_settings(
            "/{server_guid}/users",
            "User",
            object_names=None,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )


class Templates(ObjectFromSetting):
    """Класс для работы с существующими шаблонами.

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> templates = Templates(BaseUtils.get_server_guid())
        >>> templates.get_all()
        [TrObject('Parking'), TrObject('FR'), TrObject('AT'), TrObject('AD+')]
    """

    def __init__(self, server_guid=None):
        super(Templates, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_all(self, names=None):
        """Возвращает список шаблонов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_settings(
            "/{server_guid}/templates",
            "Template",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Persons(ObjectFromSetting):
    """Класс для работы с персонами и их папками.

    See Also:
        `Персоны - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-persons-folder.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
            >>> persons = Persons()
            >>> persons.get_folders()
            [TrObject('Мошенники'), TrObject('DSSL'), TrObject('persons')]
            >>> persons.get_persons()
            [
                {
                    'name': 'Leonardo',
                    'guid': 'cJuJYAha',
                    'gender': 0,
                    'birth_date': '1980-01-01',
                    'comment': 'Comment',
                    'contact_info': 'Contact info',
                    'folder_guid': 'n68LOBhG',
                    'image': <image, str>,
                    'image_guid': 'gBHZ2vpz',
                    'effective_rights': 0,
                },
                ...
            ]
            >>> persons.get_person_by_guid("cJuJYAha")
            {
                'name': 'Leonardo',
                'guid': 'cJuJYAha',
                'gender': 0,
                'birth_date': '1980-01-01',
                'comment': 'Comment',
                'contact_info': 'Contact info',
                'folder_guid': 'n68LOBhG',
                'image': <image, str>,
                'image_guid': 'gBHZ2vpz',
                'effective_rights': 0,
            }
    """

    _PERSONS_UPDATE_TIMEOUT = 10 * 60  # Time in sec between update _persons dict

    def __init__(self, server_guid=None):
        super(Persons, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        if isinstance(server_guid, str):
            server_guid = [server_guid]

        self.server_guid = server_guid

        self._persons = None

    def _update_persons_dict(self, timeout=10):
        """Updating self._persons dict"""
        persons = self.get_persons(timeout=timeout)
        by_guid, by_name = {}, {}
        for person in persons:
            by_guid[person["guid"]] = person
            by_name[person["name"]] = person

        self._persons = {
            "update_ts": int(time.time()),
            "by_guid": by_guid,
            "by_name": by_name,
        }

    def _check_loaded_persons(self, timeout=10):
        """This method check if self._persons dict is need to be updated"""
        ts_now = int(time.time())

        if (
            self._persons is None
            or (ts_now - self._persons["update_ts"]) > self._PERSONS_UPDATE_TIMEOUT
        ):
            self._update_persons_dict(timeout=timeout)

    def get_folders(self, names=None):
        """Возвращает список папок персон

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        try:
            folders = self._get_objects_from_settings(
                "/{server_guid}/persons",
                "PersonsSubFolder",
                object_names=names,
                server_guid=self.server_guid,
            )

            if names is None or "persons" in names:
                for guid in self.server_guid:
                    try:
                        settings = self._host_api.settings("/{}/persons".format(guid))
                    except KeyError:
                        continue

                    folders.append(TrObject(settings))

        except self.ObjectsNotFoundError as err:
            folders = []
            names = self._objects_str_to_list(names)

            if names is None or "persons" in names:
                for guid in self.server_guid:
                    try:
                        settings = self._host_api.settings("/{}/persons".format(guid))
                    except KeyError:
                        continue

                    folders.append(TrObject(settings))

            if not folders:
                raise err

        return folders

    def get_persons(self, folder_names=None, timeout=10):
        """Возвращает список персон

        Note:
            Данный метод работает только с локальной БД.

        Args:
            folder_names (:obj:`str` | List[:obj:`str`], optional): :obj:`str` -
                названия папок персон, разделенные запятыми или :obj:`list` -
                список папок персон. По умолчанию :obj:`None`
            timeout (:obj:`int`, optional): Макс. время запроса к БД.
                По умолчанию ``timeout=10``

        Returns:
            List[:obj:`dict`]: Список персон - если персоны найдены

        Raises:
            EnvironmentError: Если произошла ошибка при запросе в БД.
            TrassirError: Если в данной сборке Trassir нет метода :obj:`host.service_persons_get`
        """
        tmp_server_guid = self.server_guid[:]
        self.server_guid = [self.this_server_guid]
        persons_folders = self.get_folders(names=folder_names)
        self.server_guid = tmp_server_guid[:]

        try:
            persons = self._host_api.service_persons_get(
                [folder.guid for folder in persons_folders], True, 0, 0, timeout
            )
        except AttributeError:
            raise TrassirError(
                "Данный функционал не поддерживается вашей сборкой Trassir. "
                "Попробуйте обновить ПО."
            )

        if isinstance(persons, str):
            raise EnvironmentError(persons)

        return persons

    def get_person_by_guid(self, person_guid, timeout=10):
        """Возвращает информацию о персоне по его guid

        Note:
            Для уменьшения кол-ва запросов к БД - метод создает локальную
            копию всех персон при первом запросе и обновляет ее вместе
            с последующими запросами не чаще чем 1 раз в 10 минут.

        Args:
            person_guid (:obj:`str`): Guid персоны
            timeout (:obj:`int`, optional): Макс. время запроса к БД.
                По умолчанию ``timeout=10``

        Returns:
            :obj:`dict`: Даные о персоне или :obj:`None` если персона не найдена
        """
        self._check_loaded_persons(timeout=timeout)
        return self._persons["by_guid"].get(person_guid)

    def get_person_by_name(self, person_name, timeout=10):
        """Возвращает информацию о персоне по его имени

        Note:
            Для уменьшения кол-ва запросов к БД - метод создает локальную
            копию всех персон при первом запросе и обновляет ее вместе
            с последующими запросами не чаще чем 1 раз в 10 минут.

        Args:
            person_name (:obj:`str`): Имя персоны
            timeout (:obj:`int`, optional): Макс. время запроса к БД.
                По умолчанию ``timeout=10``

        Returns:
            :obj:`dict`: Даные о персоне или :obj:`None` если персона не найдена
        """
        self._check_loaded_persons(timeout=timeout)
        return self._persons["by_name"].get(person_name)


class ObjectFromList(BasicObject):
    """"""

    def __init__(self):
        super(ObjectFromList, self).__init__()

    def _load_objects_from_list(self, obj_type, sub_condition=None):
        """Load objects from Trassir objects_list method

        Args:
            obj_type (str | list): Loading object type; example: "EmailAccount"
            sub_condition (function, optional): Function with SE_Settings as argument to filter objects

        Returns:
            list: TrObject objects list
                Example [TrObject(...), TrObject(...), ...]
        """
        if sub_condition is None:
            sub_condition = BaseUtils.do_nothing

        objects = []
        for obj in self._host_api.objects_list(obj_type):
            if sub_condition(obj):
                objects.append(TrObject(obj))

        return objects

    def _get_objects_from_list(
        self,
        object_type,
        object_names=None,
        server_guid=None,
        ban_empty_result=False,
        sub_condition=None,
    ):
        """Check if objects exists and returns list from _load_objects_from_settings

        Note:
             If object_names is not None - checking if all object names are unique

        Args:
            object_type (str|list): Loading object type; example: "EmailAccount"
            object_names (str|list, optional): Comma spaced string or list of object names; default: None
            server_guid (str|list, optional): Server guids; default: None
            ban_empty_result (bool, optional): If True - raise ObjectsNotFoundError if no one object found
            sub_condition (func, optional) : Function with SE_Settings as argument to filter objects

        Returns:
            list: Trassir list from _load_objects_from_settings

        Raises:
            ObjectsNotFoundError: If can't find channel
        """
        if object_names == "":
            raise ParameterError("'{}' не выбраны".format(object_type))

        if server_guid is None:
            server_guid = self.this_server_guid
        else:
            if isinstance(server_guid, str):
                server_guid = [server_guid]

        objects = self._load_objects_from_list(object_type, sub_condition)

        objects = [obj for obj in objects if obj.server in server_guid]

        if ban_empty_result and not objects:
            raise self.ObjectsNotFoundError(
                "Не найдено ниодного объекта '{}'".format(object_type)
            )

        if object_names is None:
            return objects

        else:
            return self._filter_objects_by_name(objects, object_names)

    def _zone_type(self, zone_obj):
        """Возвращает тип зоны для объекта

        Args:
            zone_obj (:obj:`SE_Object`): Объект trassir ``object('{guid}')``

        Returns:
            :obj:`str`: Тип объекта
            :obj:`None`: Если тип зоны неизвестен
        """

        if not isinstance(zone_obj, self._host_api.ScriptHost.SE_Object):
            raise TypeError(
                "Expected SE_Object, got '{}'".format(type(zone_obj).__name__)
            )

        try:
            guid = zone_obj.guid
            channel, server = zone_obj.associated_channel.split("_")
        except (AttributeError, ValueError):
            return None

        try:
            zones_dir = self._host_api.settings(
                "/{}/channels/{}/people_zones".format(server, channel)
            )
            for i in xrange(16):
                if zones_dir["zone%02d_guid" % i] == guid:
                    func_type = zones_dir["zone%02d_func_type" % i]
                    if isinstance(func_type, int):
                        return (
                            ["Queue", "Workplace"][func_type]
                            if func_type in range(2)
                            else "Queue"
                        )
                    else:
                        return func_type
        except KeyError:
            "not a queue or workplace"

        try:
            zones_dir = self._host_api.settings(
                "/{}/channels/{}/workplace_zones".format(server, channel)
            )
            for i in xrange(16):
                if zones_dir["zone%02d_guid" % i] == guid:
                    return "Workplace"
        except KeyError:
            "not a workplace"

        try:
            zones_dir = settings("/%s/channels/%s/deep_people" % (server, channel))
            for i in xrange(16):
                if zones_dir["zone%02d_guid" % i] == guid:
                    if zones_dir["zone%02d_type" % i] in ["border", "border_swapped"]:
                        return "Border"
                    else:
                        return "Queue"
        except KeyError:
            "not a deep people queue"


class GPIO(ObjectFromList):
    """Класс для работы с тревожными входами/выходами

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> gpio = GPIO()
        >>> gpio_door = gpio.get_inputs("Door")[0]
        >>> gpio_door.obj.state("gpio_input_level")
        'Input Low (Normal High)'
        >>> gpio_light = gpio.get_outputs("Light")[0]
        >>> gpio_light.obj.set_output_high()
    """

    def __init__(self, server_guid=None):
        super(GPIO, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_inputs(self, names=None):
        """Возвращает список тревожных входов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "GPIO Input",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_outputs(self, names=None):
        """Возвращает список тревожных выходов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "GPIO Output",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Zones(ObjectFromList):
    """Класс для работы с зонами

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> zones = Zones()
        >>> zones.get_queues("Касса 1")[0].obj.state("zone_queue")
        '5+'
    """

    def __init__(self, server_guid=None):
        super(Zones, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_people(self, names=None):
        """Возвращает список PeopleZones

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "PeopleZone",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_simt(self, names=None):
        """Возвращает список зон SIMT

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "SIMT Zone",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_workplaces(self, names=None):
        """Возвращает список рабочих зон

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        people_zones = self.get_people(names=names)

        return [
            zone
            for zone in people_zones
            if self._zone_type(zone.obj) in ["Workplace", "Рабочее место"]
        ]

    def get_queues(self, names=None):
        """Возвращает список зон очередей

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        people_zones = self.get_people(names=names)

        return [
            zone
            for zone in people_zones
            if self._zone_type(zone.obj) in ["", "Queue", "Очередь"]
        ]

    def get_shelves(self, names=None):
        """Возвращает список зон полок

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "Shelf",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Borders(ObjectFromList):
    """Класс для работы с линиями пересечения

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> borders = Borders()
        >>> borders.get_simt()
        [TrObject('DBOP')]
        >>> borders.get_all()
        [TrObject('Вход в офис'), TrObject('DBOP')]
    """

    def __init__(self, server_guid=None):
        super(Borders, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_head(self, names=None):
        """Возвращает список HeadBorders

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "HeadBorder",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_people(self, names=None):
        """Возвращает список PeopleBorders

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "PeopleBorder",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_simt(self, names=None):
        """Возвращает список SIMT Borders

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "SIMT Border",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_deep_people(self, names=None):
        """Возвращает список DeepPeopleBorders

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        people_zones = self._get_objects_from_list(
            "PeopleZone",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

        return [zone for zone in people_zones if self._zone_type(zone.obj) == "Border"]

    def get_all(self, names=None):
        """Возвращает список всех линий пересечения

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        all_borders = (
            self.get_head()
            + self.get_people()
            + self.get_simt()
            + self.get_deep_people()
        )

        if names is None:
            return all_borders
        else:
            return self._filter_objects_by_name(all_borders, names)


class Sigur(ObjectFromList):
    """Класс для работы со СКУД Sigur

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.
    """

    def __init__(self, server_guid=None):
        super(Sigur, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_access_points(self, names=None):
        """Возвращает список точек доступа

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "Access Point",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class TrassirError(ScriptError):
    """Exception if bad trassir version"""

    pass


class PokaYoke(py_object):
    """Класс для защиты от дурака

    Позволяет блокировать запуск скрипта на ПО, где это
    не предусмотрено (например, на клиенте или TOS).
    А также производить некоторые другие проверки.
    """

    _EMAIL_REGEXP = re.compile(
        r"[^@]+@[^@]+\.[^@]+"
    )  # Default regex to check emails list
    _PHONE_REGEXP = re.compile(r"[^\d,;]")  # Default regex to check phone list

    _host_api = host

    def __init__(self):
        pass

    @staticmethod
    def ban_tos():
        """Блокирует запуск скрипта на `Trassir OS`

        Raises:
            OSError: Если скрипт запускается на `Trassir OS`

        Examples:
            >>> PokaYoke.ban_tos()
            OSError: Скрипт недоступен для TrassirOS
        """
        if os.name != "nt":
            raise OSError("Скрипт недоступен для TrassirOS")

    @staticmethod
    def ban_win():
        """Блокирует запуск скрипта на `Windows OS`

        Raises:
            OSError: Если скрипт запускается на `Windows OS`

        Examples:
            >>> PokaYoke.ban_win()
            OSError: Скрипт недоступен для WindowsOS
        """
        if os.name == "nt":
            raise OSError("Скрипт недоступен для WindowsOS")

    @staticmethod
    def ban_client():
        """Блокирует запуск скрипта на `Trassir Client`

        Raises:
            TrassirError: Если скрипт запускается на `Trassir Client`

        Examples:
            >>> PokaYoke.ban_client()
            TrassirError: Скрипт недоступен для клиентской версии Trassir
        """
        if BaseUtils.get_server_guid() == "client":
            raise TrassirError("Скрипт недоступен для клиентской версии Trassir")

    @classmethod
    def ban_daemon(cls):
        """Блокирует запуск скрипта на сервре Trassir, который запущен как служба

        Raises:
            TrassirError: Если скрипт запускается на сервре Trassir,
                который запущен как служба

        Examples:
            >>> PokaYoke.ban_daemon()
            TrassirError: Скрипт недоступен для Trassir запущенным как служба
        """
        if cls._host_api.settings("system_wide_options")["daemon"]:
            raise TrassirError("Скрипт недоступен для Trassir запущенным как служба")

    @staticmethod
    def check_email_account(account_name):
        """Проверяет существование E-Mail аккаунта

        Args:
            account_name (:obj:`str`): Имя E-Mail аккаунта

        Returns:
             List[:class:`TrObject`]: Список объектов

        Raises:
            ParameterError: Если аккаунт не выбран
            ObjectsNotFoundError: Если аккаунт не найден

        Examples:
            >>> PokaYoke.check_email_account("")
            ParameterError: 'EmailAccount' не выбраны
            >>> PokaYoke.check_email_account("YourAccount")
            ObjectsNotFoundError: Не найдены объекты EmailAccount: YourAccount
            >>> PokaYoke.check_email_account("MyAccount")
            [TrObject('MyAccount')]
        """
        e_accounts = EmailAccounts(BaseUtils.get_server_guid())
        return e_accounts.get_all(account_name)

    @classmethod
    def parse_emails(cls, mailing_list, regex=None):
        """Парсит email дреса из строки

        Каждый email проверяется с помощью regex ``r"[^@]+@[^@]+\.[^@]+"``.

        Args:
            mailing_list (:obj:`str`): Список email адресов, разделенный запятыми
            regex (:obj:`SRE_Pattern`, optional): Новый regex шаблон для проверки.
                По умолчанию :obj:`None`

        Returns:
            List[:obj:`str`]: Список адресов

        Raises:
            ParameterError: Если найден невалидный email

        Examples:
            >>> PokaYoke.parse_emails("a.trubilil!dssl.ru,support@dssl.ru")
            ParameterError: Email 'a.trubilil!dssl.ru' is not valid!
            >>>
            >>> PokaYoke.parse_emails("a.trubilil@dssl.ru,support@dssl.ru")
            ['a.trubilil@dssl.ru', 'support@dssl.ru']
        """
        mailing_list = mailing_list.replace(" ", "")

        if not mailing_list:
            raise ParameterError("No emails to send!")

        if regex is None:
            regex = cls._EMAIL_REGEXP
        else:
            if not isinstance(regex, cls._EMAIL_REGEXP.__class__):
                raise TypeError(
                    "Expected re.compile, got '{}'".format(type(regex).__name__)
                )

        if isinstance(mailing_list, str):
            mailing_list = mailing_list.split(",")

        mailing_list = [mail.strip() for mail in mailing_list]

        for mail in mailing_list:
            if not regex.match(mail):
                raise ParameterError("Email '{}' is not valid!".format(mail))

        return mailing_list

    @classmethod
    def check_phones(cls, phones, regex=None):
        """Проверяет строку на валидность телефонных номеров

        Строка проверяется с помощью regex ``r"[^\d,;]"``.

        Args:
            phones (:obj:`str`): Список телефонов, разделенный запятыми или точкой с запятой
            regex (:obj:`SRE_Pattern`, optional): Новый regex шаблон для проверки.
                По умолчанию :obj:`None`

        Returns:
            :obj:`str`: Список номеров телефона

        Raises:
            ParameterError: Если найден невалидный номер телефона

        Examples:
            >>> PokaYoke.check_phones("79999999999,78888888888A")
            ParameterError: Bad chars in phone list: `A`
            >>>
            >>> PokaYoke.check_phones("a.trubilil@dssl.ru,support@dssl.ru")
            '79999999999,78888888888'
        """
        phones = phones.replace(" ", "")

        if not phones:
            raise ParameterError("No phones!")

        if regex is None:
            regex = cls._PHONE_REGEXP
        else:
            if not isinstance(regex, cls._PHONE_REGEXP.__class__):
                raise TypeError(
                    "Expected re.compile, got '{}'".format(type(regex).__name__)
                )
        bad_chars = regex.findall(phones)
        if bad_chars:
            raise ParameterError(
                "Bad chars in phone list: `{}`".format(", ".join(bad_chars))
            )

        return phones


class SenderError(Exception):
    """Base Sender Exception"""

    pass


class Sender(py_object):
    _HTML_IMG_TEMPLATE = """<img src="data:image/png;base64,{img}" {attr}>"""

    def __init__(self, host_api=host):
        self._host_api = host_api

    @staticmethod
    def _get_base64(image_path):
        """Returns base64 image

        Args:
            image_path (str): Image full path
        """
        image_path = BaseUtils.win_encode_path(image_path)
        if os.path.isfile(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read())

    @staticmethod
    def _get_html_img(image_base64, **kwargs):
        """Returns html img

        Args:
            image_base64 (str): Base64 image
        """
        return BaseUtils.base64_to_html_img(image_base64, **kwargs)

    def text(self, text):
        """Send text

        Args:
            text (str): Text message
        """
        pass

    def image(self, image_path, text=""):
        """Send image and optional text

        Args:
            image_path (str): Image path
            text (str, optional): Text message; default: ""
        """
        pass

    def files(self, file_paths, text=""):
        """Send file or list of files

        Args:
            file_paths (str|list): File path or list of paths
            text (str, optional): Text message; default: ""
        """
        pass


class PopupSender(Sender):
    """Класс для показа всплывающих окон в правом нижнем углу экрана

    Args:
        width (:obj:`int`, optional): Ширина изображения, px.
            По умолчанию :obj:`width=400`

    Examples:
        >>> sender = PopupSender(300)
        >>> sender.text("Hello World!")

            .. image:: images/popup_sender.text.png

        >>> sender.image(r"manual\en\cloud-devices-16.png")

            .. image:: images/popup_sender.image.png
    """

    def __init__(self, width=400):
        super(PopupSender, self).__init__()
        self._attr = {"width": width}

    def text(self, text, popup_type="message"):
        """Показывает текст во всплывающем окне

        Вызывает один из методов Trassir :obj:`host.alert`,
        :obj:`host.message` или :obj:`host.error` с текстом

        Args:
            text (:obj:`str`): Текст сообщения
            popup_type (:obj:`"message"` | :obj:`"alert"` | :obj:`"error"`, optional)
                Тип сообщения. По умолчанию :obj:`"message"`
        """

        if popup_type == "alert":
            self._host_api.alert(text)
        elif popup_type == "error":
            self._host_api.error(text)
        else:
            self._host_api.message(text)

    def image(self, image_path, text="", popup_type=None):
        """Показывает изображение во всплывающем окне

        Args:
            image_path (:obj:`str`): Полный путь до изображения
            text (:obj:`str`, optional): Текст сообщения. По умолчанию :obj:`""`
            popup_type (:obj:`"message"` | :obj:`"alert"` | :obj:`"error"`, optional)
                Тип сообщения. По умолчанию :obj:`"message"`
        """
        image_base64 = self._get_base64(image_path)

        if not image_base64:
            self.text("<b>File not found</b><br>{}".format(image_path), popup_type)
            return

        html_image = BaseUtils.base64_to_html_img(image_base64, **self._attr)

        html = "{image}"
        if text:
            html = "<b>{text}</b><br>{image}"

        self.text(html.format(text=text, image=html_image), popup_type)


class PopupWithBtnSender(Sender):
    """Класс для показа всплывающих окон с кнопкой `Оk`

    Note:
        | Для закрытия окна необходимо нажать кнопку `Ok` в течении 60 сек.
        | После 60 сек окно закрывается автоматически.

    Args:
        width (:obj:`int`, optional): Ширина изображения, px.
            По умолчанию :obj:`width=800`

    Examples:
        >>> sender = PopupWithBtnSender()
        >>> sender.text("Hello World!")

            .. image:: images/popup_with_btn_sender.text.png

        >>> sender.image(r"manual\en\cloud-devices-16.png")

            .. image:: images/popup_with_btn_sender.image.png
    """

    def __init__(self, width=800):
        super(PopupWithBtnSender, self).__init__()
        self._attr = {"width": width}

    def text(self, text):
        """Показывает текст во всплывающем окне

        Вызывает метод Trassir :obj:`host.question` с текстом

        Args:
            text (:obj:`str`): Текст сообщения
        """
        self._host_api.question(
            "<pre>{}</pre>".format(text), "Ok", BaseUtils.do_nothing
        )

    def image(self, image_path, text=""):
        """Показывает изображение во всплывающем окне

        Args:
            image_path (:obj:`str`): Полный путь до изображения
            text (:obj:`str`, optional): Текст сообщения. По умолчанию :obj:`""`
        """
        image_base64 = self._get_base64(image_path)

        if not image_base64:
            self.text("<b>File not found</b><br>{}".format(image_path))
            return

        html_image = BaseUtils.base64_to_html_img(image_base64, **self._attr)

        html = "{image}"
        if text:
            html = "<b>{text}</b><br>{image}"

        self.text(html.format(text=text, image=html_image))


class EmailSender(Sender):
    """Класс для отправки уведомлений, изображений и файлов на почту

    Note:
        По умолчанию тема сообщений соответствует шаблону
        ``{server_name} -> {script_name}``

    Tip:
        При отправке изображения с текстом предпочтительней использовать метод
        :meth:`EmailSender.image` с необязательным аргументом :obj:`text` чем
        :meth:`EmailSender.text` с необазательным аргументом :obj:`attachments`

    Args:
        account (:obj:`str`): E-Mail аккаунт trassir. Проверяется
            методом :meth:`PokaYoke.check_email_account`
        mailing_list (:obj:`str`): Список email адресов для отправки писем
            разделенный запятыми. Проверяется и парсится в список методом
            :meth:`PokaYoke.parse_emails`
        subject (:obj:`str`, optional): Общая тема для сообщений.
            По умолчанию :obj:`None`
        max_size (:obj:`int`, optional): Максимальный размер вложения, байт.
            По умолчанию 25 * 1024 * 1024

    Examples:
        >>> sender = EmailSender("MyAccount", "my_mail@google.com")
        >>> sender.text("Hello World!")

            .. image:: images/email_sender.text.png

        >>> sender.image(r"manual\en\cloud-devices-16.png")

            .. image:: images/email_sender.image.png

        >>> sender.files([r"manual\en\cloud.html", r"manual\en\cloud.png"])

            .. image:: images/email_sender.files.png
    """

    def __init__(self, account, mailing_list, subject=None, max_size=None):
        super(EmailSender, self).__init__()

        PokaYoke.check_email_account(account)

        self.max_size = max_size or 25 * 1024 * 1024

        self._account = account
        self._mailing_list = PokaYoke.parse_emails(mailing_list)

        self._subject_default = subject or self._generate_subject()

    def _generate_subject(self):
        """Returns `server name` -> `script name`"""
        subject = "{server_name} -> {script_name}".format(
            server_name=self._host_api.settings("").name,
            script_name=self._host_api.stats().parent()["name"],
        )
        return subject

    def _group_files_by_max_size(self, file_paths, max_size):
        """Split files to groups. Size of each group is less then max_size

        Args:
            file_paths (list): List of files
            max_size (int): Max group size, bytes
        """
        group = []
        cur_size = 0
        for idx, file_path in enumerate(file_paths):
            file_size = os.stat(BaseUtils.win_encode_path(file_path)).st_size
            if not cur_size or (cur_size + file_size) < max_size:
                cur_size += file_size
                group.append(file_path)
            else:
                break
        else:
            return [group]

        return [group] + self._group_files_by_max_size(file_paths[idx:], max_size)

    def text(self, text, subject=None, attachments=None):
        """Отправка текстового сообщения

        Args:
            text (:obj:`str`): Текст сообщения
            subject (:obj:`str`, optional): Новая тема сообщения.
                По умолчанию :obj:`None`
            attachments (:obj:`list`, optional): Список вложений.
                По умолчанию :obj:`None`
        """
        if attachments is None:
            attachments = []
        self._host_api.send_mail_from_account(
            self._account,
            self._mailing_list,
            subject or self._subject_default,
            text,
            attachments,
        )

    def image(self, image_path, text="", subject=None):
        """Отправка изображения

        Args:
            image_path (:obj:`str`): Полный путь до изображения
            text (:obj:`str`, optional): Текст сообщения.
                По умолчанию :obj:`""`
            subject (:obj:`str`, optional): Новая тема сообщения.
                По умолчанию :obj:`None`
        """
        self.files([image_path], text=text, subject=subject)

    def files(self, file_paths, text="", subject=None, callback=None):
        """Отправка файлов

        Note:
            Если отправляется несколько файлов они могут быть разделены на
            несколько сообщений, основываясь на максимальном размере вложений.

        Args:
            file_paths (:obj:`str` | :obj:`list`): Путь до файла или список
                файлов для отправки
            text (:obj:`str`, optional): Текст сообщения.
                По умолчанию :obj:`""`
            subject (:obj:`str`, optional): Новая тема сообщения.
                По умолчанию :obj:`None`
            callback (:obj:`function`, optional): Функция, которая вызывается после
                отправки частей
        """
        if isinstance(file_paths, str):
            file_paths = [file_paths]

        if callback is None:
            callback = BaseUtils.do_nothing

        files_to_send = []
        for path in file_paths:
            if BaseUtils.is_file_exists(path):
                files_to_send.append(path)
            else:
                text += "\nFile not found: {}".format(path)

        file_groups = self._group_files_by_max_size(files_to_send, self.max_size)

        for grouped_files in file_groups:
            self.text(text, subject=subject, attachments=grouped_files)
            callback(grouped_files)


class TelegramSender(Sender):
    """Работа с телеграм ботом `@trassirbot <https://t.me/trassirbot>`_

    Warnings:
        | Cкрипт должен быть запущен на **сервере** Trassir.
        | На Клиенте скрипт вызовет ошибку ``ServerKeyError``

    Args:
        telegram_ids (:obj:`str`): Id пользователей, через запятую.

    Examples:
        >>> sender = TelegramSender("123456789")
        >>> sender.text("Hello World!")

            .. image:: images/telegram_sender.text.png

        >>> sender.image(r"manual\en\cloud-devices-16.png")

            .. image:: images/telegram_sender.image.png

        >>> sender.files([r"manual\en\cloud.html", r"manual\en\cloud.png"])

            .. image:: images/telegram_sender.files.png
    """

    def __init__(self, telegram_ids):
        super(TelegramSender, self).__init__()
        self._tbot_api = TBotAPI(telegram_ids)

    def text(self, text, tg_users=None, clear_msg=False):
        """Отправка текстового сообщения

        Args:
            text (:obj:`str`): Текст сообщения.
            tg_users (List[:obj:`int`], optional): Список id пользователей
                telegram для отправки отдельных сообщений. По умолчанию :obj:`None`
            clear_msg (:obj:`bool`, optional): Если :obj:`True` - добавляет
                имя сервера и скрипта к сообщению. По умолчанию :obj:`False`
        """

        self._tbot_api.send_message(text, tg_users=tg_users, clear_msg=clear_msg)

    def image(self, image_path, text="", tg_users=None):
        """Отправка изображения

        Args:
            image_path (:obj:`str`): Полный путь до изображения
            text (:obj:`str`, optional): Текст сообщения.
                По умолчанию :obj:`""`
            tg_users (List[:obj:`int`], optional): Список id пользователей
                telegram для отправки отдельных сообщений. По умолчанию :obj:`None`
        """
        if not os.path.isfile(image_path):
            self.text("Image not found: {}".format(image_path))
            return

        self._tbot_api.send_image(image_path, caption=text, tg_users=tg_users)

    def files(self, file_paths, text="", tg_users=None):
        """Отправка файлов

        Args:
            file_paths (:obj:`str` | :obj:`list`): Путь до файла или список
                файлов для отправки
            text (:obj:`str`, optional): Текст сообщения.
                По умолчанию :obj:`""`
            tg_users (List[:obj:`int`], optional): Список id пользователей
                telegram для отправки отдельных сообщений. По умолчанию :obj:`None`
        """
        if isinstance(file_paths, str):
            file_paths = [file_paths]

        if text and len(file_paths) == 1:
            self.text(text, tg_users=tg_users)
            text = ""

        files_not_found_text = ""
        for path in file_paths:
            if os.path.isfile(BaseUtils.win_encode_path(path)):
                self._tbot_api.send_document(path, caption=text, tg_users=tg_users)
            else:
                files_not_found_text += "\nFile not found: {}".format(path)

        if files_not_found_text:
            self.text(files_not_found_text)


class SMSCSenderError(SenderError):
    """Raises with SMSCSender errors"""

    pass


class SMSCSender(Sender):
    """Класс для отправки сообщений с помощью сервиса smsc.ru

    See Also:
        `https://smsc.ru/api/http/ <https://smsc.ru/api/http/>`_

    Note:
        | Номера проверяются методом
          :meth:`PokaYoke.check_phones`
        | Также при первом запуске скрипт проверяет данные авторизации

    Warnings:
        | По умолчанию сервис smsc.ru отправляет сообщения от своего имени *SMSC.RU.*
          При этом отправка на номера Мегафон/Йота **недоступна** т.к. имя *SMSC.RU*
          заблокировано оператором.
        |
        | Мы настоятельно **НЕ** рекомендуем использовать стандартное имя *SMSC.RU.*
        |
        | Для отправки смс от вашего буквенного имени необходимо его
          создать в разделе - https://smsc.ru/senders/ и зарегистрировать для
          операторов в колонке Действия по кнопке Изменить (после заключения договора
          согласно инструкции - https://smsc.ru/contract/info/ ) а также приложить
          гарантийное письмо на МТС в личный кабинет http://smsc.ru/documents/ и
          отправить на почту inna@smsc.ru

    Args:
        login (:obj:`str`): SMSC Логин
        password (:obj:`str`): SMSC Пароль
        phones (:obj:`str`): Список номеров для отправки смс резделенный
            запятыми или точкой с запятой
        translit(:obj:`bool`, optional): Переводить сообщение в
            транслит. По умолчанию :obj:`True`

    Raises:
        SMSCSenderError: При любых ошибках с отправкой сообщения

    Examples:
        >>> sender = SMSCSender("login", "password", "79999999999")
        >>> sender.text("Hello World!")

            .. image:: images/smsc_sender.text.png
    """

    _BASE_URL = "https://smsc.ru/sys/send.php?{params}"
    _ERROR_CODES = {
        1: "URL Params error",
        2: "Invalid login or password",
        3: "Not enough money",
        4: "Your IP is temporary blocked. More info: https://smsc.ru/faq/99",
        5: "Bad date format",
        6: "Message is denied (by text or sender name)",
        7: "Bad phone format",
        8: "Can't send message to this number",
        9: "Too many requests",
    }

    def __init__(self, login, password, phones, translit=True):
        super(SMSCSender, self).__init__()
        if not login:
            raise SMSCSenderError("Empty login")
        if not password:
            raise SMSCSenderError("Empty password")

        self._params = {
            "login": urllib.quote(login),  # Login
            "psw": urllib.quote(password),  # Password or MD5 hash
            "phones": urllib.quote(
                PokaYoke.check_phones(phones)
            ),  # Comma or semicolon spaced phone list
            "fmt": 3,  # Response format: 0 - string; 1 - integers; 2 - xml; 3 - json
            "translit": 1 if translit else 0,  # If 1 - transliting message
            "charset": "utf-8",  # Message charset: "windows-1251"|"utf-8"|"koi8-r"
            "cost": 3,  # Message cost in response: 0 - msg; 1 - cost; 2 - msg+cost, 3 - msg+cost+balance
        }

        self._check_account()

    def _get_link(self, **kwargs):
        """Returns get link"""
        params = self._params.copy()
        params.update(kwargs)
        url = self._BASE_URL.format(params=urllib.urlencode(params))

        return url

    def _request_callback(self, code, result, error):
        """Callback for async_get"""
        if code != 200:
            raise SMSCSenderError("RequestError [{}]: {}".format(code, error))
        else:
            try:
                data = json.loads(result)
            except ValueError:
                data = {"error_code": 0, "error": "JSON loads error: {}".format(result)}

            error_code = data.get("error_code")
            if error_code is not None:
                error = self._ERROR_CODES.get(error_code)
                if not error:
                    error = data.get("error", "Unknown error")
                raise SMSCSenderError(
                    "ResponseError [{}]: {}".format(error_code, error)
                )

    def _check_account(self):
        """Send test request to smsc server"""
        url = self._get_link(cost=1, mes=urllib.quote("Hello world!"))
        self._host_api.async_get(url, self._request_callback)

    def text(self, text):
        """Отправка текстового сообщения

        Args:
            text (:obj:`str`): Текст сообщения.
        """

        url = self._get_link(mes=text)

        self._host_api.async_get(url, self._request_callback)


class FtpUploadTracker:
    """Upload progress class"""

    size_written = 0.0
    last_shown_percent = 0

    def __init__(self, file_path, callback, host_api=host):
        self._host_api = host_api
        self.total_size = os.path.getsize(BaseUtils.win_encode_path(file_path))
        self.file_path = file_path
        self.callback = callback

    # noinspection PyUnusedLocal
    def handle(self, block):
        """Handler for storbinary

        See Also:
            https://docs.python.org/2/library/ftplib.html#ftplib.FTP.storbinary
        """
        self.size_written += 1024.0
        percent_complete = round((self.size_written / self.total_size) * 100)

        if self.last_shown_percent != percent_complete:
            self.last_shown_percent = percent_complete
            self._host_api.timeout(
                100, lambda: self.callback(self.file_path, int(percent_complete), "")
            )


class FTPSenderError(SenderError):
    """Raises with FTPSender errors"""

    pass


class FTPSender(Sender):
    """Класс для отправки файлов на ftp сервер

    При инициализации проверят подключение к ftp серверу. Файлы отправляет
    по очереди. Максимальный размер очереди можно изменить. Во время
    выполнения передает текущий прогресс отправки файла в callback функцию.

    Note:
        Помимо прогресса в функцию callback может вернуться код ошибки.
            - -1 Файл не существует.
            - -2 Ошибка отправки на ftp, файл будет повторно отправлен.
            - -3 Неизвестная ошибка.


    Args:
        host (:obj:`str`): Адрес ftp сервера.
        port (:obj:`int`, optional): Порт ftp сервера. По умолчанию :obj:`port=21`
        user (:obj:`str`, optional): Имя пользователя. По умолчанию :obj:`"anonymous"`
        passwd (:obj:`str`, optional): Пароль пользователя. По умолчанию :obj:`passwd=""`
        work_dir (:obj:`str`, optional): Директория на сервре для сохранения файлов.
            По умолчанию :obj:`None`
        callback (:obj:`function`, optional): Callable function. По умолчанию :obj:`None`
        queue_maxlen (:obj:`int`, optional): Максимальная длина очереди на отправку.
            По умолчанию :obj:`queue_maxlen=1000`

    Examples:
        >>> # noinspection PyUnresolvedReferences
        >>> def callback(file_path, progress, error):
        >>>     # Пример callback функции, которая отображает
        >>>     # текущий прогресс в счетчике запуска скрипта
        >>>     # Args:
        >>>     #   file_path (str): Путь до файла
        >>>     #   progress (int): Текущий прогресс передачи файла, %
        >>>     #   error (str | Exception): Ошибка при отправке файла, если есть
        >>>     host.stats()["run_count"] = progress
        >>>     if error:
        >>>         host.error(error)
        >>>
        >>>     if progress == 100:
        >>>         host.timeout(3000, lambda: os.remove(BaseUtils.win_encode_path(file_path)))
        >>>
        >>> sender = FTPSender("172.20.0.10", 21, "trassir", "12345", work_dir="/test_dir/", callback=callback)
        >>> sender.files(r"D:\Shots\export_video.avi")
    """

    def __init__(
        self,
        host,
        port=21,
        user="anonymous",
        passwd="",
        work_dir=None,
        callback=None,
        queue_maxlen=1000,
    ):
        super(FTPSender, self).__init__()
        self._host = host
        self._port = port
        self._user = user
        self._passwd = passwd
        self._work_dir = work_dir

        self.queue = deque(maxlen=queue_maxlen)

        self._ftp = None

        if callback is None:
            callback = BaseUtils.do_nothing

        self.callback = callback

        self._work_now = False

        self._check_connection()

    def _check_connection(self):
        """Check if it possible to connect"""
        try:
            ftp = ftplib.FTP()
            ftp.connect(self._host, self._port, timeout=10)
            ftp.login(self._user, self._passwd)
        except ftplib.all_errors as err:
            raise FTPSenderError(err)
        if self._work_dir:
            try:
                ftp.cwd(self._work_dir)
            except ftplib.error_perm:
                ftp.mkd(self._work_dir)
                ftp.cwd(self._work_dir)

        ftp.quit()

    def _get_connection(self):
        """Connecting to ftp

        Returns:
            ftplib.FTP: Ftp object
        """
        try:
            ftp = ftplib.FTP()
            ftp.connect(self._host, self._port, timeout=10)
            ftp.login(self._user, self._passwd)
            if self._work_dir:
                try:
                    ftp.cwd(self._work_dir)
                except ftplib.error_perm:
                    ftp.mkd(self._work_dir)
                    ftp.cwd(self._work_dir)
            ftp.encoding = "utf-8"
            return ftp
        except ftplib.all_errors:
            return

    def _close_connection(self):
        """Close ftp connection"""
        try:
            if self._ftp is not None:
                self._ftp.close()
        finally:
            self._ftp = None

    def _send_file(self, file_path, work_dir=None):
        """Storbinary file with self.ftp

        Args:
            file_path (str): Full file path
            work_dir (str): Work dir on ftp
        """
        if work_dir is not None:
            if self._work_dir:
                work_dir = os.path.normpath("{}/{}".format(self._work_dir, work_dir))
            try:
                self._ftp.cwd(work_dir)
            except ftplib.error_perm:
                self._ftp.mkd(work_dir)
                self._ftp.cwd(work_dir)

        file_name = os.path.basename(file_path)
        upload_tracker = FtpUploadTracker(file_path, self.callback)
        with open(BaseUtils.win_encode_path(file_path), "rb") as opened_file:
            self._ftp.storbinary(
                "STOR " + file_name, opened_file, 1024, upload_tracker.handle
            )

    @BaseUtils.run_as_thread_v2()
    def _sender(self):
        """Send files in queue"""
        if self.queue:
            if self._ftp is None:
                self._ftp = self._get_connection()

            if self._ftp:
                work_dir = None
                file_path = self.queue.popleft()

                if isinstance(file_path, tuple):
                    file_path, work_dir = file_path

                if BaseUtils.is_file_exists(BaseUtils.win_encode_path(file_path)):
                    try:
                        self._send_file(file_path, work_dir)

                    except ftplib.all_errors as err:
                        self._host_api.timeout(
                            100, lambda: self.callback(file_path, -2, error=err)
                        )
                        self.queue.append(file_path)
                        self._close_connection()

                    except Exception as err:
                        self._host_api.timeout(
                            100, lambda: self.callback(file_path, -3, error=err)
                        )

                else:
                    self._host_api.timeout(
                        100,
                        lambda: self.callback(file_path, -1, error="File not found"),
                    )

            self._host_api.timeout(500, self._sender)
        else:
            self._work_now = False
            self._close_connection()

    def files(self, file_paths, *args):
        """Отправка файлов

        Note:
            Можно указать отдельный путь на ftp сервере для каждого файла.
            Для этого список файлов на отправку должен быть приведен к виду
            ``[(shot_path, ftp_path), ...]`` При этом так же будет учитываться
            глобальная папка :obj:`work_dir` заданная при инициализации класса.

        Args:
            file_paths (:obj:`str` | :obj:`list`): Путь до файла или список
                файлов для отправки
        """
        if not isinstance(file_paths, list):
            file_paths = [file_paths]

        self.queue.extend(file_paths)
        if not self._work_now:
            self._work_now = True
            self._sender()
