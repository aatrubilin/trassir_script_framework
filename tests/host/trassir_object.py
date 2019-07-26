import unittest


class FakeTrassirObject(object):
    def __init__(self, name):
        self._name = name
        self._changes_callbacks__dbg = []
        self._states__dbg = {}
        self.guid = ""

        self.fake_obj = True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @name.getter
    def name(self):
        if self.fake_obj:
            raise EnvironmentError("object '%s' not found" % (self.guid or self._name))
        return self._name

    def activate_on_state_changes(self, callback):
        self._changes_callbacks__dbg.append(callback)

    def state(self, key):
        return self._states__dbg[key]

    def change_state__dbg(self, key, value):
        if self._states__dbg[key] != value:
            for callback in self._changes_callbacks__dbg:
                callback()
        self._states__dbg[key] = value


class FakeTrassirChannel(FakeTrassirObject):
    def __init__(self, name):
        FakeTrassirObject.__init__(self, name)
        self.states__dbg = {
            "motion": "No Motion",
            "recording": "Not Recording",
            "recording_on_device": "Not Recording (on device)",
            "signal": "Signal",
            "sound_detector": "Disabled",
        }
        self.fake_obj = False

    def export_archive(self, string_start_time_YYYYMMDD_HHMMSS, string_end_time_YYYYMMDD_HHMMSS, string_filename, options):
        pass

    def manual_record_start(self):
        pass

    def manual_record_stop(self):
        pass

    def merge_interest_off(self):
        pass

    def merge_interest_on(self):
        pass

    def ptz_position_query(self):
        return

    def ptz_preset(self, integer_preset_n):
        pass

    def record_off(self):
        pass

    def record_on(self):
        pass

    def screenshot(self):
        pass

    def screenshot_ex(self, string_timestamp, string_directory):
        pass

    def screenshot_v2(self, string_time_YYYYMMDD_HHMMSS, string_screenshot_filename, string_screenshot_folder, integer_make_thumb):
        pass

    def screenshot_v2_figures(self, string_time_YYYYMMDD_HHMMSS, string_screenshot_filename, string_screenshot_folder, integer_make_thumb):
        pass

    def set_watermark(self, string_watermark_text, integer_watermark_position, integer_timestamp_position):
        pass


class FakeTrassirIPDevice(FakeTrassirObject):
    def __init__(self, name):
        FakeTrassirObject.__init__(self, name)
        self._states__dbg = {
            "connection": "Connected",
            "hdd": "HDD OK"
        }
        self.fake_obj = False


class FakeTrassirDeepDetectionZone(FakeTrassirObject):
    def __init__(self, name):
        FakeTrassirObject.__init__(self, name)
        self._states__dbg = {
            "objects_inside": "No Tracked Objects in Zone",
            "zone_health": "Normal",
            "zone_queue": "0"
        }
        self.fake_obj = False


class FakeTrassirTemplate(FakeTrassirObject):
    def __init__(self, name):
        FakeTrassirObject.__init__(self, name)
        self._states__dbg = {
            "shared": "Local",
            "state": "Any State"
        }
        self.fake_obj = False

    def delete_template(self):
        pass


class FakeTrassirOperatorGUI(FakeTrassirObject):
    def __init__(self, name):
        FakeTrassirObject.__init__(self, name)
        self._states__dbg = {
            "sleeping": "Operator Works"
        }
        self.fake_obj = False

    def show_channel(self, channel_name, monitor_n):
        pass

    def show_channel_with_sound(self, channel_name, monitor_n):
        pass

    def show_template(self, template_name, monitor_n):
        pass

    def archive_export(self, channel_name_or_guid, start_time_YYYYMMDD_HHMMSS, end_time_YYYYMMDD_HHMMSS, filename, archive_on_device):
        pass

    def archive_export_ss(self, channel_name_or_guid, start_time_YYYYMMDD_HHMMSS, end_time_YYYYMMDD_HHMMSS, filename, archive_on_device):
        pass

    def archive_export_ex(self, channel_name_or_guid, start_time_YYYYMMDD_HHMMSS, end_time_YYYYMMDD_HHMMSS, filename, options):
        pass

    def create_cms_filter(self, filter_name, filter_data):
        pass

    def show_template_by_guid(self, template_name, monitor_n):
        pass

    def show(self, channel_or_template, monitor_n):
        pass

    def update_active_monitor(self, csv_channels):
        pass

    def show_archive(self, channel_or_template, monitor_n, start_time_YYYYMMDD_HHMMSS, end_time_YYYYMMDD_HHMMSS):
        pass

    def archive_open_inplace(self, channel_or_template, start_time_YYYYMMDD_HHMMSS):
        pass

    def screenshot_ex(self, channel_name, time_YYYYMMDD_HHMMSS, screenshot_filename, screenshot_folder, make_thumb):
        pass

    def screenshot(self, channel_name, time_YYYYMMDD_HHMMSS, screenshot_filename):
        pass

    def show_html(self, source, url):
        pass

    def show_html_on_monitor(self, monitor_n, source, url):
        pass

    def show_html_on_template(self, monitor_n, template_name, source, url):
        pass

    def change_view_settings(self, name, value):
        pass

    def raise_monitor(self, monitor_n):
        pass

    def assign_channels(self, csv_channels, monitor_n):
        pass

    def assign_channels_nxm(self, csv_channels, monitor_n, layout_n, layout_m):
        pass

    def eco_start(self, channel_name, monitor_n):
        pass

    def eco_stop(self, channel_name, monitor_n):
        pass

    def ptz_start(self, channel_name, monitor_n):
        pass

    def ptz_stop(self, channel_name, monitor_n):
        pass

    def ptz_set_coordinates(self, channel_name, monitor_n, pan, tilt, zoom):
        pass

    def ptz_turn_x(self, channel_name, monitor_n, pan_speed):
        pass

    def ptz_turn_y(self, channel_name, monitor_n, tilt_speed):
        pass

    def ptz_set_zoom(self, channel_name, monitor_n, speed):
        pass

    def ptz_set_focus(self, channel_name, monitor_n, speed):
        pass

    def ptz_set_iris(self, channel_name, monitor_n, speed):
        pass

    def ptz_focus_auto(self, channel_name, monitor_n):
        pass

    def ptz_iris_auto(self, channel_name, monitor_n):
        pass

    def use_hq(self, channel_name, monitor_n, use_hq):
        pass

    def sip_make_call(self, sip_id):
        pass

    def sip_accept_call(self):
        pass

    def sip_reject_call(self):
        pass

    def sip_send_code(self, code):
        pass

    def sip_transfer_call(self, sip_id):
        pass

    def open_travi(self, travi_file_path, monitor_n):
        pass


class FakeObjectSelfTest(unittest.TestCase):

    def test_activate_on_changes_callbacks(self):
        def callback_1():
            callback_1.times_called += 1
        callback_1.times_called = 0

        def callback_2():
            callback_2.times_called += 1
        callback_2.times_called = 0

        fake_device = FakeTrassirIPDevice("Fake Device")
        fake_device.activate_on_state_changes(callback_1)
        fake_device.activate_on_state_changes(callback_2)
        fake_device.change_state__dbg("hdd", "HDD ERROR")

        self.assertEqual(callback_1.times_called, 1, "Callback 1 called first time")
        self.assertEqual(callback_2.times_called, 1, "Callback 2 called first time")

        fake_device.change_state__dbg("hdd", "HDD OK")

        self.assertEqual(callback_1.times_called, 2, "Callback 1 called second time")
        self.assertEqual(callback_2.times_called, 2, "Callback 2 called second time")

        fake_device.change_state__dbg("hdd", "HDD OK")

        self.assertEqual(callback_1.times_called, 2, "Callback 1 no more calls")
        self.assertEqual(callback_2.times_called, 2, "Callback 2 no more calls")


if __name__ == "__main__":
    unittest.main()
