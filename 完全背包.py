#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, m = map(int, input().split())

f = [0] * (m+1)

for i in range(n):
    v, w = map(int, input().split())
    
    for j in range(v, m+1):
        f[j] = max(w + f[j-v], f[j])
print(f[-1])
 
    