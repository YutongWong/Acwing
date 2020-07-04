#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, m = map(int, input().split())

f = [0] * (m+1)
# 二进制优化优化本质：转化成01背包，把k个第i物品用二进制方法拆成多个物品（而不是k个物品）。
# 二进制优化：有选和不选两种选择
goods = []
# 拆！
for i in range(n):
    v, w, s = map(int, input().split())
    k = 1
    while k <= s:
        s -= k
        goods.append([k*v, k*w])
        k *= 2
        
    if s != 0: goods.append([s*v, s*w])
        

# 01backpack
for good in goods:
    for j in range(m, good[0]-1, -1):
        f[j] = max(good[1] + f[j - good[0]], f[j])
print(f[-1])
    