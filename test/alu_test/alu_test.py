# cocotb test for alu

import cocotb
from cocotb.triggers import Timer
# alu_control is a 4-bit control signal
# `define OP_ALU_NOP    4'b0000 
# `define OP_ALU_ADD    4'b0001 // Add
# `define OP_ALU_SUB    4'b0010 // Subtract
# `define OP_ALU_AND    4'b0011 // Bitwise AND
# `define OP_ALU_OR     4'b0100 // Bitwise OR
# `define OP_ALU_XOR    4'b0101 // Bitwise XOR
# `define OP_ALU_NOR    4'b0110 // Bitwise NOR
# `define OP_ALU_SLL    4'b0111 // Shift Left Logical
# `define OP_ALU_SRL    4'b1000 // Shift Right Logical
# `define OP_ALU_SRA    4'b1001 // Shift Right Arithmetic
# `define OP_ALU_SLT    4'b1010 // Set Less Than (signed)
# `define OP_ALU_SLTU   4'b1011 // Set Less Than (unsigned)

# module Alu (
#     input wire [3:0] i_alu_ctrl,
#     input wire [`DATA_WIDTH:0] i_a,
#     input wire [`DATA_WIDTH:0] i_b,
#     output reg [`DATA_WIDTH:0] o_res
# );
@cocotb.test()
async def test_alu_add(dut):
    """Test ALU ADD operation"""
    # Set inputs
    dut.i_alu_ctrl.value = 1
    dut.i_a.value = 5
    dut.i_b.value = 3
    await Timer(1, units='ns')
    # Check output
    expected_val = 8
    assert dut.o_res.value == expected_val, (
        f"result={dut.o_res.value}, expected={expected_val}"
    )

# @cocotb.test()
# async def test_alu_sub(dut):
#     """Test ALU SUB operation"""
#     # Set inputs
#     dut.alu_control.value = 1
#     dut.a.value = 5
#     dut.b.value = 3
#     await Timer(1, units='ns')
#     # Check output
#     expected_val = 2
#     assert dut.result.value == expected_val, (
#         f"result={dut.result.value}, expected={expected_val}"
#     )

# @cocotb.test()
# async def test_alu_and(dut):
#     """Test ALU AND operation"""
#     # Set inputs
#     dut.alu_control.value = 2
#     dut.a.value = 5
#     dut.b.value = 3
#     await Timer(1, units='ns')
#     # Check output
#     expected_val = 1
#     assert dut.result.value == expected_val, (
#         f"result={dut.result.value}, expected={expected_val}"
#     )

# @cocotb.test()
# async def test_alu_or(dut):
#     """Test ALU OR operation"""
#     # Set inputs
#     dut.alu_control.value = 3
#     dut.a.value = 5
#     dut.b.value = 3
#     await Timer(1, units='ns')
#     # Check output
#     expected_val = 7
#     dut._log.info(f"result={hex(dut.result.value)}, expected={hex(expected_val)}")
#     assert dut.result.value == expected_val, (
#         f"result={dut.result.value}, expected={expected_val}"
#     )

# @cocotb.test()
# async def test_alu_xor(dut):
#     """Test ALU XOR operation"""
#     # Set inputs
#     dut.alu_control.value = 4
#     dut.a.value = 5
#     dut.b.value = 3
#     await Timer(1, units='ns')
#     # Check output
#     expected_val = 6
#     dut._log.info(f"result={dut.result.value}, expected={hex(expected_val)}")
#     assert dut.result.value == expected_val, (
#         f"result={dut.result.value}, expected={expected_val}"
#     )

# @cocotb.test()
# async def test_alu_nor(dut):
#     """Test ALU NOR operation"""
#     # Set inputs
#     dut.alu_control.value = 5
#     dut.a.value = 5
#     dut.b.value = 3
#     await Timer(1, units='ns')
#     # Check output
#     #-8 2's complement
#     expected_val = '11111111111111111111111111111000' 
#     assert dut.result.value == expected_val, (
#         f"result={dut.result.value}, expected={expected_val}"
#     )

# @cocotb.test()
# async def test_alu_sll(dut):
#     """Test ALU SLL operation"""
#     # Set inputs
#     dut.alu_control.value = 6
#     dut.a.value = 5
#     dut.b.value = 1
#     await Timer(1, units='ns')
#     # Check output
#     expected_val = 10
#     assert dut.result.value == expected_val, (
#         f"result={dut.result.value}, expected={expected_val}"
#     )

# @cocotb.test()
# async def test_alu_srl(dut):
#     """Test ALU SRL operation"""
#     # Set inputs
#     dut.alu_control.value = 7
#     dut.a.value = 5
#     dut.b.value = 1
#     await Timer(1, units='ns')
#     # Check output
#     expected_val = 2
#     assert dut.result.value == expected_val, (
#         f"result={dut.result.value}, expected={expected_val}"
#     )

# @cocotb.test()
# async def test_alu_sra(dut):
#     """Test ALU SRA operation"""
#     # Set inputs
#     dut.alu_control.value = 8
#     dut.a.value = -5
#     dut.b.value = 1
#     await Timer(1, units='ns')
#     # Check output
#     expected_val = '11111111111111111111111111111101'
#     assert dut.result.value == expected_val, (
#         f"result={dut.result.value}, expected={expected_val}"
#     )

# @cocotb.test()
# async def test_alu_slt1(dut):
#     """Test ALU SLT operation"""
#     # Set inputs
#     dut.alu_control.value = 9
#     dut.a.value = 5
#     dut.b.value = 3
#     await Timer(1, units='ns')
#     # Check output
#     expected_val = 0
#     assert dut.result.value == expected_val, (
#         f"result={dut.result.value}, expected={expected_val}"
#     )
# @cocotb.test()
# async def test_alu_slt2(dut):
#     """Test ALU SLT operation"""
#     # Set inputs
#     dut.alu_control.value = 9
#     dut.a.value = 3
#     dut.b.value = 5
#     await Timer(1, units='ns')
#     # Check output
#     expected_val = 0x1
#     assert dut.result.value == expected_val, (
#         f"result={dut.result.value}, expected={expected_val}"
#     )
# @cocotb.test()
# async def test_alu_sltu1(dut):
#     """Test ALU SLTU operation"""
#     # Set inputs
#     dut.alu_control.value = 10
#     dut.a.value = 3
#     dut.b.value = 5
#     await Timer(1, units='ns')
#     # Check output
#     expected_val = 0x1
#     assert dut.result.value == expected_val, (
#         f"result={dut.result.value}, expected={expected_val}"
#     )
# @cocotb.test()
# async def test_alu_sltu2(dut):
#     """Test ALU SLTU operation"""
#     # Set inputs
#     dut.alu_control.value = 10
#     dut.a.value = 5
#     dut.b.value = 3
#     await Timer(1, units='ns')
#     # Check output
#     expected_val = 0
#     assert dut.result.value == expected_val, (
#         f"result={dut.result.value}, expected={expected_val}"
#     )
# # Add more tests as needed for other ALU operations