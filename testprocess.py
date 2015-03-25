#! /usr/bin/python
import os
import sys
import time
def child_process():
    '''child process'''
    print 'child process is running'
    sys.exit(0)
def parent_process():
    '''parent process'''
    time.sleep(5)
    print 'parent process is running'
    print 'waiting for child process'
    exit_stat = os.wait()
    print "waited child process's PID = %d" % (exit_stat[0])
    sys.exit(0)
def main():
    '''main function'''
    try:
        pid = os.fork()
        if pid > 0:
            '''parent process'''
            parent_process()
        else:
            child_process()
    except OSError, e:
        print os.strerror(e.errno)
if __name__ == '__main__':
    main()
