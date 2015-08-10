# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# bitmap的实现
class Bitmap():
    def __init__(self,max):
        self.size = int((max+31-1)/31)
        self.array = [0 for i in range(self.size)]
        
    def bitIndex(self,num):
        return num % 31
        
    def set(self, num):
        elemIndex = num/31
        byteIndex = self.bitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem | (1<<byteIndex)
        
    def test(self, i):
        elemIndex = i/31
        byteIndex = self.bitIndex(i)
        if self.array[elemIndex] & (1 << byteIndex):
            return True
        return False    
        
if __name__=='__main__':        
        MAX=ord('z')
        suffle_array=[x for x in 'coledraw']
        result  =[]
        bitmap =Bitmap(MAX)
        for c in suffle_array:
            bitmap.set(ord(c))
        for i in range(MAX + 1):
            if bitmap.test(i):
                result.append(chr(i))

print '原始数组为： %s' %suffle_array
print '排序后的数组为：%s' %result
