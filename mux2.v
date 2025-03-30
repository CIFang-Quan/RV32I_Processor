// this file is helper for 2 bit mux

//`include "definitions.v"
`default_nettype none
`timescale 1ns/1ns

module Mux2 (
    input wire [`DATA_WIDTH-1:0] i_a,
    input wire [`DATA_WIDTH-1:0] i_b,
    input wire i_sel,
    output reg [`DATA_WIDTH-1:0] o_res
);
    always @* begin
        case (i_sel)
            1'b0: o_res = i_a;
            1'b1: o_res = i_b;
            default: o_res = 32'b0;
        endcase
    end
endmodule