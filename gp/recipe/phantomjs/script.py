# -*- coding: utf-8 -*-
import os
import sys


def main(binaries):
    os.environ['PHANTOMJS_EXECUTABLE'] = binaries['phantomjs']
    script_name = os.path.basename(sys.argv[0])
    script = binaries[script_name]
    args = [script] + sys.argv[1:]
    os.execve(args[0], args, os.environ)
