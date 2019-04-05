# -*- coding: utf-8 -*-
# Пример сохранения скриншота с отправкой на почту
# и добавлением соотвествующего события в Trassir

"""
[many lines of rassir_script_framework source]
"""

pk = PokaYoke()
ss = ShotSaver()
scr_obj = ScriptObject()
senders = [
    EmailSender("QS", "a.trubilin@dssl.ru"),
    PopupSender(),
]

# Загружаем каналы
channels = pk.get_channels("AC-D2121IR3W 2,AC-D7141IR1 3,DS-2CD2142FWD-IS 2")


def shot_callback(success, shot_path):
    if success:
        scr_obj.fire_event_v2("Shot saved", data=shot_path)
        for sender in senders:
            sender.image(shot_path)
    else:
        scr_obj.fire_event_v2("Can't save shot", data=shot_path)


for channel in channels.values():
    ss.async_shot(shot_callback, channel.full_guid)
