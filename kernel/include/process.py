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
