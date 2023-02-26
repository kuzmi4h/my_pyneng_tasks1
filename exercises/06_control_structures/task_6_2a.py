#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address = input("Введите IP-адрес в формате 10.0.1.1: ")
ip_octets = ip_address.split(".")

if all(octet.isdigit() for octet in ip_octets):
   pass 
else:
    print('Неправильный IP-адрес')
    break

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

