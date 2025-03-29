
PWD=$(shell pwd)
export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)


# use verilator as sim
SIM ?= verilator

# use verilog as language
TOPLEVEL_LANG ?= verilog

# source code list 
VERILOG_SOURCES = ../../definitions.v \
			 	 ../../reg_file.v
#$(shell find ../../ -name "*.v")
#TOP LEVEL module

TOPLEVEL = Reg_file

# module direct to test
MODULE = reg_file_test

# include the common Makefile
include $(shell cocotb-config --makefiles)/Makefile.sim