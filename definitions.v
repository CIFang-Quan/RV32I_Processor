`ifndef DEFINITIONS_VH
`define DEFINITIONS_VH

// Width definitions
`define DATA_WIDTH 32
`define ADDR_WIDTH 32
`define INST_WIDTH 32
`define NUM_REGISTER 32

`define DMEM_SIZE `DATA_WIDTH*(2^`ADDR_WIDTH) // 2^32 bytes
`define IMEM_SIZE `INST_WIDTH*(2^`DATA_WIDTH) // 2^32 bytes

`define FUNCT_3 3
`define FUNCT_7 7

// RISC-V Base Instruction Set Opcodes
`define OPCODE 7
`define OP_LUI     7'b0110111 // Load Upper Immediate
`define OP_AUIPC   7'b0010111 // Add Upper Immediate to PC
`define OP_JAL     7'b1101111 // Jump and Link
`define OP_JALR    7'b1100111 // Jump and Link Register
`define OP_BRANCH  7'b1100011 // Branch Instructions (BEQ, BNE, BLT, etc.)
`define OP_LOAD    7'b0000011 // Load Instructions (LB, LH, LW, LBU, LHU)
`define OP_STORE   7'b0100011 // Store Instructions (SB, SH, SW)
`define OP_ALU     7'b0110011 // ALU Instructions (ADD, SUB, AND, OR, XOR, etc.)
`define OP_ALUI    7'b0010011 // ALU Immediate Instructions (ADDI, ANDI, ORI, XORI, etc.)
`define OP_FENCE   7'b0001111 // Fence
`define OP_SYSTEM  7'b1110011 // System Instructions (ECALL, EBREAK, SCR, etc.)


`define OP_ALU_NOP    4'b0000 
`define OP_ALU_ADD    4'b0001 // Add
`define OP_ALU_SUB    4'b0010 // Subtract
`define OP_ALU_AND    4'b0011 // Bitwise AND
`define OP_ALU_OR     4'b0100 // Bitwise OR
`define OP_ALU_XOR    4'b0101 // Bitwise XOR
`define OP_ALU_NOR    4'b0110 // Bitwise NOR
`define OP_ALU_SLL    4'b0111 // Shift Left Logical
`define OP_ALU_SRL    4'b1000 // Shift Right Logical
`define OP_ALU_SRA    4'b1001 // Shift Right Arithmetic
`define OP_ALU_SLT    4'b1010 // Set Less Than (signed)
`define OP_ALU_SLTU   4'b1011 // Set Less Than (unsigned)


`define IMM_NOP            3'b000 // U-type immediate
`define IMM_I_TYPE         3'b001 // I-type immediate
`define IMM_S_TYPE         3'b010 // S-type immediate
`define IMM_B_TYPE         3'b011 // B-type immediate
`define IMM_J_TYPE         3'b100 // J-type immediate
`define IMM_U_TYPE         3'b101 // U-type immediate

`endif