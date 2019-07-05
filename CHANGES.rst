=========
Changelog
=========

Version 0.6
===========
*Released 2019-07-05*

Changes

- Fix :meth:`trassir_script_framework.BaseUtils.win_encode_path`
- Update tbot_api
- Other fixes

Version 0.5
===========
*Released 2019-05-16*

New Features

- Added :meth:`trassir_script_framework.BaseUtils.save_pkl`
- Added :meth:`trassir_script_framework.BaseUtils.load_pkl`
- Added :class:`trassir_script_framework.Templates`
- Added :meth:`trassir_script_framework.GUITemplate.delete`

Changes

- Fix ShotSaver examples
- Rename Template to :class:`trassir_script_framework.GUITemplate`
- Fix some errors in :meth:`trassir_script_framework.BaseUtils.image_to_base64`
- Add extension to file_log in :meth:`trassir_script_framework.BaseUtils.get_logger`

Version 0.4
===========
*Released 2019-04-30*

New Features

- Added :meth:`trassir_script_framework.BaseUtils.set_script_name`

Changes

- Fix catch_request_exceptions in :class:`trassir_script_framework.HTTPRequester`
- Add tg_users argument to :class:`trassir_script_framework.TelegramSender` methods

Version 0.3
===========
*Released 2019-04-26*

New Features

- Added :meth:`trassir_script_framework.BaseUtils.is_template_exists`
- Added :class:`trassir_script_framework.HTTPRequester`
- Added :meth:`trassir_script_framework.ShotSaver.pool_shot`
- Added :meth:`trassir_script_framework.Persons.get_person_by_name`
- Added :meth:`trassir_script_framework.BaseUtils.image_to_base64`
- Added :meth:`trassir_script_framework.BaseUtils.base64_to_html_img`
- Added more `examples
  <https://github.com/AATrubilin/trassir_script_framework/tree/master/examples>`_

Changes

- Added data to string transform :meth:`trassir_script_framework.ScriptObject.fire_event_v2`
- Added raise exception in functions with :meth:`trassir_script_framework.BaseUtils.run_as_thread_v2`
- Change argument structure in :meth:`trassir_script_framework.BaseUtils.to_json`
- Change argument structure in :meth:`trassir_script_framework.ShotSaver.async_shot`
- Fix: :class:`trassir_script_framework.FTPSender` errors when send several files
- Fix: :class:`trassir_script_framework.FTPSender` remove self.logger
- Fix: :meth:`trassir_script_framework.BaseUtils.get_logger` permission denied when deleting log file

Version 0.2b
============
*Released 2019-04-12*

New Features

- Added :class:`trassir_script_framework.FTPSender`
- Added :meth:`trassir_script_framework.BaseUtils.lpr_flags_decode`
- Added more examples

Changes

- Transferring PokaYoke GET methods to independent classes
  and extended functionality:

    | `PokaYoke.get_servers` -> :class:`trassir_script_framework.Servers`
    | `PokaYoke.get_persons` -> :class:`trassir_script_framework.Persons`
    | `PokaYoke.get_person_folders` -> :class:`trassir_script_framework.Persons`
    | `PokaYoke.get_users` -> :class:`trassir_script_framework.Users`
    | `PokaYoke.get_terminals` -> :class:`trassir_script_framework.PosTerminals`
    | `PokaYoke.get_ip_cameras` -> :class:`trassir_script_framework.Devices`
    | `PokaYoke.get_channels` -> :class:`trassir_script_framework.Channels`
    | `PokaYoke.get_networks` -> :class:`trassir_script_framework.NetworkNodes`
    | `PokaYoke.get_rules` -> :class:`trassir_script_framework.Rules`
    | `PokaYoke.get_scripts` -> :class:`trassir_script_framework.Scripts`
    | `PokaYoke.get_schedules` -> :class:`trassir_script_framework.Schedules`
    | `PokaYoke.get_servers` -> :class:`trassir_script_framework.EmailAccounts`
    | `PokaYoke.get_template_loops` -> :class:`trassir_script_framework.TemplateLoops`
    | `PokaYoke.get_gpio_inputs` -> :class:`trassir_script_framework.GPIO`
    | `PokaYoke.get_gpio_outputs` -> :class:`trassir_script_framework.GPIO`
    | `PokaYoke.get_people_zones` -> :class:`trassir_script_framework.Zones`
    | `PokaYoke.get_simt_zones` -> :class:`trassir_script_framework.Zones`
    | `PokaYoke.get_workplaces` -> :class:`trassir_script_framework.Zones`
    | `PokaYoke.get_queues` -> :class:`trassir_script_framework.Zones`
    | `PokaYoke.get_shelves` -> :class:`trassir_script_framework.Zones`
    | `PokaYoke.get_people_zones` -> :class:`trassir_script_framework.Zones`
    | `PokaYoke.get_head_borders` -> :class:`trassir_script_framework.Borders`
    | `PokaYoke.get_people_borders` -> :class:`trassir_script_framework.Borders`
    | `PokaYoke.get_simt_borders` -> :class:`trassir_script_framework.Borders`
    | `PokaYoke.get_deep_people_borders` -> :class:`trassir_script_framework.Borders`
    | `PokaYoke.get_all_borders` -> :class:`trassir_script_framework.Borders`
    | `PokaYoke.get_access_points` -> :class:`trassir_script_framework.Sigur`


- Rename some method and classes:

    | `BaseUtils.check_file` -> :meth:`trassir_script_framework.BaseUtils.is_file_exists`
    | `BaseUtils.check_folder` -> :meth:`trassir_script_framework.BaseUtils.is_folder_exists`
    | `BaseUtils.pretty_json` -> :meth:`trassir_script_framework.BaseUtils.to_json`
    | `PokaYokeObject` -> :meth:`trassir_script_framework.TrObject`

- Fix some typos


Version 0.1b
============
*Released 2019-04-05*

- Beta release
