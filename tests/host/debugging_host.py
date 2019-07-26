import os
from time import sleep

from .settings_dir import FakeSettingsDir
from .utils import generate_random_guid


class DebuggingHost:
    # See host.sip in tech1script for total list of available options

    def __init__(self, server_guid=None):
        self._SCRIPT_PATH = "."
        self._LOCAL_SERVER_SETTINGS = FakeSettingsDir(guid=server_guid, name="FakeLocalServer", path="", parent=None)

        self._IS_MUTED = False
        self._IS_TIMEOUT_ENABLED = False
        self._USE_ASK_RESULT = None
        self._USE_QUESTION_CALLBACK_NUMBER = 0

    # === SETTINGS & OBJECTS ===

    def settings(self, path):
        # TODO: Add here more typical options
        if path == "":
            return self.local_server__dbg
        elif path == "system_wide_options":
            return {
                "screenshots_folder": self.script_path
            }
        elif path.startswith('scripts/'):
            return {
                'name': path[8:]
            }
        elif path.startswith('templates'):
            templates_dir = FakeSettingsDir()
            templates_dir._children__dbg = [FakeSettingsDir(name="name")]
            return templates_dir
        else:
            return None

    def object(self, object_id):
        class StubObject():
            def __init__(self, object_id):
                self.name = "name"
                self.guid = str(object_id)
        return StubObject(object_id)

    def object_add(self, object):
        pass

    # === SIMPLE MANIPULATING DEBUG FUNCITONS ===
    def mute_messages__dbg(self, is_muted):
        self._is_muted = bool(is_muted)

    def enable_real_timeout__dbg(self, is_enabled):
        self._is_timeout_enabled = bool(is_enabled)

    def set_ask_result__dbg(self, expected_result):
        if expected_result is not None and not isinstance(expected_result, basestring):
            raise ValueError("Expected result should be None or string")
        self._use_ask_result = expected_result

    def set_question_callback_number__dbg(self, expected_callback_number):
        if not isinstance(expected_callback_number, int):
            raise ValueError("Expected callback number should be ingeger")
        self._use_question_callback_number = expected_callback_number

    # === OUTPUT ===
    _default_timeout = 5000

    def _fancy_print(self, tag, text, timeout=_default_timeout):
        if not self._is_muted:
            if timeout != DebuggingHost._default_timeout:
                print "{} (t/o {}): {}".format(tag, timeout, text)
            else:
                print "{}: {}".format(tag, text)

    def message(self, text, timeout=_default_timeout):
        self._fancy_print("MESSAGE", text, timeout)

    def alert(self, text, timeout=_default_timeout):
        self._fancy_print("ALERT", text, timeout)

    def error(self, text, timeout=_default_timeout):
        self._fancy_print("ERROR", text, timeout)

    def log_message(self, text):
        self._fancy_print("LOG_MESSAGE", text, DebuggingHost._default_timeout)

    def send_mail_from_account(self, account, receivers, subject, text, files):
        self._fancy_print("MAIL", subject + ": " + text, DebuggingHost._default_timeout)

    def text_set(self, channel_guid, text, *args):
        self._fancy_print("TEXT_SET", text, DebuggingHost._default_timeout)

    def figure_set(self, channel_guid, figures_list):
        return

    def text_remove(self, channel_guid):
        return

    def figure_remove(self, channel_guid):
        return

    # === SCREENSHOTS ===
    def screenshot_v2(self, channel_name, screenshot_name, screenshot_path, timestamp):
        fake_name = channel_name + "_" + screenshot_name + str(timestamp) + ".png"
        with open(os.path.join(screenshot_path, fake_name), "w") as handle:
            handle.write("1337")

    def screenshot_v2_figures(self, channel_name, screenshot_name, screenshot_path, timestamp):
        self.screenshot_v2(channel_name, screenshot_name, screenshot_path, timestamp)

    # === TIMEOUT ===
    def timeout(self, milliseconds, callback):
        if self._is_timeout_enabled:
            sleep(milliseconds / 1000)
        callback()

    # === USER INTERACTION ===
    def ask(self, text, ok_callback, cancel_callback, timeout=None, default_value=None):
        # Use function set_ask_result__dbg(..) to manipulate results of ask(...)
        # or mock this function entirely
        if timeout is None and default_value is not None:
            raise ValueError("Must specify timeout with default value")
        _ = text
        if self._use_ask_result:
            ok_callback(self._use_ask_result)
        else:
            cancel_callback()

    def question(self, text, *args):
        # Use function set_question_callback_number__dbg(..) to manipulate results of question(...)
        # or mock this function entirely
        _ = text
        if len(args) < 2:
            raise ValueError("At least one option should be specified")
        if len(args) % 2:
            args = args[:-1]  # ignore timeout arg
        try:
            callback = args[self._use_question_callback_number * 2]  # ignore button text args
        except IndexError:
            raise ValueError("Tried to use callback {} but there was only {} callbacks provided".format(
                self._use_question_callback_number, len(args) // 2
            ))
        if callable(callback):
            callback()
        else:
            raise ValueError(
                "Tried to use callback {} but it was not callable".format(self._use_question_callback_number))

    # === ARCHIVE ===
    def archive_remote_export(self, server_guid, channel_guid, filename, start_ts, end_ts, options, callback):
        callback()

    def archive_export(self, server_guid, channel_guid, filename, start_ts, end_ts, options, callback):
        callback()

    def archive_export_travi(self, channels_config, filename, start_ts, end_ts, options, callback):
        callback()

    def archive_export_tasks_get(self):
        return []

    def archive_export_task_cancel(self, task_id, timeout_sec, callback_success, callback_error):
        callback_success()

    def get_archive_export_status(self, task_id):
        # ARCHIVE_EXPORT_STATUS_SCRIPT_TASK_NOT_FOUND = 0,
        # ARCHIVE_EXPORT_STATUS_SCRIPT_IN_PROGRESS = 1,
        # ARCHIVE_EXPORT_STATUS_SCRIPT_FAILED = 2,
        # ARCHIVE_EXPORT_STATUS_SCRIPT_COMPLETED = 3
        return 0

    def get_archive_pos(self):
        return 0

    def open_archive(self, channel, mode):
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
    def visible_templates(self, monitor_num):
        return ""

    def all_visible_templates(self, monitor_num):
        return []

    # === PATHS ===
    def path_working(self):
        # On stationary computer returns path to tech1 folder
        return "."

    def path_arbitrary_data(self):
        # On stationary computer returns path to tech1 folder
        return "."

    # === LPR ===
    def lpr_radar_speed_store(self, channel_guid, lane, speed):
        return

    # === POS ===
    def pos_fraud(self, event, fraud_text):
        return

    def pos_import_detector(self, setup):
        return

    def pos_incident_create(self, terminal_id, incident_type_name, cashier_name):
        return

    def generate_pos_report(self, report_type, time_begin, time_end):
        return

    # === ALARMS ===
    def fire_alarm(self, alarm):
        pass

    # === HTTP ===
    def add_view_http_handler(self, url, settings_path, activation_func):
        # TODO: this deserves non-mock default implementation
        class FakeRpcHTTPHandler:
            def __init__(self):
                pass

        return FakeRpcHTTPHandler()

    def add_setup_http_handler(self, url, settings_path, activation_func):
        # TODO: this deserves non-mock default implementation
        class FakeRpcHTTPHandler:
            def __init__(self):
                pass

        return FakeRpcHTTPHandler()

    def add_function_call_http_handler(self, url, settings_path, activation_func):
        # TODO: this deserves non-mock default implementation
        class FakeHTTPRequestCallHandler:
            def __init__(self):
                pass

        return FakeHTTPRequestCallHandler()

    def add_protected_function_call_http_handler(self, url, settings_path, activation_func):
        # TODO: this deserves non-mock default implementation
        class FakeHTTPRequestCallHandler:
            def __init__(self):
                pass

        return FakeHTTPRequestCallHandler()

    def async_post(self, url, data, callback, settings_map, headers_map):
        return

    def async_get(self, url, callback, settings_map, headers_map):
        return

    # === OTHER ===
    def exec_encoded(self, encoded_script):
        return encoded_script

    def objects_list(self, filter):
        # TODO: this deserves non-mock default implementation
        return []

    def wanted_objects(self, id):
        # TODO: this deserves non-mock default implementation
        return ""

    def license_id(self):
        return ""

    def apply_channel_views_limit(self, channel_guid, limit):
        return

    def generate_thumbnail(self, data, columns, rows, extension):
        class FakeGenerateThumbnail:
            def __init__(self):
                pass

            def ready(self):
                return True

            def image(self):
                return data

        return FakeGenerateThumbnail()

    def encrypt_json(self, json_string):
        return json_string

    def decrypt_json(self, json_string):
        return json_string

    def stats(self):
        # TODO(p.sadovnikov): Write more robust default stub
        script_dir = FakeSettingsDir(name="script_name")
        stats_dir = FakeSettingsDir(parent=script_dir)
        return stats_dir

    def tr(self, language):
        return

    def random_guid(self):
        return generate_random_guid()

    def register_finalizer(self, func):
        pass

    # === SUBSCRIBE FUNCTIONS ===

    # Added for completeness sake because they may be used for example in HTTP handlers
    # You should mock these functions when checking their usage inside detector class
    # Do not test their usage outside detectors

    def activate_on_events(self, *args, **kwargs):
        pass

    def activate_on_pos_events(self, *args, **kwargs):
        pass

    def activate_on_pos_incidents(self, *args, **kwargs):
        pass

    def activate_on_lpr_events(self, *args, **kwargs):
        pass

    def activate_on_people_detection_events(self, *args, **kwargs):
        pass

    def activate_on_deep_detection_events(self, *args, **kwargs):
        pass  # legacy

    def activate_on_aruco_detection_events(self, *args, **kwargs):
        pass

    def activate_on_ptz_events(self, *args, **kwargs):
        pass

    def activate_on_context_menu(self, *args, **kwargs):
        pass

    def activate_on_shortcut(self, *args, **kwargs):
        pass

    def activate_on_gui_event(self, *args, **kwargs):
        pass

    def activate_on_focus_change(self, *args, **kwargs):
        pass

    def activate_on_template_switch(self, *args, **kwargs):
        pass

    def activate_on_layout_change(self, *args, **kwargs):
        pass

    # === MISC ===

    class TrassirObject:
        def __init__(self, object_type):
            self._object_type = object_type

        def set_guid(self, guid):
            self._guid = guid

        def set_name(self, script_name):
            self._script_name = script_name

        def fire_event(self, *args):
            pass


hh = DebuggingHost()
