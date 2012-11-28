# -*- coding: utf-8 -*-
import os
import sys
import subprocess


def test_binaries():
    dirname = os.path.dirname(sys.argv[0])
    phantomjs = os.path.join(dirname, 'phantomjs')
    assert os.path.isfile(phantomjs)
    p = subprocess.Popen('%s -h' % phantomjs, shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    p.wait()
    assert 'Usage:' in p.stdout.read()

    casperjs = os.path.join(dirname, 'casperjs')
    assert os.path.isfile(casperjs)
    p = subprocess.Popen(casperjs, shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    p.wait()
    assert 'Usage:' in p.stdout.read()
