#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, v = map(int, input().split())

vs = []
ws = []
for i in range(n):
    vi, wi = map(int, input().split())
    vs.append(vi)
    ws.append(wi)

f = [0] + [-float('inf')]*v #!
# f = [0]*(v+1)
# iterate objects
for i in range(n):
    # iterate volumn
    for j in range(v, vs[i]-1, -1):
        # consider only first i obj, limited in j, the best value I can get is f[j]
        # the current f[j] is f[i-1][j], that is, did not consider obj i
        # 2 choices: choose -> value of obj i + best value given remaining volumn & 
        #                                       does not consider obj i(we have chosen)
        #            not choose -> best value I can get w/o consiering obj i given volumn j => f[j]
        # (f[j-vs[i]] since j-vs[i]<j, it has not been calculated yet, it is actually f[i-1][j-vs[i]])
        # (f[j] means the consider only i-1 obj, f[i-1][j])
        # WANT the bigger value
        f[j] = max(ws[i] + f[j - vs[i]], f[j])
# print(f[-1])
print(max(f)) #!

#! base case: when no obj is considered,
# [0,-INF,-INF,-INF,...,-INF] => bag with volumn 0 should be 0, 恰好装满，其他背包没有被恰好装满
# [0, 0, 0, 0, 0, ..., 0] => all bags are 0, 只求最大价值，背包不需要被装满，所以其他背包得到的最大价值=0
        