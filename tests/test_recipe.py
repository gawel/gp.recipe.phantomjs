# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
import subprocess


def test_binaries():
    dirname = os.path.dirname(sys.argv[0])
    phantomjs = os.path.join(dirname, 'phantomjs')
    assert os.path.isfile(phantomjs), os.listdir(dirname)
    p = subprocess.Popen('%s -h' % phantomjs, shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    p.wait()
    assert b'Usage:' in p.stdout.read()

    casperjs = os.path.join(dirname, 'casperjs')
    assert os.path.isfile(casperjs), os.listdir(dirname)
    p = subprocess.Popen(casperjs, shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    p.wait()
    assert b'Usage:' in p.stdout.read()
