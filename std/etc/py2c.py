#!/usr/bin/python

import py_compile
import sys

# Compile the python script to check the code correctness
py_compile.compile(sys.argv[1])
