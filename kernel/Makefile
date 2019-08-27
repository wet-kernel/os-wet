# In the name of God, the Compassionate, the Merciful.
# OS Wet (c) 2019 Mani Jamali. Free Software GNU General Public License version 3.0

# Makefile : Kernel builder

# Path to install:
PREFIX=../stor


# Run `$ make build` for build the kernel

build:
	@echo -n "Building the kernel ... "
	@python3 install.py
	@echo "done"

# Run `$ make clean` for clean cache

clean:
	@echo -n "Cleaning the cache ... "
	@rm jobs/* vmwet.py vmwet
	@> vmwet.py
	@echo "done"

# Run `$ make install` for install the kernel

install:
	@echo -n "Installing the kernel ... "
	@cp vmwet ${PREFIX}/vmwet
	@echo "done"

# Run `$ make run` for run the kernel

run:
	@echo "Runing the kernel ... done"
	@cd ${PREFIX} && ./run.sh kernel

# Run `$ make all`

all:
	@make clean
	@make
	@make install
	@make run
