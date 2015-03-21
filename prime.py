#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 漏 2014 ray.huang <ray.huang@ray-gii-rmbp>
#
# Distributed under terms of the MIT license.

"""
Output all prime numbers up to a specified integer n
"""

def prime( n ):
    primes = [2]
    num = 3
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    print primes
    return primes

if __name__ == '__main__':
    prime(50)
