// this file is Imem 
// Imem is a memory that stores the instructions
// It only supports read operation

//`include "definitions.v"
`default_nettype none
`timescale 1ns/1ns

module Imem (
    input wire [`DATA_WIDTH-1:0] i_pc,
    // output wire [`INST_WIDTH-1:0] o_inst
    output reg [`INST_WIDTH-1:0] o_inst
);
    // initialize a constant memory(reg array) to store the instructions
    // use readmemh to read the instructions from the file
    
    // just for test purpose
    reg [`INST_WIDTH-1:0] mem[0:1023];
    // reg [`INST_WIDTH-1:0] mem[0:(1<<(`DATA_WIDTH-2))-1]; // 2^32 byte
    
    // for test purpose, we only have 64 instructions
    initial begin
        $readmemh("instructions.txt", mem);
        //$display("Mem[0] = %h", mem[0]);
    end

    // just for test purpose
    // assign o_inst = mem[i_pc >> 2];

    always @(i_pc) begin
        o_inst = mem[i_pc >> 2];
    end

    // each time pc change we will read the instruction from the memory
    // can ignore the last two bits of pc
    // since the instructions are 32 bits/4 bytes
    // we will only use the first 30 bits of pc to access the memory

    // debug info
    //     always @(pc) begin
    //     $display("PC = %h, Index = %h, Instruction = %h", pc, pc[31:2], mem[pc[31:2]]);
    // end

endmodule