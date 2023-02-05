#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_net = input("Введите IP-сети в формате: 10.1.1.0/24 ")
n1, n2, n3, n4 = ip_net.split('/')[0].split('.')
mask = ip_net.split("/")[1]
mask2 = "1" * int(mask) + 0 * (32 - int(mask))
print(mask2)
'''access_template = ['Network:',
                   '{}{}{}{}',
                   '{}{}{}{}',
                   'Mask:',
                   '/{}',
                   '{}',
                   '{}' ]

print('\n'.join(access_template).format(n1, n2, n3, n4, n1, n2, n3 ,n4, mask, mask, mask))
'''

print(f'''
      Network:
      {n1:<8} {n2:<8} {n3:<8} {n4:<8}
      {int(n1):08b} {int(n2):08b} {int(n3):08b} {int(n4):08b}
      Mask:
      /{mask}
      {n1:<8} {n2:<8} {n3:<8} {n4:<8}
      {int(n1):08b} {int(n2):08b} {int(n3):08b} {int(n4):08b}
      '''
      )
