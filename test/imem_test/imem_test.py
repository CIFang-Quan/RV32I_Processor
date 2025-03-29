# cocotb test for imem_test.py

import cocotb
from cocotb.triggers import Timer

# module Imem (
#     input wire [`ADDR_WIDTH-1:0] i_pc,
#     output wire [`INST_WIDTH-1:0] o_inst
#     // output reg [`INST_WIDTH-1:0] o_inst
# );

@cocotb.test()
async def test_Imem(dut):
    """Test Instruction Memory"""
    # load instruction from instructions.txt
    # instructions
    Ins= [
        0x00a00513,
        0x00a00593,
        0x008000ef,
        0x000000ef,
        0x04050c63,
        0x04058a63,
        0x00634333,
        0x0073c3b3, 
        0x00a04663,
        0x00100313,
        0x40a00533,
        0x00b04663,
        0x00100393,
        0x40b005b3,
        0x00a5c663,
        0x00050293,
        0x00000663,
        0x00058293,
        0x00050593,
        0x00a54533,
        0x00b50533,
        0xfff28293,
        0xfe029ce3,
        0x00730463,
        0x40a00533,
        0x00008067,
        0x00a54533,
        0x00008067
    ]
    # load instruction into instruction memory
    # dut.pc.value = 0
    # await Timer(100, units='ns')
    # for i in range(28):
    #     dut.pc.value = i*4
    #     await Timer(1, units='ns')
    #     assert dut.instruction.value.integer == Ins[i], (
    #         f"instruction={hex(dut.instruction.value)}, expected={hex(0x00a00513)}"
    #     )
    #     await Timer(1, units='ns')

    for i in range(0,28):
        # Set PC value
        dut.i_pc.value = i*4
        # Wait longer for signals to propagate
        await Timer(10, units='ns')
        
        # Debug print to see what's happening
        dut._log.info(f"PC={hex(dut.i_pc.value.integer)}, instruction={hex(dut.o_inst.value.integer)}")
        
        # Check assertion
        assert dut.o_inst.value.integer == Ins[i], (
            f"instruction={hex(dut.o_inst.value.integer)}, expected={hex(Ins[i])}, iteration={i}"
        )
        # !!!!!!!!!!!!! 
        # remember instructions should contain an empty row at the end !!!!!!!!!
        # !!!!!!!!!!!!!