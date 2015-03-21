#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 漏 2014 ray.huang <ray.huang@ray-gii-rmbp>
#
# Distributed under terms of the MIT license.

"""

"""
def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b
fibfun = fib()
fibresult = [fibfun.next() for i in range(15)]
print fibresult
