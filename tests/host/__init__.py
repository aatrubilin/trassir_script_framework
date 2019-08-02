# -*- coding: utf-8 -*-

import os
from time import sleep

from sqlalchemy import create_engine

from .settings_dir import FakeSettingsDir
from .trassir_object import (
    FakeTrassirObject,
    FakeTrassirChannel,
    FakeTrassirIPDevice,
    FakeTrassirTemplate,
    FakeTrassirOperatorGUI,
)
from .utils import generate_random_guid
from . import __doc__ as docstr


_SCRIPT_PATH = "."
_LOCAL_SERVER_SETTINGS = FakeSettingsDir(
    guid="FHqSOje4", name="DemoServer", path="", parent=None
)
_LOCAL_OBJECTS_LIST = [
    ("DemoChannel", "YdxkePGP", "Channel", "FHqSOje4C"),
    ("Face Recognizer", "FHqSOje4FR", "Face Recognizer", "FHqSOje4"),
    ("IP-устройства", "FHqSOje4I", "Folder", "FHqSOje4"),
    ("SIP", "FHqSOje4P", "Folder", "FHqSOje4"),
    ("Каналы", "FHqSOje4C", "Folder", "FHqSOje4"),
    ("Шаблоны", "FHqSOje4T", "FolderH", "FHqSOje4"),
    ("DemoDevice", "iGt0xqub", "IP Device", "FHqSOje4I"),
    (
        "Интерфейс оператора DemoServer",
        "operatorgui_FHqSOje4",
        "OperatorGUI",
        "FHqSOje4",
    ),
    ("Unnamed Schedule", "cDT0zG3N", "Schedule", "FHqSOje4"),
    ("DemoServer", "FHqSOje4", "Server", "FHqSOje4"),
    ("DemoTemplate", "JbNSVnx0", "Template", "FHqSOje4T"),
]
_LOCAL_OBJECTS_GUID_DICT = {obj[1]: obj for obj in _LOCAL_OBJECTS_LIST}
_LOCAL_OBJECTS_NAME_DICT = {obj[0]: obj for obj in _LOCAL_OBJECTS_LIST}


_IS_MUTED = False
_IS_TIMEOUT_ENABLED = False
_USE_ASK_RESULT = None
_USE_QUESTION_CALLBACK_NUMBER = 0


# === CONSTANTS ===

EXTHTTP_HANDLER_GET = 1
EXTHTTP_HANDLER_NEED_SDK_ENABLE = 128
EXTHTTP_HANDLER_POST = 2
EXTHTTP_HANDLER_SESSION_OPTIONAL = 16
EXTHTTP_HANDLER_SESSION_SDK = 32
EXTHTTP_HANDLER_SESSION_USER = 64
EXTHTTP_HANDLER_STATIC = 12
EXTHTTP_HANDLER_STATIC_DIR = 8
EXTHTTP_HANDLER_STATIC_FILE = 4
EXTHTTP_METHOD_GET = 0
EXTHTTP_METHOD_POST = 1
EXTHTTP_SESSION_NONE = 0
EXTHTTP_SESSION_SDK = 1
EXTHTTP_SESSION_USER = 2
LPR_BLACKLIST = 4
LPR_CORRECTED = 64
LPR_DOWN = 2
LPR_EXT_DB_ERROR = 32
LPR_INFO = 16
LPR_UP = 1
LPR_WHITELIST = 8
RIGHTS_ALTER_RIGHTS = 64
RIGHTS_ANY = 8396799
RIGHTS_BOOKMARK = 32
RIGHTS_CLOUD_VIEW = 16
RIGHTS_EVERYTHING = 8396799
RIGHTS_EXPORT = 256
RIGHTS_HEALTH = 2048
RIGHTS_INCIDENTS = 4096
RIGHTS_MASK = 7775
RIGHTS_MODIFY = 4
RIGHTS_NONE = 0
RIGHTS_PASSWORD = 8388608
RIGHTS_PTZ = 512
RIGHTS_ROOT = 128
RIGHTS_SETUP = 8
RIGHTS_SOUND = 1024
RIGHTS_USERADMIN = 8063
RIGHTS_VIEW = 1
RIGHTS_VIEWARCHIVE = 2


# === SETTINGS & OBJECTS ===


def settings(path):
    # TODO: Add here more typical options
    if path == "":
        return _LOCAL_SERVER_SETTINGS
    elif path == "system_wide_options":
        return {"screenshots_folder": _SCRIPT_PATH}
    elif path.startswith("scripts/"):
        return {"name": path[8:]}
    elif path.startswith("templates"):
        templates_dir = FakeSettingsDir()
        templates_dir._children__dbg = [FakeSettingsDir(name="name")]
        return templates_dir
    else:
        return None


def object(object_id):
    obj = _LOCAL_OBJECTS_GUID_DICT.get(object_id)
    if obj is None:
        obj = _LOCAL_OBJECTS_NAME_DICT.get(object_id)

    if obj is None:
        obj = FakeTrassirObject("name")
        obj.guid = object_id

    else:
        name_, guid_, type_, _ = obj

        if type_ == "Channel":
            obj = FakeTrassirChannel(name_)

        elif type_ == "IP Device":
            obj = FakeTrassirIPDevice(name_)

        elif type_ == "Template":
            obj = FakeTrassirTemplate(name_)

        elif type_ == "OperatorGUI":
            obj = FakeTrassirOperatorGUI(name_)

        else:
            obj = FakeTrassirObject(name_)
            obj.fake_obj = False

        obj.guid = guid_
    return obj


def object_add(object):
    pass


# === OUTPUT ===
_DEFAULT_TIMEOUT = 5000


def _fancy_print(tag, text, timeout=_DEFAULT_TIMEOUT):
    if not _IS_MUTED:
        if timeout != _DEFAULT_TIMEOUT:
            print("{} (t/o {}): {}".format(tag, timeout, text))
        else:
            print("{}: {}".format(tag, text))


def message(text, timeout=_DEFAULT_TIMEOUT):
    _fancy_print("MESSAGE", text, timeout)


def alert(text, timeout=_DEFAULT_TIMEOUT):
    _fancy_print("ALERT", text, timeout)


def error(text, timeout=_DEFAULT_TIMEOUT):
    _fancy_print("ERROR", text, timeout)


def log_message(text):
    _fancy_print("LOG_MESSAGE", text, _DEFAULT_TIMEOUT)


def send_mail_from_account(account, receivers, subject, text, files):
    _fancy_print("MAIL", subject + ": " + text, _DEFAULT_TIMEOUT)


def text_set(channel_guid, text, *args):
    _fancy_print("TEXT_SET", text, _DEFAULT_TIMEOUT)


def figure_set(channel_guid, figures_list):
    return


def text_remove(channel_guid):
    return


def figure_remove(channel_guid):
    return


# === SCREENSHOTS ===
def screenshot_v2(channel_name, screenshot_name, screenshot_path, timestamp):
    fake_name = channel_name + "_" + screenshot_name + str(timestamp) + ".png"
    with open(os.path.join(screenshot_path, fake_name), "w") as handle:
        handle.write("1337")


def screenshot_v2_figures(channel_name, screenshot_name, screenshot_path, timestamp):
    screenshot_v2(channel_name, screenshot_name, screenshot_path, timestamp)


# === TIMEOUT ===
def timeout(milliseconds, callback):
    if _IS_TIMEOUT_ENABLED:
        sleep(milliseconds / 1000)
    callback()


# === USER INTERACTION ===
def ask(text, ok_callback, cancel_callback, timeout=None, default_value=None):
    # Use function set_ask_result__dbg(..) to manipulate results of ask(...)
    # or mock this function entirely
    if timeout is None and default_value is not None:
        raise ValueError("Must specify timeout with default value")
    _ = text
    if _USE_ASK_RESULT:
        ok_callback(_USE_ASK_RESULT)
    else:
        cancel_callback()


def question(text, *args):
    # Use function set_question_callback_number__dbg(..) to manipulate results of question(...)
    # or mock this function entirely
    _ = text
    if len(args) < 2:
        raise ValueError("At least one option should be specified")
    if len(args) % 2:
        args = args[:-1]  # ignore timeout arg
    try:
        callback = args[_USE_QUESTION_CALLBACK_NUMBER * 2]  # ignore button text args
    except IndexError:
        raise ValueError(
            "Tried to use callback {} but there was only {} callbacks provided".format(
                _USE_QUESTION_CALLBACK_NUMBER, len(args) // 2
            )
        )
    if callable(callback):
        callback()
    else:
        raise ValueError(
            "Tried to use callback {} but it was not callable".format(
                _USE_QUESTION_CALLBACK_NUMBER
            )
        )


# === ARCHIVE ===
def archive_remote_export(
    server_guid, channel_guid, filename, start_ts, end_ts, options, callback
):
    callback()


def archive_export(
    server_guid, channel_guid, filename, start_ts, end_ts, options, callback
):
    callback()


def archive_export_travi(
    channels_config, filename, start_ts, end_ts, options, callback
):
    callback()


def archive_export_tasks_get():
    return []


def archive_export_task_cancel(task_id, timeout_sec, callback_success, callback_error):
    callback_success()


def get_archive_export_status(task_id):
    # ARCHIVE_EXPORT_STATUS_SCRIPT_TASK_NOT_FOUND = 0,
    # ARCHIVE_EXPORT_STATUS_SCRIPT_IN_PROGRESS = 1,
    # ARCHIVE_EXPORT_STATUS_SCRIPT_FAILED = 2,
    # ARCHIVE_EXPORT_STATUS_SCRIPT_COMPLETED = 3
    return 0


def get_archive_pos():
    return 0


def open_archive(channel, mode):
    class FakeArchivePlayer:
        def __init__(self):
            pass

        def ready(self):
            pass

        def archive_status(self):
            pass

    return FakeArchivePlayer()


def abackend_stats(self):
    return [{"depth": 0, "gb": 0.0, "real_depth": 0.0}]


# === TEMPLATES ===
def visible_templates(monitor_num):
    return ""


def all_visible_templates(monitor_num):
    return []


# === PATHS ===
def path_working():
    # On stationary computer returns path to tech1 folder
    return "."


def path_arbitrary_data():
    # On stationary computer returns path to tech1 folder
    return "."


# === LPR ===
def lpr_radar_speed_store(channel_guid, lane, speed):
    return


# === POS ===
def pos_fraud(event, fraud_text):
    return


def pos_import_detector(setup):
    return


def pos_incident_create(terminal_id, incident_type_name, cashier_name):
    return


def generate_pos_report(report_type, time_begin, time_end):
    return


# === ALARMS ===
def fire_alarm(alarm):
    pass


# === HTTP ===
def add_view_http_handler(url, settings_path, activation_func):
    # TODO: this deserves non-mock default implementation
    class FakeRpcHTTPHandler:
        def __init__(self):
            pass

    return FakeRpcHTTPHandler()


def add_setup_http_handler(url, settings_path, activation_func):
    # TODO: this deserves non-mock default implementation
    class FakeRpcHTTPHandler:
        def __init__(self):
            pass

    return FakeRpcHTTPHandler()


def add_function_call_http_handler(url, settings_path, activation_func):
    # TODO: this deserves non-mock default implementation
    class FakeHTTPRequestCallHandler:
        def __init__(self):
            pass

    return FakeHTTPRequestCallHandler()


def add_protected_function_call_http_handler(url, settings_path, activation_func):
    # TODO: this deserves non-mock default implementation
    class FakeHTTPRequestCallHandler:
        def __init__(self):
            pass

    return FakeHTTPRequestCallHandler()


def async_post(url, data, callback, settings_map=None, headers_map=None):
    return


def async_get(url, callback, settings_map=None, headers_map=None):
    return


# === OTHER ===
def exec_encoded(encoded_script):
    return encoded_script


def objects_list(filter):
    if filter:
        return [obj for obj in _LOCAL_OBJECTS_LIST if obj[2] == filter]
    return _LOCAL_OBJECTS_LIST


def wanted_objects(id):
    # TODO: this deserves non-mock default implementation
    return ""


def license_id():
    return ""


def apply_channel_views_limit(channel_guid, limit):
    return


def generate_thumbnail(data, columns, rows, extension):
    class FakeGenerateThumbnail:
        def __init__(self):
            pass

        def ready(self):
            return True

        def image(self):
            return data

    return FakeGenerateThumbnail()


def encrypt_json(json_string):
    return json_string


def decrypt_json(json_string):
    return json_string


def stats():
    # TODO(p.sadovnikov): Write more robust default stub
    script_dir = FakeSettingsDir(name="DemoScript")
    stats_dir = FakeSettingsDir(parent=script_dir)
    return stats_dir


def tr(language):
    return


def random_guid():
    return generate_random_guid()


def register_finalizer(func):
    pass


# === SUBSCRIBE FUNCTIONS ===

# Added for completeness sake because they may be used for example in HTTP handlers
# You should mock these functions when checking their usage inside detector class
# Do not test their usage outside detectors


def activate_on_events(*args, **kwargs):
    pass


def activate_on_pos_events(*args, **kwargs):
    pass


def activate_on_pos_incidents(*args, **kwargs):
    pass


def activate_on_lpr_events(*args, **kwargs):
    pass


def activate_on_people_detection_events(*args, **kwargs):
    pass


def activate_on_deep_detection_events(*args, **kwargs):
    pass  # legacy


def activate_on_aruco_detection_events(*args, **kwargs):
    pass


def activate_on_ptz_events(*args, **kwargs):
    pass


def activate_on_context_menu(*args, **kwargs):
    pass


def activate_on_shortcut(*args, **kwargs):
    pass


def activate_on_gui_event(*args, **kwargs):
    pass


def activate_on_focus_change(*args, **kwargs):
    pass


def activate_on_template_switch(*args, **kwargs):
    pass


def activate_on_layout_change(*args, **kwargs):
    pass


# === FACE RECOGNITION ===


def service_persons_get(*args):
    if len(args) < 5:
        raise TypeError("service_persons_get(): not enough arguments")
    elif len(args) > 5:
        raise TypeError("service_persons_get(): too many arguments")
    else:
        if not isinstance(args[0], list):
            raise SystemError("bad argument to internal function")
        else:
            for guid in args[0]:
                if not isinstance(guid, (str, unicode)):
                    raise TypeError(
                        "expected string or Unicode object, {} found".format(
                            type(guid).__name__
                        )
                    )


def service_fr_last_track_with_person_get(
    channel_guid, person_guid, unknown_arg, timeout
):

    res = {
        "comment": "",
        "facial_emotion": "",
        "ts_disappeared_sec": 1563526690,
        "channel_guid": "jiUCatIw",
        "matches": [
            {"score": 9969, "person_guid": "dRSCJ0Mv_pV4ggECb"},
            {"score": 9970, "person_guid": "KrWWZnmj_pV4ggECb"},
        ],
        "gender": "GENDER_MALE",
        "age": 38,
        "headwear": "",
        "track_guid": "yJeGTfOe",
        "hair_color": "",
        "ts_appeared_sec": 1563526688,
        "facial_hair": "",
        "ts_best_view_sec": 1563526688,
        "race": "RACE_CAUCASIAN",
        "face_confidence": 73,
        "image": "<base64image>",
        "glasses": "GLASSES_NONE",
    }
    return res


# === MISC ===


def get_database_connection():
    return create_engine("sqlite://")


# === MISC ===


class TrassirObject:
    def __init__(self, object_type):
        self._object_type = object_type

    def set_guid(self, guid):
        self._guid = guid

    def set_name(self, script_name):
        self._script_name = script_name

    def set_initial_state(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def set_folder(self, folder):
        self._folder = folder

    def change_folder(self, folder):
        self._folder = folder

    def set_parent(self, parent):
        self._parent = parent

    def fire_event(self, type_, p1, p2, p3):
        # "Script: %1", message, channel, data
        pass


class ScriptHost:
    SE_Settings = FakeSettingsDir
    SE_Object = FakeTrassirObject
