#!/usr/bin/python
# -*- coding: utf-8 -*-

from include import *
from subprocess import call

if __name__ == "__main__":
    #spancat -s "2016-01-31 17:05:00" -e "2016-01-31 17:14:49" real.log > test_real_log.ans
    call(["./timecat.py", "-s", "2016-01-31 17:05:00", "-e", "2016-01-31 17:14:49", "real.log"])
