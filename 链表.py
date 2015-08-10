# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#链表的实现（单向链表）
class jd():
    def __init__(self, data):
        self.data=data
        self.next=None

class Linklist():
    def __init__(self,jd2):  
        self.head=jd2
        self.head.next=None
        self.tail=self.head
    
    def add(self,jd2):
        self.tail.next=jd2
        self.tail=self.tail.next

    def view(self):
        jd2=self.head
        linkstr=""
        while jd2 is not None:
            if jd2.next is not None:
                linkstr=linkstr+str(jd2.data)+"-->"
            else:
                linkstr+=str(jd2.data)
            jd2=jd2.next
        print linkstr    
        
        
