#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
0<N,V≤100
0<vi,wi,si≤100
"""

n, m = map(int, input().split())
v, w, s = [], [], []
for i in range(n):
    vi, wi, si = map(int, input().split())
    v.append(vi)
    w.append(wi)
    s.append(si)

f = [0] * (m+1)
for i in range(n):
    for j in range(m, v[i]-1, -1):
        gen = (k for k in range(1, s[i]+1) if k*v[i] <= j)
        for k in gen:
            f[j] = max(k * w[i] + f[j - v[i] * k], f[j])
print(f[-1])


