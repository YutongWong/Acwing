#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N, V = map(int, input().split())
f = [0] * (V+1)

for i in range(N):
    vs = []
    ws = []
    s = int(input().split()[0])
    for k in range(s):
        v, w = map(int, input().split())
        vs.append(v)
        ws.append(w)
    for j in range(V, 0, -1):
        for k in range(s):
            if j >= vs[k]:
                f[j] = max(ws[k]+f[j - vs[k]], f[j])
print(f[-1])

