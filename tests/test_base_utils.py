# -*- coding: utf-8 -*-
import os
import sys
import time
import json
import pytest
import threading

from datetime import datetime

CWD = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CWD)

from trassir_script_framework import BaseUtils


class TestBaseUtils:

        shot_path = os.path.join(CWD, r"files/Скриншот.jpg")
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
            536871009: ["LPR_EXT_DB_ERROR", "LPR_UP", "LPR_CORRECTED"]
        }

        def test_do_nothing(self):
            assert BaseUtils.do_nothing() is True
            assert BaseUtils.do_nothing("123", "test", 12345) is True
            assert BaseUtils.do_nothing("123", test="test") is True

        def test_run_as_thread_v2(self):

            @BaseUtils.run_as_thread_v2()
            def thread_daemon_func():
                time.sleep(.1)

            @BaseUtils.run_as_thread_v2(daemon=False)
            def thread_not_daemon_func():
                time.sleep(.1)

            t_daemon = thread_daemon_func()
            t_not_daemon = thread_not_daemon_func()

            assert isinstance(t_daemon, threading.Thread)
            assert isinstance(t_not_daemon, threading.Thread)

            assert t_daemon.daemon is True
            assert t_not_daemon.daemon is False

        def test_win_encode_path(self):
            file_path = self.shot_path
            if os.name == "nt":
                assert BaseUtils.win_encode_path(file_path) == file_path.decode("utf8").encode("cp1251")
            else:
                assert file_path == file_path

        def test_is_file_exists(self):
            assert os.path.isfile(BaseUtils.win_encode_path(self.shot_path)) is True
            assert os.path.isfile("Unexisting_file.jpg") is False

        def test_is_folder_exists(self):
            BaseUtils.is_folder_exists(CWD)

            with pytest.raises(IOError):
                BaseUtils.is_folder_exists(CWD + "/test/te")

        def test_is_template_exists(self):
            assert BaseUtils.is_template_exists("name") is True
            assert BaseUtils.is_template_exists("name2") is False

        def test_cat(self):
            with pytest.raises(TypeError) as exc_info:
                assert BaseUtils.cat("test.avi")
            exception_msg = exc_info.value.args[0]
            assert exception_msg == "Bad file extension: .avi. To ignore this: set check_ext=False"

        def test_to_json(self):
            dt_now = datetime.now()
            with pytest.raises(TypeError):
                json.dumps(dt_now)

            assert '"%s"' % dt_now.isoformat() == BaseUtils.to_json(dt_now)

        def test_lpr_flags_decode(self):
            for flags_int, flags_decoded in self.lpr_flags.iteritems():
                assert BaseUtils.lpr_flags_decode(flags_int) == flags_decoded

        def test_get_object_name_by_guid(self):
            assert BaseUtils.get_object_name_by_guid("guid") == "name"

        def test_get_server_guid(self):
            assert BaseUtils.get_server_guid() == "guid"

        def test_get_script_name(self):
            assert BaseUtils.get_script_name() == "script_name"

        def test_get_screenshot_folder(self):
            assert BaseUtils.get_screenshot_folder() == os.getcwd()
