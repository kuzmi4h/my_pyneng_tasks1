#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Задание 5.1b

Переделать скрипт из задания 5.1a таким образом, чтобы, при запросе параметра,
отображался список возможных параметров. Список параметров надо получить из словаря,
а не прописывать вручную.

Вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
$ python task_5_1b.py
Введите имя устройства: r1
Введите имя параметра (location, vendor, model, ios, ip): ip
10.255.0.1

$ python task_5_1b.py
Введите имя устройства: sw1
Введите имя параметра (location, vendor, model, ios, ip, vlans, routing): ip
10.255.0.101

Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно
решить без использования условия if.
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

#switch = input("Введите имя устройства: ")
#print(f"Введите имя параметра ({list(london_co[switch].keys())}): ", end="")
#param = input()

#print(london_co[switch][param])

device_name = input("Введите имя устройства: ")
param = ",".join(london_co[device_name])
param_name = input(f"Введите имя параметра ({param}): ")

device_dict = london_co.get(device_name, "Такого устройства нет в словаре")
param_value = device_dict.get(param_name, "Такого параметра нет в словаре")    
print(param_value)


