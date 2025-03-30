
PWD=$(shell pwd)
export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)


# use verilator as sim
SIM ?= verilator

# use verilog as language
TOPLEVEL_LANG ?= verilog
# to supress warnings
VERILATOR_ARGS += -Wno-WIDTHTRUNC -Wno-UNUSED -Wno-UNDRIVEN -Wno-CASEINCOMPLETE 
# source code list 
VERILOG_SOURCES = ../../definitions.v \
				 ../../alu.v \
				 ../../branch_compar.v \
				 ../../control_logic.v \
				 ../../dmem.v \
				 ../../imem.v \
				 ../../immgen.v \
				 ../../mux2.v \
				 ../../mux4.v \
				 ../../pc_adder.v \
				 ../../reg_file.v \
				 ../../top.v
#$(shell find ../../ -name "*.v")
#TOP LEVEL module

TOPLEVEL = top
# module direct to test
MODULE = top_test

# include the common Makefile
include $(shell cocotb-config --makefiles)/Makefile.sim