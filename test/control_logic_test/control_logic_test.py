# cocotb test for control logic module

import cocotb
from cocotb.triggers import Timer

# module Control_logic (
#     input wire [31:0] i_inst,
#     input wire i_breq,
#     input wire i_brlt,
#     output reg o_pcsel,
#     output reg o_reg_w,
#     output reg [2:0] o_imm_sel,
#     output reg o_op1_sel,
#     output reg o_op2_sel,
#     output reg o_brun,
#     output reg [3:0] o_alu_ctrl,
#     output reg o_mem_r,
#     output reg o_mem_w,
#     output reg [1:0] o_wb_sel
# );

@cocotb.test()
async def test_J_type(dut):
    """Test control logic for J-type instruction"""
    dut.i_inst.value =0x6F #opcode for JAL other bit set 0
    await Timer(1, units='ns')
    expected_val = (
        0b1,#o_pcsel
        0b1,#o_op1_sel
        0b0,#o_op2_sel
        0b1,#o_reg_w
        0b100,#o_imm_sel
        0b0,#o_mem_r
        0b0,#o_mem_w
        0b10,#o_wb_sel
        0b0001#o_alu_ctrl
        )
    temp_tuple =(
        dut.o_pcsel.value,
        dut.o_op1_sel.value,
        dut.o_op2_sel.value,
        dut.o_reg_w.value,
        dut.o_imm_sel.value,
        dut.o_mem_r.value,
        dut.o_mem_w.value,
        dut.o_wb_sel.value,
        dut.o_alu_ctrl.value
    )
    await Timer(1, units='ns')
    dut._log.info(f"i_pcsel={temp_tuple[0]}\n"
                f"i_op1_sel={temp_tuple[1]}\n"
                f"i_op2_sel={temp_tuple[2]}\n"
                f"i_reg_w={temp_tuple[3]}\n"
                f"i_imm_sel={temp_tuple[4]}\n"
                f"i_mem_w={temp_tuple[5]}\n"
                f"i_mem_r={temp_tuple[6]}\n"
                f"i_wb_sel={temp_tuple[7]}\n"
                f"i_alu_ctrl={temp_tuple[8]}")
    assert  temp_tuple == expected_val, (
        f"control logic={temp_tuple}, expected={expected_val}"
    )

# @cocotb.test()
# async def test_I_type_JALR(dut):
#     """Test control logic for I-type instruction"""
#     dut.instruction.value =0x67 #opcode for JALR other bit set 0
#     await Timer(1, units='ns')
#     # Check output
#     # expected_val is a tuple of all the output values
#     expected_val = (
#         0b1,#pcsel
#         0b0,#operand1_sel
#         0b0,#operand2_sel
#         0b1,#reg_write
#         0b000,#immgen_sel
#         0b0,#dmem_read
#         0b0,#dmem_write
#         0b0,#brunsigned
#         0b00,#writeback_sel
#         0b0000#alu_op
#         )
#     temp_tuple =(
#         dut.pcsel.value,
#         dut.operand1_sel.value,
#         dut.operand2_sel.value,
#         dut.reg_write.value,
#         dut.immgen_sel.value,
#         dut.dmem_write.value,
#         dut.dmem_read.value,
#         dut.brunsigned.value,
#         dut.writeback_sel.value,
#         dut.alu_op.value,
#     )

#     await Timer(1, units='ns')
#     dut._log.info(f"pcsel={temp_tuple[0]}\n"
#               f"operand1_sel={temp_tuple[1]}\n"
#               f"operand2_sel={temp_tuple[2]}\n"
#               f"reg_write={temp_tuple[3]}\n"
#               f"immgen_sel={temp_tuple[4]}\n"
#               f"dmem_write={temp_tuple[5]}\n"
#               f"dmem_read={temp_tuple[6]}\n"
#               f"brunsigned={temp_tuple[7]}\n"
#               f"writeback_sel={temp_tuple[8]}\n"
#               f"alu_op={temp_tuple[9]}")
#     assert  temp_tuple == expected_val, (
#         f"control logic={temp_tuple}, expected={expected_val}"
#     )

# @cocotb.test()
# async def test_I_type_LW(dut):
#     """Test control logic for I-type instruction"""
#     dut.instruction.value =0x03
#     await Timer(1, units='ns')
#     # Check output
#     # expected_val is a tuple of all the output values
#     expected_val = (
#         0b0,#pcsel
#         0b0,#operand1_sel
#         0b0,#operand2_sel
#         0b1,#reg_write
#         0b000,#immgen_sel
#         0b0,#dmem_write
#         0b1,#dmem_read
#         0b0,#brunsigned
#         0b01,#writeback_sel
#         0b0000#alu_op
#         )
#     temp_tuple =(
#         dut.pcsel.value,
#         dut.operand1_sel.value,
#         dut.operand2_sel.value,
#         dut.reg_write.value,
#         dut.immgen_sel.value,
#         dut.dmem_write.value,
#         dut.dmem_read.value,
#         dut.brunsigned.value,
#         dut.writeback_sel.value,
#         dut.alu_op.value,
#     )
#     await Timer(1, units='ns')
#     dut._log.info(f"pcsel={temp_tuple[0]}\n"
#               f"operand1_sel={temp_tuple[1]}\n"
#               f"operand2_sel={temp_tuple[2]}\n"
#               f"reg_write={temp_tuple[3]}\n"
#               f"immgen_sel={temp_tuple[4]}\n"
#               f"dmem_write={temp_tuple[5]}\n"
#               f"dmem_read={temp_tuple[6]}\n"
#               f"brunsigned={temp_tuple[7]}\n"
#               f"writeback_sel={temp_tuple[8]}\n"
#               f"alu_op={temp_tuple[9]}")
#     assert  temp_tuple == expected_val, (
#         f"control logic={temp_tuple}, expected={expected_val}"
#     )

# @cocotb.test()
# async def test_S_type_SW(dut):
#     """Test control logic for S-type instruction"""
#     dut.instruction.value =0x23
#     await Timer(1, units='ns')
#     # Check output
#     # expected_val is a tuple of all the output values
#     expected_val = (
#         0b0,#pcsel
#         0b0,#operand1_sel
#         0b0,#operand2_sel
#         0b0,#reg_write
#         0b001,#immgen_sel
#         0b1,#dmem_write
#         0b0,#dmem_read
#         0b0,#brunsigned
#         0b11,#writeback_sel
#         0b0000#alu_op
#         )
#     temp_tuple =(
#         dut.pcsel.value,
#         dut.operand1_sel.value,
#         dut.operand2_sel.value,
#         dut.reg_write.value,
#         dut.immgen_sel.value,
#         dut.dmem_write.value,
#         dut.dmem_read.value,
#         dut.brunsigned.value,
#         dut.writeback_sel.value,
#         dut.alu_op.value,
#     )
#     await Timer(1, units='ns')
#     dut._log.info(f"pcsel={temp_tuple[0]}\n"
#               f"operand1_sel={temp_tuple[1]}\n"
#               f"operand2_sel={temp_tuple[2]}\n"
#               f"reg_write={temp_tuple[3]}\n"
#               f"immgen_sel={temp_tuple[4]}\n"
#               f"dmem_write={temp_tuple[5]}\n"
#               f"dmem_read={temp_tuple[6]}\n"
#               f"brunsigned={temp_tuple[7]}\n"
#               f"writeback_sel={temp_tuple[8]}\n"
#               f"alu_op={temp_tuple[9]}")
#     assert  temp_tuple == expected_val, (
#         f"control logic={temp_tuple}, expected={expected_val}"
#     )
# @cocotb.test()
# async def test_B_type_BEQ_jump(dut):
#     """Test control logic for B-type instruction"""
#     dut.instruction.value =0x63
#     dut.breq.value = 1
#     await Timer(1, units='ns')
#     # Check output
#     # expected_val is a tuple of all the output values
#     expected_val = (
#         0b1,#pcsel
#         0b1,#operand1_sel
#         0b0,#operand2_sel
#         0b0,#reg_write
#         0b010,#immgen_sel
#         0b0,#dmem_read
#         0b0,#dmem_write
#         0b0,#brunsigned
#         0b11,#writeback_sel
#         0b0000#alu_op
#         )
#     temp_tuple =(
#         dut.pcsel.value,
#         dut.operand1_sel.value,
#         dut.operand2_sel.value,
#         dut.reg_write.value,
#         dut.immgen_sel.value,
#         dut.dmem_write.value,
#         dut.dmem_read.value,
#         dut.brunsigned.value,
#         dut.writeback_sel.value,
#         dut.alu_op.value,
#     )
#     await Timer(1, units='ns')
#     dut._log.info(f"pcsel={temp_tuple[0]}/n\
#                     operand1_sel={temp_tuple[1]}/n\
#                     operand2_sel={temp_tuple[2]}/n\
#                     reg_write={temp_tuple[3]}\/n\
#                     immgen_sel={temp_tuple[4]}/n\
#                     dmem_write={temp_tuple[5]}/n\
#                     dmem_read={temp_tuple[6]}/n\
#                     brunsigned={temp_tuple[7]}/n\
#                     writeback_sel={temp_tuple[8]}/n\
#                     alu_op={temp_tuple[9]}")
#     assert  temp_tuple == expected_val, (
#         f"control logic={temp_tuple}, expected={expected_val}"
#     )
# @cocotb.test()
# async def test_B_type_BEQ_Njump(dut):
#     """Test control logic for B-type instruction"""
#     dut.instruction.value =0x63
#     dut.breq.value = 0
#     await Timer(1, units='ns')
#     # Check output
#     # expected_val is a tuple of all the output values
#     expected_val = (
#         0b0,#pcsel
#         0b1,#operand1_sel
#         0b0,#operand2_sel
#         0b0,#reg_write
#         0b010,#immgen_sel
#         0b0,#dmem_read
#         0b0,#dmem_write
#         0b0,#brunsigned
#         0b11,#writeback_sel
#         0b0000#alu_op
#         )
#     temp_tuple =(
#         dut.pcsel.value,
#         dut.operand1_sel.value,
#         dut.operand2_sel.value,
#         dut.reg_write.value,
#         dut.immgen_sel.value,
#         dut.dmem_write.value,
#         dut.dmem_read.value,
#         dut.brunsigned.value,
#         dut.writeback_sel.value,
#         dut.alu_op.value,
#     )
#     await Timer(1, units='ns')
#     dut._log.info(f"pcsel={temp_tuple[0]}\n"
#               f"operand1_sel={temp_tuple[1]}\n"
#               f"operand2_sel={temp_tuple[2]}\n"
#               f"reg_write={temp_tuple[3]}\n"
#               f"immgen_sel={temp_tuple[4]}\n"
#               f"dmem_write={temp_tuple[5]}\n"
#               f"dmem_read={temp_tuple[6]}\n"
#               f"brunsigned={temp_tuple[7]}\n"
#               f"writeback_sel={temp_tuple[8]}\n"
#               f"alu_op={temp_tuple[9]}")
#     assert  temp_tuple == expected_val, (
#         f"control logic={temp_tuple}, expected={expected_val}"
#     )
# @cocotb.test()
# async def test_R_type_ADD(dut):
#     """Test control logic for R-type instruction"""
#     dut.instruction.value =0x33
#     await Timer(1, units='ns')
#     # Check output
#     # expected_val is a tuple of all the output values
#     expected_val = (
#         0b0,#pcsel
#         0b0,#operand1_sel
#         0b1,#operand2_sel
#         0b1,#reg_write
#         0b111,#immgen_sel
#         0b0,#dmem_read
#         0b0,#dmem_write
#         0b0,#brunsigned
#         0b10,#writeback_sel
#         0b0000#alu_op
#         )
#     temp_tuple =(
#         dut.pcsel.value,
#         dut.operand1_sel.value,
#         dut.operand2_sel.value,
#         dut.reg_write.value,
#         dut.immgen_sel.value,
#         dut.dmem_write.value,
#         dut.dmem_read.value,
#         dut.brunsigned.value,
#         dut.writeback_sel.value,
#         dut.alu_op.value,
#     )
#     await Timer(1, units='ns')
#     dut._log.info(f"pcsel={temp_tuple[0]}\n"
#               f"operand1_sel={temp_tuple[1]}\n"
#               f"operand2_sel={temp_tuple[2]}\n"
#               f"reg_write={temp_tuple[3]}\n"
#               f"immgen_sel={temp_tuple[4]}\n"
#               f"dmem_write={temp_tuple[5]}\n"
#               f"dmem_read={temp_tuple[6]}\n"
#               f"brunsigned={temp_tuple[7]}\n"
#               f"writeback_sel={temp_tuple[8]}\n"
#               f"alu_op={temp_tuple[9]}")
#     assert  temp_tuple == expected_val, (
#         f"control logic={temp_tuple}, expected={expected_val}"
#     )
# @cocotb.test()
# async def test_R_type_SUB(dut):
#     """Test control logic for R-type instruction"""
#     dut.instruction.value =0x40000033
#     await Timer(1, units='ns')
#     # Check output
#     # expected_val is a tuple of all the output values
#     expected_val = (
#         0b0,#pcsel
#         0b0,#operand1_sel
#         0b1,#operand2_sel
#         0b1,#reg_write
#         0b111,#immgen_sel
#         0b0,#dmem_read
#         0b0,#dmem_write
#         0b0,#brunsigned
#         0b10,#writeback_sel
#         0b0001#alu_op
#         )
#     temp_tuple =(
#         dut.pcsel.value,
#         dut.operand1_sel.value,
#         dut.operand2_sel.value,
#         dut.reg_write.value,
#         dut.immgen_sel.value,
#         dut.dmem_write.value,
#         dut.dmem_read.value,
#         dut.brunsigned.value,
#         dut.writeback_sel.value,
#         dut.alu_op.value,
#     )
#     await Timer(1, units='ns')
#     dut._log.info(f"pcsel={temp_tuple[0]}\n"
#               f"operand1_sel={temp_tuple[1]}\n"
#               f"operand2_sel={temp_tuple[2]}\n"
#               f"reg_write={temp_tuple[3]}\n"
#               f"immgen_sel={temp_tuple[4]}\n"
#               f"dmem_write={temp_tuple[5]}\n"
#               f"dmem_read={temp_tuple[6]}\n"
#               f"brunsigned={temp_tuple[7]}\n"
#               f"writeback_sel={temp_tuple[8]}\n"
#               f"alu_op={temp_tuple[9]}")
#     assert  temp_tuple == expected_val, (
#         f"control logic={temp_tuple}, expected={expected_val}"
#     )