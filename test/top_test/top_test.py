# cocotb test for top_test.py

import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.result import TestFailure

# module top(
#     input wire clk,
#     input wire rst,
#     output wire [`DATA_WIDTH-1:0] debug
# );

import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.result import TestFailure


@cocotb.test()
async def test_fibonacci5(dut):
    """Test top module running fibonacci5"""

    dut._log.info("==== Fibonacci Test Start ====")

    dut.clk.value = 0
    dut.rst.value = 1


    async def clk_gen():
        while True:
            dut.clk.value = 0
            await Timer(5, units="ns")
            dut.clk.value = 1
            await Timer(5, units="ns")
    cocotb.start_soon(clk_gen())

    await RisingEdge(dut.clk)
    dut.rst.value = 0

    reg_names = [
        "zero", "ra", "sp", "gp\n", "tp", "t0", "t1", "t2\n",
        "s0", "s1", "a0", "a1\n", "a2", "a3", "a4", "a5\n",
        "a6", "a7", "s2", "s3\n", "s4", "s5", "s6", "s7\n",
        "s8", "s9", "s10", "s11\n", "t3", "t4", "t5", "t6\n"
    ]

    for cycle in range(2000):
        await RisingEdge(dut.clk)

        pc_val = dut.pc_out.value.integer
        dut._log.info(f"[Cycle {cycle:04}] PC = 0x{pc_val:08x}")

        reg_vals = []
        for i in range(32):
            reg = dut.regs[i].value.signed_integer
            reg_vals.append(reg)
        reg_line = "  ".join([f"{reg_names[i]}=0x{reg_vals[i]:08x}" for i in range(32)])
        dut._log.info("  " + reg_line)

        if dut.debug_valid.value == 0x00000073:
            a0_val = dut.debug.value.integer
            dut._log.info(f"[Done] Program ended with a0 = {a0_val}")
            assert a0_val == 5, f"Expected Fibonacci(5) == 5, got {a0_val}"
            return

    raise TestFailure("Timeout: Fibonacci(5) did not complete.")


