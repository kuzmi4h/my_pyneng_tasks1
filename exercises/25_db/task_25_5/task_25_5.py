#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Задание 25.5

Для заданий 25 раздела нет тестов!

После выполнения заданий 25.1 - 25.5 в БД остается информация о неактивных записях.
И, если какой-то MAC-адрес не появлялся в новых записях, запись с ним,
может остаться в БД навсегда.

И, хотя это может быть полезно, чтобы посмотреть, где MAC-адрес находился
в последний раз, постоянно хранить эту информацию не очень полезно.

Например, если запись в БД уже больше месяца, то её можно удалить.

Для того, чтобы сделать такой критерий, нужно ввести новое поле,
в которое будет записываться последнее время добавления записи.

Новое поле называется last_active и в нем должна находиться строка,
в формате: YYYY-MM-DD HH:MM:SS.

В этом задании необходимо:
* изменить, соответственно, таблицу dhcp и добавить новое поле.
 * таблицу можно поменять из cli sqlite, но файл dhcp_snooping_schema.sql тоже необходимо изменить
* изменить скрипт add_data.py, чтобы он добавлял к каждой записи время

Получить строку со временем и датой, в указанном формате,
можно с помощью функции datetime в запросе SQL.
Синтаксис использования такой:
sqlite> insert into dhcp (mac, ip, vlan, interface, switch, active, last_active)
   ...> values ('00:09:BC:3F:A6:50', '192.168.100.100', '1', 'FastEthernet0/7', 'sw1', '0', datetime('now'));

То есть вместо значения, которое записывается в базу данных,
надо указать datetime('now').

После этой команды в базе данных появится такая запись:
mac                ip               vlan  interface        switch  active  last_active
-----------------  ---------------  ----  ---------------  ------  ------  -------------------
00:09:BC:3F:A6:50  192.168.100.100  1     FastEthernet0/7  sw1     0       2019-03-08 11:26:56
"""
