# -*- coding: utf-8 -*-
# Пример сохранения скриншота с отправкой на почту

"""
[many lines of trassir_script_framework source]
"""
channels = Channels()
sender = EmailSender("QS", "a.trubilin@dssl.ru"),
ss = ShotSaver()

# Загружаем каналы
selected_channels = channels.get_enabled("AC-D2121IR3W 2,AC-D7141IR1 3,DS-2CD2142FWD-IS 2")


def shot_callback(success, shot_path):
    if success:
        sender.image(shot_path)
    else:
        host.error("Can't save shot %s" % shot_path)


for channel in selected_channels:
    ss.async_shot(shot_callback, channel.full_guid)
