#cocotb test immgen 

import cocotb
from cocotb.triggers import Timer

# module Immgen (
#     input wire [2:0] i_imm_ctrl,
#     input wire [`INST_WIDTH-1:0] i_inst,
#     output reg [`DATA_WIDTH-1:0] o_imm
# );

@cocotb.test()
async def test_Itype(dut):
    """Test I-type instruction"""
    # assgin a I-type instruction with random immediate value and set rs1 func3 rd opcode all 0 
    # since we only test immgen
    # rs1 in I-type instruction is 19-15
    # func3 in I-type instruction is 14-12
    # rd in I-type instruction is 11-7
    # opcode in I-type instruction is 6-0

    dut.i_inst.value = 0

    dut.i_inst.value = dut.i_inst.value | (0xAAA << 20)

    dut.i_imm_ctrl = 1
    await Timer(1, units='ns')

    expected_val = 0xFFFFFAAA
    assert dut.o_imm.value == expected_val, (
        f"imm={dut.o_imm.value}, expected={hex(expected_val)}"
    )

# @cocotb.test()
# async def test_Btype(dut):
#     """Test B-type instruction"""

#     dut.instruction.value = 0

#     dut.instruction.value = dut.instruction.value | 0xFE000F80

#     dut.imm_select.value = 0x2
#     await Timer(1, units='ns')

#     expected_val = 0xFFFFFFFE
#     assert dut.imm.value == expected_val, (
#         f"imm={dut.imm.value}, expected={hex(expected_val)}"
#     )

# @cocotb.test()
# async def test_Stype(dut):
#     """Test S-type instruction"""

#     dut.instruction.value = 0

#     dut.instruction.value = dut.instruction.value | 0xFE000F80
#     dut.imm_select.value = 0x1

#     await Timer(1, units='ns')

#     expected_val = 0xFFFFFFFF
#     assert dut.imm.value == expected_val, (
#         f"imm={dut.imm.value}, expected={hex(expected_val)}"
#     )

# @cocotb.test()
# async def test_Jtype(dut):
#     """Test J-type instruction"""

#     dut.instruction.value = 0

#     dut.instruction.value = dut.instruction.value | 0xFFFFF000
#     dut.imm_select.value = 0x3

#     await Timer(1, units='ns')

#     expected_val = 0xFFFFFFFE
#     assert dut.imm.value == expected_val, (
#         f"imm={dut.imm.value}, expected={hex(expected_val)}"
#     )

# @cocotb.test()
# async def test_Utype(dut):
#     """Test U-type instruction"""

#     dut.instruction.value = 0

#     dut.instruction.value = dut.instruction.value | 0xFFFFF000
#     dut.imm_select.value = 0x4

#     await Timer(1, units='ns')

#     expected_val = 0xFFFFF000
#     assert dut.imm.value == expected_val, (
#         f"imm={dut.imm.value}, expected={hex(expected_val)}"
#     )