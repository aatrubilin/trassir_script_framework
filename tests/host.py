import os


def exec_encoded(script):
    return script


class TrassirObject:
    pass


class SE_Settings(dict):
    def __init__(self, path, data=None):
        if data is None:
            data = {"name": "name"}
        super(SE_Settings, self).__init__(data)
        self.type = ""
        self.guid = "guid"
        self.name = "name"

    def ls(self):
        return [SE_Settings("test"), SE_Settings("test2")]


def settings(path):
    if path == "system_wide_options":
        return {"screenshots_folder": os.getcwd()}
    return SE_Settings("path")


class Object:
    def __init__(self, guid):
        self.name = "name"
        self.guid = guid


def object(id):
    return Object(id)


class stats:
    def parent(self):
        return {"name": "script_name"}


def objects_list(type):
    return [("guid", "name", type, "parent")]