# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 栈的存储方式
class Stack():
    def __init__(st, size):
        st.stack=[]
        # 将传递容量变成传递的数组
        st.size=size
        # 初始化栈底
        st.top=-1
    
    def push(st,content):
        if st.Full():
            print "Stack is Full!"
        else:
            st.stack.append(content)
            st.top=st.top+1
    def out(st):
        if st.Empty():
            print "Stack is empty"
        else:
            st.top=st.top-1
    
    def Full(st):
        if st.top == st.size:
            return True
        else:
            return False
    
    def Empty(st):
        if st.top == -1:
            return True
        else:
            return False
            