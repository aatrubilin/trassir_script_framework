# -*- coding: utf-8 -*-
# Вывод текущего состояния всех очередей

"""
[many lines of trassir_script_framework source]
"""

zones = Zones()
queues = zones.get_queues()

for queue in queues:
    host.message("{} -> {} чел".format(queue.name, queue.obj.state("zone_queue")))
