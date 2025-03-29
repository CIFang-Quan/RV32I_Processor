# cocotb test for br_cmp

import cocotb 
from cocotb.triggers import Timer

# module Brcmptop (
#     input wire [`DATA_WIDTH-1:0] i_rs1,
#     input wire [`DATA_WIDTH-1:0] i_rs2,
#     input wire i_brun, //0 signed, 1 unsigned
#     output wire o_breq, // 0 not equal, 1 equal
#     output wire o_brlt  // 0 not less than, 1 less than
#     // output wire o_bge  // 0 not greater | equal than, 1 greater | equal than
# );

@cocotb.test()
async def test_br_cmp_signed(dut):
    """Test Branch Comparator"""
    # Set inputs
    dut.i_rs1.value = 0b11111111111111111111111111111101
    dut.i_rs2.value = 0b11111111111111111111111111111000
    dut.i_brun = 0
    await Timer(1, units='ns')
    # Check output
    expected_val_1 = 0
    assert dut.o_breq.value == expected_val_1, (
        f"br_cmp={dut.o_breq.value}, expected={expected_val_1}"
    )
    expected_val_2 = 0
    assert dut.o_brlt.value == expected_val_2, (
        f"br_cmp={dut.o_brlt.value}, expected={expected_val_2}"
    )

# @cocotb.test()
# async def test_br_cmp_unsigned(dut):
#     """Test Branch Comparator"""
#     # Set inputs
#     dut.rs1.value = 0b01111111111111111111111111111111
#     dut.rs2.value = 0b11111111111111111111111111111111
#     dut.unsigned_cmp = 1
#     await Timer(1, units='ns')
#     # Check output
#     expected_val_1 = 0
#     assert dut.breq.value == expected_val_1, (
#         f"br_cmp={dut.breq.value}, expected={expected_val_1}"
#     )
#     expected_val_2 = 1
#     assert dut.brlt.value == expected_val_2, (
#         f"br_cmp={dut.brlt.value}, expected={expected_val_2}"
#     )

# @cocotb.test()
# async def test_br_cmp_unsigned_2(dut):
#     """Test Branch Comparator"""
#     # Set inputs
#     dut.rs1.value = 0b01111111111111111111111111111111
#     dut.rs2.value = 0b01111111111111111111111111111111
#     dut.unsigned_cmp = 1
#     await Timer(1, units='ns')
#     # Check output  
#     expected_val_1 = 1
#     assert dut.breq.value == expected_val_1, (
#         f"br_cmp={dut.breq.value}, expected={expected_val_1}"
#     )
#     expected_val_2 = 0
#     assert dut.brlt.value == expected_val_2, (
#         f"br_cmp={dut.brlt.value}, expected={expected_val_2}"
#     )
