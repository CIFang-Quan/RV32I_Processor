// this file is for ALU 
// ALU is a arithmetic logic unit
// it support add, sub, and, or, xor, nor,
//             sll, srl, sra, slt, sltu operation

//`include "definitions.v"
`default_nettype none
`timescale 1ns/1ns

module Alu (
    input wire [3:0] i_alu_ctrl,
    input wire [`DATA_WIDTH-1:0] i_a,
    input wire [`DATA_WIDTH-1:0] i_b,
    output reg [`DATA_WIDTH-1:0] o_res
);
    
    always @* begin
        case (i_alu_ctrl)
            `OP_ALU_ADD: o_res = i_a + i_b; // add
            `OP_ALU_SUB: o_res = i_a - i_b; // sub
            `OP_ALU_AND: o_res = i_a & i_b; // and
            `OP_ALU_OR: o_res = i_a | i_b; // or
            `OP_ALU_XOR: o_res = i_a ^ i_b; // xor
            `OP_ALU_NOR: o_res = ~(i_a | i_b); // nor
            `OP_ALU_SLL: o_res = i_a << i_b[4:0]; // sll
            `OP_ALU_SRL: o_res = i_a >> i_b[4:0]; // srl
            `OP_ALU_SRA: o_res = $signed(i_a) >>> i_b[4:0]; // sra
            `OP_ALU_SLT: o_res = ($signed(i_a) < $signed(i_b)) ? 32'b1 : 32'b0; // slt (signed)
            `OP_ALU_SLTU: o_res = (i_a < i_b) ? 32'b1 : 32'b0; // sltu (unsigned)
            default: o_res = 32'b0; // default case
        endcase
    end
    
endmodule