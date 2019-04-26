# -*- coding: utf-8 -*-
# Замыкание тревожного выхода для открытия шлабаума
# при распознавании номера из белого списка

"""
[many lines of trassir_script_framework source]
"""


gpio = GPIO()
gate = gpio.get_outputs("Шлагбаум")[0]


def lpr_callback(ev):
    """Callback for AutoTrassir Events

    Args:
        ev (SE_LprEvent): AutoTrassir event
    """

    if "LPR_WHITELIST" in BaseUtils.lpr_flags_decode(ev.flags):
        # Если номер найден в белом списке замыкает трев. выход.
        gate.obj.set_output_high()

        # Через 1500 мс размыкаем тревожный выход.
        host.timeout(1500, lambda: gate.obj.set_output_low)


host.activate_on_lpr_events(lpr_callback)
