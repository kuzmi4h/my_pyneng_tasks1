#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


ospf_route = open("ospf.txt")

for line in ospf_route:
    line = line.replace(",", " ").split()
    prefix, metric, nexthop, update, intf = line[1], line[2].strip("[]"), line[4], line[5], line[6]
    print(f'Prefix                {prefix}')
    print(f'AD/Metric             {metric}')
    print(f'Next-Hop              {nexthop}')
    print(f'Last update           {update}')
    print(f'Outbound Interface    {intf}')
