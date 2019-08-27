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
