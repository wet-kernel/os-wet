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