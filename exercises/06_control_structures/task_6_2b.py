# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
    ip = input('Введите IP-адрес в формате 10.0.1.1: ')
    octets = ip.split('.')
    if len(octets) != 4:
        print('Неправильный IP-адрес')
        continue
    correct_ip = True
    for octet in octets:
        if not octet.isdigit() or not 0 <= int(octet) <= 255:
            correct_ip = False
            print('Неправильный IP-адрес')
            break
    if correct_ip:
        first_octet = int(octets[0])
        if first_octet >= 1 and first_octet <= 223:
            print('unicast')
        elif first_octet >= 224 and first_octet <= 239:
            print('multicast')
        elif ip == '255.255.255.255':
            print('local broadcast')
        elif ip == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
        break

