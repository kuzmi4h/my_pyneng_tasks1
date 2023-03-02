#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для этого использовать шаблон template и подставить в него значения из строки
ospf_route. Значения из строки ospf_route надо получить с помощью Python.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""
'''
ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route = ospf_route.split()

prefix = ospf_route[0]
next_hop = ospf_route[3][:-1]
last_update = ospf_route[4][:-1]
interface = ospf_route[5]


ad_metric=ospf_route[1].strip('[]')
template = f"""
Prefix                {prefix}
AD/Metric             {ad_metric}
Next-Hop              {next_hop}
Last update           {last_update}
Outbound Interface    {interface}
"""
print(template)


import re

ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

# Определяем шаблон для поиска информации о маршруте OSPF
pattern = (
    r"^(?P<prefix>\S+)\s+\[(?P<metric>\d+)/(?P<ad>\d+)\]\s+via\s+"
    r"(?P<next_hop>\S+),\s+(?P<last_update>\S+),\s+(?P<interface>\S+)$"
)

# Ищем информацию о маршруте OSPF в строке ospf_route
match = re.search(pattern, ospf_route)

# Выводим найденную информацию на экран
print(f"Prefix                {match['prefix']}")
print(f"AD/Metric             {match['ad']}/{match['metric']}")
print(f"Next-Hop              {match['next_hop']}")
print(f"Last update           {match['last_update']}")
print(f"Outbound Interface    {match['interface']}")
'''

ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

# Разбиваем строку по пробелам, получаем список слов
words = ospf_route.split()

# Выводим информацию
print(f"Prefix                {words[0]}")
print(f"AD/Metric             {words[1].strip('[]')}")
print(f"Next-Hop              {words[3].rstrip(',')}")
print(f"Last update           {words[4].rstrip(',')}")
print(f"Outbound Interface    {words[5]}")

