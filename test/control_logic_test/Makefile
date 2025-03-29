
PWD=$(shell pwd)
export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)


# use verilator as sim
SIM ?= verilator

# use verilog as language
TOPLEVEL_LANG ?= verilog
# to supress warnings
VERILATOR_ARGS += -Wno-WIDTHTRUNC -Wno--CASEINCOMPLETE
# source code list 
VERILOG_SOURCES = ../../definitions.v \
				 ../../control_logic.v
#$(shell find ../../ -name "*.v")
#TOP LEVEL module

TOPLEVEL = Control_logic
# module direct to test
MODULE = control_logic_test

# include the common Makefile
include $(shell cocotb-config --makefiles)/Makefile.sim