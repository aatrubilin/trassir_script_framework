# -*- coding: utf-8 -*-
# Вывод инфомрации о персоне по его имени

"""
[many lines of trassir_script_framework source]
"""

person_name = "Александр Трубилин"

persons = Persons()
person = persons.get_person_by_name(person_name)

if person is None:
    data = "{name} не найден".format(name=person_name)
else:
    base64_image = BaseUtils.image_to_base64(person["image"])
    data = "<b>{name}</b><br><br>{img}".format(
        name=person["name"],
        img=BaseUtils.base64_to_html_img(base64_image, width=300),
    )

host.question(
    "<pre>{data}</pre>".format(data=data),
    "Ok", lambda: None,
)
