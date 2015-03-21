#!/usr/bin/env python
import platform

profile = [
        platform.architecture(),
        platform.dist(),
        platform.system(),
        ]

for item in profile:
    print item
