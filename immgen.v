// this file is immediate number generator for single cycle processor.
// ISA based on RV32I
// it accepts 32-bit i_inst and generates 32-bit immediate value.
// and have 2 select bits to select the type of immediate value to be generated.

//`include "definitions.v"
`default_nettype none
`timescale 1ns/1ns

module Immgen (
    input wire [2:0] i_imm_ctrl,
    input wire [`INST_WIDTH-1:0] i_inst,
    output reg [`DATA_WIDTH-1:0] o_imm
);

// I-type immediate = i_inst[31:20]
// S-type immediate = {i_inst[31:25], i_inst[11:7]}
// B-type immediate = {i_inst[31], i_inst[7], i_inst[30:25], i_inst[11:8], 1'b0}
// J-type immediate = {i_inst[31], i_inst[19:12], i_inst[20], i_inst[30:21], 1'b0}  // 20 bits
// U-type immediate = i_inst[31:12] << 12

always @* begin
    case (i_imm_ctrl)
        `IMM_I_TYPE: o_imm = {{20{i_inst[31]}}, i_inst[31:20]}; // I-type immediate
        `IMM_S_TYPE: o_imm = {{20{i_inst[31]}}, i_inst[31:25], i_inst[11:7]}; // S-type immediate
        `IMM_B_TYPE: o_imm = {{19{i_inst[31]}}, i_inst[31], i_inst[7], i_inst[30:25], i_inst[11:8], 1'b0}; // B-type immediate
        `IMM_J_TYPE: o_imm = {{11{i_inst[31]}}, i_inst[31], i_inst[19:12], i_inst[20], i_inst[30:21], 1'b0}; // J-type immediate
        `IMM_U_TYPE: o_imm = {i_inst[31:12], 12'b0}; // U-type immediate
        default: o_imm = 32'b0;
    endcase
end

endmodule