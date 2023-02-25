#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""



access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
# Запрос у пользователя информации о режиме работы интерфейса
mode = input("Введите режим работы интерфейса (access/trunk): ")

access_int = 'номер VLAN:'
trunk_int = 'разрешенные VLANы:'
interf = {"access": access_int, "trunk": trunk_int}
inter = "".join(interf[mode])
# Запрос у пользователя информации о номере интерфейса
interface = input("Введите имя интерфейса: ")

# Запрос у пользователя информации о номере VLANов
vlan = input(f"Введите {inter}: ")

# Создание словаря для замены access/trunk на соответствующий шаблон
mode_dict = {"access": access_template, "trunk": trunk_template}

# Создание шаблона команд для заданного режима
template = "\n".join(mode_dict[mode])

# Вывод на экран конфигурации интерфейса
print("\n" + "interface " + interface)
print(template.format(vlan))
