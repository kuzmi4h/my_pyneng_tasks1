#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""
'''
mac = "AAAA:BBBB:CCCC"
binary_mac = ''.join([bin(int(x, 16))[2:].zfill(4) for x in mac.split(':')])
print(binary_mac)


mac = "AAAA:BBBB:CCCC"

binary_mac = ""
for group in mac.split(":"):
    # преобразуем каждую группу в число в 16-ричной системе и затем в двоичную строку
    binary_mac += format(int(group, 16), "08b")

print(binary_mac)

import binascii

mac = "AAAA:BBBB:CCCC"
bin_mac = bin(int(binascii.hexlify(mac.replace(':', '').encode()), 16))[2:]
print(bin_mac)

'''
mac = "AAAA:BBBB:CCCC"
mac = mac.replace(':','')
mac = int(mac, 16)
mac = bin(mac)[2:]
print(mac)
