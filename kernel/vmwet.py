# In the name of God, the Compassionate, the Merciful.
# OS Wet (c) 2019 Mani Jamali. Free Software GNU General Public License version 3.0

# kernel-header.py : Kernel informations

k_header_magic = "wet"
k_header_code = "supertest"
k_header_version = "0.01"


# In the name of God, the Compassionate, the Merciful.
# OS Wet (c) 2019 Mani Jamali. Free Software GNU General Public License version 3.0

# imports_module.py : Import python modules into kernel

import sys, os, shutil, py_compile
from importlib import reload
# In the name of God, the Compassionate, the Merciful.
# OS Wet (c) 2019 Mani Jamali. Free Software GNU General Public License version 3.0

# parameters.py : Kernel parameters

def parameters (args):
    return args

params = parameters(sys.argv[1:])
# In the name of God, the Compassionate, the Merciful.
# OS Wet (c) 2019 Mani Jamali. Free Software GNU General Public License version 3.0

# sysvar.py : System variables

root = None
path = None
switch = 0
# In the name of God, the Compassionate, the Merciful.
# OS Wet (c) 2019 Mani Jamali. Free Software GNU General Public License version 3.0

# include/process_colors.py : Internal process colors in this kernel

class process_colors:
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    purple = 35
    cyan = 36
    white = 37

    style_none = 0
    style_bold = 1
    style_underline = 2
    style_negative1 = 3
    style_negative2 = 5

    bg_black = 40
    bg_red = 41
    bg_green = 42
    bg_yellow = 43
    bg_blue = 44
    bg_purple = 45
    bg_cyan = 46
    bg_white = 47

    def color (style,text,background):
        return "\033["+str(style)+";"+str(text)+";"+str(background)+"m"

    def get_colors ():
        py_compile.compile("etc/console/color","proc/color.pyc")
        from proc import color
        color = reload(color)
        style = color.style
        fgcolor = color.fgcolor
        bgcolor = color.bgcolor
        return "\033["+str(style)+";"+str(fgcolor)+";"+str(bgcolor)+"m"

    def get_style ():
        py_compile.compile("etc/console/color","proc/color.pyc")
        from proc import color
        color = reload(color)
        strv = color.style
        return strv

    def get_fgcolor ():
        py_compile.compile("etc/console/color","proc/color.pyc")
        from proc import color
        color = reload(color)
        strv = color.fgcolor
        return strv

    def get_bgcolor ():
        py_compile.compile("etc/console/color","proc/color.pyc")
        from proc import color
        color = reload(color)
        strv = color.bgcolor
        return strv

    def get_warning():
        py_compile.compile("etc/console/color", "proc/color.pyc")
        from proc import color
        color = reload(color)
        strv =  "\033[" + str(color.warning_style) + ";" + str(color.warning_fgcolor) + ";" + str(color.warning_bgcolor) + "m"
        return strv

    def get_path():
        py_compile.compile("etc/console/color", "proc/color.pyc")
        from proc import color
        color = reload(color)
        strv =  "\033[" + str(color.path_style) + ";" + str(color.path_fgcolor) + ";" + str(color.path_bgcolor) + "m"
        return strv

    def get_prompt():
        py_compile.compile("etc/console/color", "proc/color.pyc")
        from proc import color
        color = reload(color)
        strv =  "\033[" + str(color.prompt_style) + ";" + str(color.prompt_fgcolor) + ";" + str(color.prompt_bgcolor) + "m"
        return strv

    def get_fail():
        py_compile.compile("etc/console/color", "proc/color.pyc")
        from proc import color
        color = reload(color)
        strv =  "\033[" + str(color.fail_style) + ";" + str(color.fail_fgcolor) + ";" + str(color.fail_bgcolor) + "m"
        return strv

    def get_ok():
        py_compile.compile("etc/console/color", "proc/color.pyc")
        from proc import color
        color = reload(color)
        strv =  "\033[" + str(color.ok_style) + ";" + str(color.ok_fgcolor) + ";" + str(color.ok_bgcolor) + "m"
        return strv


# In the name of God, the Compassionate, the Merciful.
# OS Wet (c) 2019 Mani Jamali. Free Software GNU General Public License version 3.0

# include/process.py : Internal process library

class process:
    def show_start_process(process_name):
        if params[0]=="kernel":
            print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] Start " + process_name + " process ...")

    def show_switch_process(process_name):
        if params[0]=="kernel":
            print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] Switch " + process_name + " ...")

    def show_endswitch_process(process_name):
        if params[0] == "kernel":
            print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] End switch " + process_name + " ...")

    def show_fail_process(process_name):
        print("[" + process_colors.get_fail()   + " NO " +process_colors.get_colors() + "] Fail " + process_name + " process ...")

    def show_end_process(process_name):
        if params[0] == "kernel":
            print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] End " + process_name + " process ...")

    def show_power_on ():
        if params[0] == "kernel":
            print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] Power on the kernel ...")

    def show_stop ():
        print("[" + process_colors.get_fail()   + " NO " +process_colors.get_colors() + "] Stop the kernel ...")

    def show_power_off ():
        if params[0] == "kernel":
            print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] Power off the kernel ...")

    def show_reboot():
        if params[0] == "kernel":
            print("[" + process_colors.get_ok() + " OK " +process_colors.get_colors() + "] Reboot the kernel ...")

    def show_clean_switch(switch):
        if params[0] == "kernel":
            print("[" + process_colors.get_ok() + " OK " + process_colors.get_colors() + "] Clean switch "+switch+" ...")

    def start_ziro ():
        process.show_switch_process("/proc/switch/0")
        if not os.path.isdir ("proc/switch/0"):
            os.mkdir ("proc/switch/0")
            os.mkdir ("proc/switch/0/var")
            return 0

    def start (switch):
        process.show_switch_process("/proc/switch/"+str(switch))
        if not os.path.isdir ("proc/switch/"+str(switch)):
            os.mkdir ("proc/switch/"+str(switch))
            os.mkdir("proc/switch/"+str(switch)+"/var")

    def check (switch):
        if not os.path.isdir ("proc/switch/"+str(switch)):
            process.show_fail_process("to switch /proc/switch/"+str(switch))
            process.show_stop()
            exit()

    def end (switch):
        if os.path.isdir ("proc/switch/"+str(switch)):
            process.show_endswitch_process("/proc/switch/"+str(switch))
            shutil.rmtree("proc/switch/"+str(switch), ignore_errors=False, onerror=None)
            exit()

    def endall ():
        proclist = os.listdir("proc/switch/")
        for i in proclist:
            process.show_endswitch_process("/proc/switch/"+i)
            shutil.rmtree("proc/switch/"+i, ignore_errors=False, onerror=None)

    def kill (switch):
        if os.path.isdir ("proc/switch/"+str(switch)):
            shutil.rmtree("proc/switch/"+str(switch), ignore_errors=False, onerror=None)

    def show (process_name,process_type,process_message):
        if process_type=="fail":
            print (process_colors.get_fail()+process_name+": error: "+process_message+process_colors.get_colors())
        elif process_type=="warning":
            print (process_colors.get_warning()+process_name+": warning: "+process_message+process_colors.get_colors())

    def processer ():
        if os.path.isdir("proc/switch/0"):
            proclist = os.listdir("proc/switch/")
            nproc = int(max(proclist)) + 1
            process.start(nproc)
            return int(nproc)
        else:
            process.start_ziro()
            return 0

# In the name of God, the Compassionate, the Merciful.
# OS Wet (c) 2019 Mani Jamali. Free Software GNU General Public License version 3.0

# process/root.py : Root process

def k_root():
    process.show_start_process("root")
    if os.path.isfile("etc/root"):
        file = open("etc/root","r")
        strv = file.readline()
        file.close()
        return strv
    else:
        process.show_fail_process("root")
        process.show_stop()
        exit(0)
# In the name of God, the Compassionate, the Merciful.
# OS Wet (c) 2019 Mani Jamali. Free Software GNU General Public License version 3.0

# process/switch.py : Switch process

def k_switch():
    process.show_start_process("switch")
    switch = process.processer()
    process.check(switch)
# In the name of God, the Compassionate, the Merciful.
# OS Wet (c) 2019 Mani Jamali. Free Software GNU General Public License version 3.0

# process/init.py : Init process

def k_init ():
    process.show_power_on()
    process.show_start_process("init")
    process.show_start_process("color")

    ### process ###

    root = k_root()

    ### process ###

k_init()

