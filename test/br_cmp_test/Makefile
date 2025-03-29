
PWD=$(shell pwd)
export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)


# use verilator as sim
SIM ?= verilator

# use verilog as language
TOPLEVEL_LANG ?= verilog
# to supress warnings
VERILATOR_ARGS += -Wno-WIDTHTRUNC
# source code list 
VERILOG_SOURCES = ../../definitions.v \
				 ../../branch_compar.v
#$(shell find ../../ -name "*.v")
#TOP LEVEL module

TOPLEVEL = Brcmptop
# module direct to test
MODULE = br_cmp_test

# include the common Makefile
include $(shell cocotb-config --makefiles)/Makefile.sim