#!/usr/bin/env python
import subprocess

"""
A ssh based command dispatch system
"""
machines = ["~/dev/test",
        "~/dev/ops",
        ]

cmd = "-lt"
for machine in machines:
    subprocess.call("ls %s %s " % (machine, cmd), shell= True)

