# Python wrapper used to run the submission

import os, sys, signal

try:
    sys.path = ['subdir'] + sys.path
    import program
except:
    os.kill(os.getpid(), signal.SIGUSR2)
