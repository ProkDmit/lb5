#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import math
a1=int(input("a1= "))
a2=int(input("a2= "))
b1=int(input("b1= "))
b2=int(input("b2= "))
A=math.sqrt(a1*a1+a2*a2)
B=math.sqrt(b1*b1+b2*b2)
if A>B:
    print("Точка A находится дальше")
else:
    print("Точка B находится дальше")
