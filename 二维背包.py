#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N, V, M = map(int, input().split())
f = [[0] * (M+1) for i in range(V+1)]

for i in range(N):
    v, m, w = map(int, input().split())
    for j in range(V, v-1, -1):
        for k in range(M, m -1, -1):
            f[j][k] = max(w + f[j - v][k - m], f[j][k])
print(f[-1][-1])
