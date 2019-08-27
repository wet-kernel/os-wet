# In the name of God, the Compassionate, the Merciful.
# OS Wet (c) 2019 Mani Jamali. Free Software GNU General Public License version 3.0

# include/install.py : Installer library

import os, py_compile

def writer (src,dest,job_name):
    file = open(src,"r")
    strv = file.read()
    file.close()

    file = open(dest,"a")
    file.write(strv+"\n")
    file.close()

    file = open ("jobs/"+job_name,"w")

def check (job_name):
    if os.path.isfile ("jobs/"+job_name):
        return False
    else:
        return True

def compile (src,dest):
    py_compile.compile(src,dest)