// this file is for pc adder constantly add 4 to pc

//`include "definitions.v"
`default_nettype none
`timescale 1ns/1ns

module Pc_adder (
    input wire [`DATA_WIDTH-1:0] i_pc,
    output wire [`DATA_WIDTH-1:0] o_pc_next
);
    assign o_pc_next = i_pc + 32'd4;
endmodule