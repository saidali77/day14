# -*- coding: utf-8 -*-
a = list(input())
b = list(input())
c = list(input())
if a == b:
    if b == c:
        print('Все введения равны')
    else:
        print('Первое и Второе введение равны')
elif a == c:
    print('Первое и Третье введение равны')
elif b == c:
    print('Второе и Третье введение равны')
