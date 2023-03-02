#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
'''
ip = input("Введите ip-адрес в формате x.x.x.x: ")
octets = ip.split('.')

if int(octets[0]) >= 1 and int(octets[0]) <= 223:
    print('unicast')
elif int(octets[0]) >= 224 and int(octets[0]) <= 239:
    print('multicast')
elif (int(octets[0]) and int(octets[1]) and int(octets[2]) and  int(octets[3])) == 255:
    print('local broadcast')
elif (int(octets[0]) and int(octets[1]) and int(octets[2]) and  int(octets[3])) == 0:
    print('unassigned')
else:
    print('unused')
'''
"""
ip_address = input("Введите IP-адрес в формате 10.0.1.1: ")
ip_octets = ip_address.split(".")

first_octet = int(ip_octets[0])

if first_octet >= 1 and first_octet <= 223:
    print("unicast")
elif first_octet >= 224 and first_octet <= 239:
    print("multicast")
elif ip_address == "255.255.255.255":
    print("local broadcast")
elif ip_address == "0.0.0.0":
    print("unassigned")
else:
    print("unused")
"""

# запрос ввода IP-адреса
ip_address = input("Введите IP-адрес в формате 10.0.1.1: ")

# разбиение IP-адреса на октеты
octets = ip_address.split('.')

# проверка типа адреса
if octets == ['0', '0', '0', '0']:
    print("unassigned")
elif octets == ['255', '255', '255', '255']:
    print("local broadcast")
elif int(octets[0]) >= 1 and int(octets[0]) <= 223:
    print("unicast")
elif int(octets[0]) >= 224 and int(octets[0]) <= 239:
    print("multicast")
else:
    print("unused")

