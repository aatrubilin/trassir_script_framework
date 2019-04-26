# -*- coding: utf-8 -*-
# Сохранение скриншотов за последний час с интервалом 1 минута

"""
[many lines of trassir_script_framework source]
"""
import threading
from datetime import datetime, timedelta

channels = Channels()
my_channel = channels.get_enabled("AC-D2141IR3 Склад")[0]

dt_now = datetime.now()
dt_range = [dt_now - timedelta(minutes=i) for i in xrange(60)]

save_result = {
    "success": 0,
    "fail": 0
}
lock = threading.Lock()


def callback(success, shot_path):
    global save_result, lock
    lock.acquire()
    try:
        if success:
            save_result["success"] += 1
        else:
            save_result["fail"] += 1
    finally:
        lock.release()


shot_args = []
for dt in dt_range:
    shot_args.append(
        ((my_channel.full_guid,), {"dt": dt, "callback": callback})
    )

ss = ShotSaver()
ss.screenshots_folder += "/timelapse"


def end_callback():
    if save_result["success"]:
        message("Saved {} shots".format(save_result["success"]))
    else:
        error("Failed to save {} shots".format(save_result["fail"]))


ss.pool_shot(shot_args, pool_size=5, end_callback=lambda: host.timeout(1000, end_callback))
