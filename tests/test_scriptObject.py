import os
import sys

from unittest import TestCase

cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(cwd)
if os.name == "nt":
    cwd = cwd.decode("cp1251").encode("utf8")

from trassir_script_framework import ScriptObject


class TestScriptObject(TestCase):
    obj = ScriptObject(name="DemoScript", guid="script_guid", parent=None)

    def test_health(self):
        self.obj.health = "Error"
        self.assertEqual("Error", self.obj.health)
        self.obj.health = "OK"
        self.assertEqual("OK", self.obj.health)

        def fail_health():
            self.obj.health = "FAIL"

        self.assertRaises(ValueError, fail_health)

    def test_check_me(self):
        self.obj.check_me = False
        self.assertEqual(False, self.obj.check_me)

        self.obj.check_me = True
        self.assertEqual(True, self.obj.check_me)

        def fail_check_me():
            self.obj.check_me = "FAIL"

        self.assertRaises(ValueError, fail_check_me)

    def test_name(self):
        self.assertEqual("DemoScript", self.obj.name)
        self.obj.name = "UpdatedDemoScript"
        self.assertEqual("UpdatedDemoScript", self.obj.name)

        def fail_name():
            self.obj.name = 12345

        self.assertRaises(ValueError, fail_name)

    def test_folder(self):
        self.assertEqual("", self.obj.folder)
        self.obj.folder = "ScriptFolder"
        self.assertEqual("ScriptFolder", self.obj.folder)

        def fail_folder():
            self.obj.name = 12345

        self.assertRaises(ValueError, fail_folder)

    def test_fire_event_v2(self):
        self.assertRaises(TypeError, self.obj.fire_event, "NewEvent")
        self.obj.fire_event_v2("NewEvent")
