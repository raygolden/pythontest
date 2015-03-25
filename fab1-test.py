#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 漏 2015 ray <ray@ray-ubuntu>
#
# Distributed under terms of the MIT license.

"""
test of fab
"""
def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b
fibfun = fib()
fibresult = [fibfun.next() for c in range(5)]
print fibresult
