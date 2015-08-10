# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 图

chart ={"A":["B","D"],"C":["E"],"D":["C","E"]}
def path(chart,x,y,pathd=[]):
    pathd=pathd+[x]
    if x==y:
        return pathd
    if not chart.has_key(x):
        return None
        
    for jd in chart[x]:
        if jd not in pathd:
            newjd=path(chart,jd,y,pathd)
            if newjd:
                return newjd