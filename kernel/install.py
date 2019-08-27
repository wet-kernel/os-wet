# In the name of God, the Compassionate, the Merciful.
# OS Wet (c) 2019 Mani Jamali. Free Software GNU General Public License version 3.0

# install.py : Kernel installer

import py_compile, os

from include import install # import install library

### install headers ###

if install.check("kernel-header") == True:
    install.writer("kernel-header.py", "vmwet.py", "kernel-header")

if install.check("imports_module")==True:
    install.writer("imports_module.py","vmwet.py","imports_module")

if install.check("parameters")==True:
    install.writer("parameters.py","vmwet.py","parameters")

if install.check("sysvar")==True:
    install.writer("sysvar.py","vmwet.py","sysvar")

### install modules ###

if install.check("include_process_colors")==True:
    install.writer("include/process_colors.py","vmwet.py","include_process_colors")

if install.check("include_process")==True:
    install.writer("include/process.py","vmwet.py","include_process")

### install process ###

if install.check("process_root")==True:
    install.writer("process/root.py","vmwet.py","process_root")

if install.check("process_switch")==True:
    install.writer("process/switch.py","vmwet.py","process_switch")

if install.check("process_init")==True:
    install.writer("process/init.py","vmwet.py","process_init")

install.compile ("vmwet.py","vmwet")