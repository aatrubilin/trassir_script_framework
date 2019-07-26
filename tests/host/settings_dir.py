import string
import unittest

from .utils import generate_random_guid


class FakeSettingsDir(dict):
    def __init__(self, guid=None, name=None, dir_type=None, path=None, parent=None, **kwargs):
        super(FakeSettingsDir, self).__init__(**kwargs)
        if path is not None and parent is not None:
            raise ValueError("Can not specify both explicit path and parent")

        self._changes_callbacks__dbg = []
        self._children__dbg = []

        self.type = dir_type
        self.name = name
        if guid is not None:
            if any([c not in string.letters + string.digits for c in guid]):
                raise ValueError("Illegal characters in explicit guid")
            self.guid = guid
        else:
            self.guid = generate_random_guid()
        self._parent = parent

        if self._parent is not None:
            self._parent._children__dbg.append(self)
            if self._parent.path:
                if self._parent.path == "/":
                    self.path = self._parent.path + self.guid
                else:
                    self.path = self._parent.path + "/" + self.guid
            else:
                self.path = self.guid
        else:
            if path is not None:
                if path != "/":
                    path_split = path.split("/")
                    for idx, guid in enumerate(path_split):
                        if not guid:
                            if idx != 0:
                                raise ValueError("Illegal explicit path")
                        else:
                            if any([c not in string.letters + string.digits for c in guid]):
                                raise ValueError("Illegal explicit path")
                self.path = path
            else:
                self.path = ""

    def __setitem__(self, key, value):
        if key not in self or key in self and self[key] != value:
            for callback in self._changes_callbacks__dbg:
                callback()
        super(FakeSettingsDir, self).__setitem__(key, value)

    def __getitem__(self, key):
        # TODO(p.sadovnikov): Write more robust implementation
        if key == "name":
            return self.name
        raise NotImplementedError("Not implemented key: {}".format(key))

    def ls(self):
        return list(self._children__dbg)

    def subdir(self, dir_guid):
        try:
            return next(child for child in self._children__dbg if dir_guid == child.guid)
        except StopIteration:
            return None

    def parent(self):
        return self._parent

    def cd(self, path):
        if not path:
            return None  # yup, can not go nowhere
        if path.startswith("/"):
            return None  # only downward cd implemented for test by default
        split_path = path.split("/")
        return self.cd_recursive__dbg(split_path)

    def cd_recursive__dbg(self, split_path):
        if not split_path:
            return self
        dir_guid = split_path[0]
        if not dir_guid:
            return self
        directory = self.subdir(dir_guid)
        if directory is None:
            return directory
        return directory._cd_recursive(split_path[1:])

    def is_value_default(self, key):
        if key in self:
            # Notice that generally that is not the case but for test purposes consider it so
            return False
        return True

    def unset_value(self, key):
        if key in self:
            del self[key]
            for callback in self._changes_callbacks__dbg:
                callback()
        return

    def activate_on_changes(self, callback):
        self._changes_callbacks__dbg.append(callback)


class FakeSettingsDirSelfTest(unittest.TestCase):

    # @unittest.skip("it is OK")
    def test_activate_on_changes_callbacks(self):
        def callback_1():
            callback_1.times_called += 1
        callback_1.times_called = 0

        def callback_2():
            callback_2.times_called += 1
        callback_2.times_called = 0

        fake_dir = FakeSettingsDir()
        fake_dir.activate_on_changes(callback_1)
        fake_dir.activate_on_changes(callback_2)
        fake_dir["anykey"] = "anyvalue"

        self.assertEqual(callback_1.times_called, 1, "Callback 1 called first time")
        self.assertEqual(callback_2.times_called, 1, "Callback 2 called first time")

        fake_dir.unset_value("anykey")

        self.assertEqual(callback_1.times_called, 2, "Callback 1 called second time")
        self.assertEqual(callback_2.times_called, 2, "Callback 2 called second time")

    def _set_up_cd_tree(self):
        fake_root = FakeSettingsDir(path="")

        _ = FakeSettingsDir(guid="dir1", name="nope1", parent=fake_root)
        fake_dir2 = FakeSettingsDir(guid="dir2", name="subdirectory2", parent=fake_root)

        _ = FakeSettingsDir(guid="dir11", name="subdirectory2_11", parent=fake_dir2)
        _ = FakeSettingsDir(guid="dir22", name="nope22", parent=fake_dir2)

        return fake_root

    # @unittest.skip("it is OK")
    def test_correct_path_construction_1(self):
        fake_root = FakeSettingsDir(path="")
        fake_dir1 = FakeSettingsDir(guid="dir1", parent=fake_root)
        fake_dir2 = FakeSettingsDir(guid="dir2", parent=fake_dir1)
        fake_dir3 = FakeSettingsDir(guid="dir3", parent=fake_dir2)
        self.assertEqual(fake_dir3.path, "dir1/dir2/dir3")

    # @unittest.skip("it is OK")
    def test_correct_path_construction_2(self):
        fake_root = FakeSettingsDir(path="/")
        fake_dir1 = FakeSettingsDir(guid="dir1", parent=fake_root)
        fake_dir2 = FakeSettingsDir(guid="dir2", parent=fake_dir1)
        fake_dir3 = FakeSettingsDir(guid="dir3", parent=fake_dir2)
        self.assertEqual(fake_dir3.path, "/dir1/dir2/dir3")

    # @unittest.skip("it is OK")
    def test_correct_path_construction_3(self):
        fake_root = FakeSettingsDir(path="test1/test2")
        fake_dir1 = FakeSettingsDir(guid="dir1", parent=fake_root)
        fake_dir2 = FakeSettingsDir(guid="dir2", parent=fake_dir1)
        fake_dir3 = FakeSettingsDir(guid="dir3", parent=fake_dir2)
        self.assertEqual(fake_dir3.path, "test1/test2/dir1/dir2/dir3")

    # @unittest.skip("it is OK")
    def test_incorrect_path_construction_1(self):
        self.assertRaises(ValueError, FakeSettingsDir, path="test1/test2/")

    # @unittest.skip("it is OK")
    def test_incorrect_path_construction_2(self):
        self.assertRaises(ValueError, FakeSettingsDir, path="test1//test2")

    # @unittest.skip("it is OK")
    def test_incorrect_path_construction_3(self):
        self.assertRaises(ValueError, FakeSettingsDir, path="test1/%^&*")

    # @unittest.skip("it is OK")
    def test_subdir_1(self):
        root = self._set_up_cd_tree()
        result = root.subdir("dir2")
        self.assertEqual(result.name, "subdirectory2", "subdir to correct directory")

    # @unittest.skip("it is OK")
    def test_cd_1(self):
        root = self._set_up_cd_tree()
        result = root.cd("dir2/dir11")
        self.assertEqual(result.name, "subdirectory2_11", "cd to correct directory")

    # @unittest.skip("it is OK")
    def test_subdir_2(self):
        root = self._set_up_cd_tree()
        result = root.subdir("nonexistent")
        self.assertEqual(result, None, "no such directory directory")

    # @unittest.skip("it is OK")
    def test_cd_2(self):
        root = self._set_up_cd_tree()
        result = root.cd("dir2/nonexistent")
        self.assertEqual(result, None, "no such directory directory")


if __name__ == "__main__":
    unittest.main()
