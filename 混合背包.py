#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, m = map(int, input().split())
f = [0] * (m+1)

goods = []

for i in range(n):
    v, w, c = map(int, input().split())
    if c == 0:
        goods.append([v, w, 0])
    elif c == -1:
        goods.append([v, w])
    else:
        k = 1
        while k <= c:
            c -= k
            goods.append([k * v, k * w])
            k *= 2
        if c != 0: goods.append([c * v, c * w])

for good in goods:
    if len(good) == 3:
        for j in range(good[0], m+1):
            f[j] = max(good[1] + f[j - good[0]], f[j])
    else:
        for j in range(m, good[0]-1, -1):
            f[j] = max(good[1] + f[j - good[0]], f[j])
print(f[-1])