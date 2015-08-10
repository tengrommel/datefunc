# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 树的基本结构
#Tree = [2,3,[58,6,[5]]]

# print Tree[0]
# print Tree[1]
# print Tree[2]
# print Tree[2][1]
#Tree2 = Tree[2]
#print Tree2[0]

class TRee():
    def __init__(self,leftjd=0,rightjd=0,data=0):
        self.leftjd = leftjd
        self.rightjd = rightjd
        self.data = data
        
class Btree():
    def __init__(self, base=0):
        self.base=base
    def empty(self):
        if self.base is 0:
            return True
        else:
            return False
    def qout(self,jd):
        """前序遍历，NLR，根左右"""
        if jd==0:
            return
        print jd.data
        self.qout(jd.leftjd)
        self.qout(jd.rightjd)
    def mout(self, jd):
        """中序遍历，LNR，左根右"""
        if jd==0:
            return
        self.qout(jd.leftjd)            
        print jd.data
        self.qout(jd.rightjd)
    def out(self, jd):
        """后序遍历，LNR，左右根"""
        if jd==0:
            return
        self.qout(jd.leftjd)
        self.qout(jd.rightjd)            
        print jd.data
        