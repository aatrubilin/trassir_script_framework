# -*- coding: utf-8 -*-

import os
import sys
import time
import urllib2
import threading

from datetime import datetime
from unittest import TestCase

cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(cwd)
if os.name == "nt":
    cwd = cwd.decode("cp1251").encode("utf8")

from trassir_script_framework import BaseUtils


class TestBaseUtils(TestCase):
    shot_path = os.path.join(cwd, r"files/Скриншот.jpg")
    dt = datetime.strptime("2019-07-22T08:45:48.954000", "%Y-%m-%dT%H:%M:%S.%f")
    ts = 1563759948954000

    lpr_flags = {
        1: ["LPR_UP"],
        2: ["LPR_DOWN"],
        33: ["LPR_EXT_DB_ERROR", "LPR_UP"],
        34: ["LPR_DOWN", "LPR_EXT_DB_ERROR"],
        536870913: ["LPR_UP"],
        536870914: ["LPR_DOWN"],
        536870921: ["LPR_UP", "LPR_WHITELIST"],
        536870922: ["LPR_DOWN", "LPR_WHITELIST"],
        536870929: ["LPR_INFO", "LPR_UP"],
        536870930: ["LPR_DOWN", "LPR_INFO"],
        536870945: ["LPR_EXT_DB_ERROR", "LPR_UP"],
        536870946: ["LPR_DOWN", "LPR_EXT_DB_ERROR"],
        536870953: ["LPR_EXT_DB_ERROR", "LPR_UP", "LPR_WHITELIST"],
        536870954: ["LPR_DOWN", "LPR_EXT_DB_ERROR", "LPR_WHITELIST"],
        536870961: ["LPR_EXT_DB_ERROR", "LPR_INFO", "LPR_UP"],
        536870962: ["LPR_DOWN", "LPR_EXT_DB_ERROR", "LPR_INFO"],
        536871009: ["LPR_EXT_DB_ERROR", "LPR_UP", "LPR_CORRECTED"],
    }

    def test_do_nothing(self):
        self.assertIs(BaseUtils.do_nothing(), True)
        self.assertIs(BaseUtils.do_nothing("123", 12345), True)
        self.assertIs(BaseUtils.do_nothing("123", test="test"), True)

    def test_run_as_thread(self):
        @BaseUtils.run_as_thread
        def thread_func():
            time.sleep(0.1)

        t = thread_func()

        self.assertIsInstance(t, threading.Thread)
        self.assertIs(t.daemon, True)

    def test_catch_request_exceptions(self):
        @BaseUtils.catch_request_exceptions
        def catch_http_error(url):
            raise urllib2.HTTPError(url, 400, "Bad Request", None, None)

        self.assertEqual((400, "HTTPError: 400"), catch_http_error("https://dssl.ru"))

        @BaseUtils.catch_request_exceptions
        def catch_url_error(reason):
            raise urllib2.URLError(reason)

        self.assertEqual(
            ("getaddrinfo failed", "URLError: getaddrinfo failed"),
            catch_url_error("getaddrinfo failed"),
        )

    def test_win_encode_path(self):
        file_path = self.shot_path
        print(file_path)
        if os.name == "nt":
            self.assertEqual(file_path.decode("utf8"), BaseUtils.win_encode_path(file_path))
        else:
            self.assertEqual(file_path, file_path)

    def test_is_file_exists(self):
        self.assertEqual(True, os.path.isfile(BaseUtils.win_encode_path(self.shot_path)))
        self.assertEqual(False, os.path.isfile("fake_file.jpeg"))

    def test_is_folder_exists(self):
        self.assertRaises(IOError, BaseUtils.is_folder_exists, cwd)
        BaseUtils.is_folder_exists(BaseUtils.win_encode_path(cwd))

    def test_is_template_exists(self):
        self.assertEqual(True, BaseUtils.is_template_exists("name"))
        self.assertEqual(False, BaseUtils.is_template_exists("fakeName"))

    def test_cat(self):
        self.assertRaises(TypeError, BaseUtils.cat, "test.avi")

    def test_to_json(self):
        dt_now = datetime.now()
        self.assertEqual('"%s"' % dt_now.isoformat(), BaseUtils.to_json(dt_now))

    def test_ts_to_dt(self):
        self.assertEqual(self.dt, BaseUtils.ts_to_dt(self.ts))

    def test_dt_to_ts(self):
        self.assertEqual(self.ts, BaseUtils.dt_to_ts(self.dt))

    def test_lpr_flags_decode(self):
        for flags_int, flags_decoded in self.lpr_flags.iteritems():
            self.assertEqual(flags_decoded, BaseUtils.lpr_flags_decode(flags_int))

    def test_event_type_encode(self):
        self.assertEqual(1745631458, BaseUtils.event_type_encode("Border %1 A-B Crossing"))
        self.assertEqual(1838034845, BaseUtils.event_type_encode("Object Left the Zone"))
        self.assertEqual(-2095846277, BaseUtils.event_type_encode("Fire Detected"))

    def test_event_type_decode(self):
        self.assertEqual("Border %1 A-B Crossing", BaseUtils.event_type_decode(1745631458))
        self.assertEqual("Object Left the Zone", BaseUtils.event_type_decode(1838034845))
        self.assertEqual("Fire Detected", BaseUtils.event_type_decode(-2095846277))

    def test_image_to_base64(self):
        self.assertEqual(True, BaseUtils.image_to_base64(self.shot_path).startswith("/9j/4AAQSkZJRgABAQAA"))

    def test_base64_to_html_img(self):
        base64_image = BaseUtils.image_to_base64(self.shot_path)
        self.assertEqual(True, BaseUtils.base64_to_html_img(base64_image).startswith("""<img src="data:image"""))

    def test_save_pkl(self):
        data = {"key": "value"}
        BaseUtils.save_pkl("tests/data.pkl", data)
        self.assertEqual(True, BaseUtils.is_file_exists("tests/data.pkl"))

    def test_load_pkl(self):
        data = BaseUtils.load_pkl("tests/data.pkl")
        self.assertEqual({"key": "value"}, data)
        self.assertEqual([], BaseUtils.load_pkl("fake_file.pkl", list))

    def test_get_object(self):
        self.assertEqual("DemoDevice", BaseUtils.get_object("iGt0xqub").name)
        self.assertEqual(None, BaseUtils.get_object("fake"))

    def test_get_object_name_by_guid(self):
        self.assertEqual("DemoTemplate", BaseUtils.get_object_name_by_guid("JbNSVnx0"))

    def test_get_full_guid(self):
        self.assertEqual("YdxkePGP_FHqSOje4", BaseUtils.get_full_guid("YdxkePGP"))

    def test_get_operator_gui(self):
        self.assertEqual("Operator Works", BaseUtils.get_operator_gui().state("sleeping"))

    def test_get_server_guid(self):
        self.assertEqual("FHqSOje4", BaseUtils.get_server_guid())

    def test_get_script_name(self):
        self.assertEqual("DemoScript", BaseUtils.get_script_name())

    def test_get_screenshot_folder(self):
        self.assertEqual(".", BaseUtils.get_screenshot_folder())

    # def test_get_logger(self):
    #     self.fail()

    # def test_set_script_name(self):
    #     self.fail()
