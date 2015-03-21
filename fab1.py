#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 漏 2014 ray.huang <ray.huang@ray-gii-rmbp>
#
# Distributed under terms of the MIT license.

"""

"""
def fib(n):
    a, b = 1, 1
    for i in range(int(n)-1):
        a, b = b, a+b
    return a    
inputnum = raw_input('please input the number:')
print fib(inputnum)
