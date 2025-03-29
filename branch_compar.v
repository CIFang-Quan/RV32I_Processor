// this file is for branch comparator 

// we support beq,bne,blt,bltu(bge,bgeu is implicit support
// since we support blt,bltu)

//`include "definitions.v"
`default_nettype none
`timescale 1ns/1ns

module Brcmptop (
    input wire [`DATA_WIDTH-1:0] i_rs1,
    input wire [`DATA_WIDTH-1:0] i_rs2,
    input wire i_brun, //0 signed, 1 unsigned
    output wire o_breq, // 0 not equal, 1 equal
    output wire o_brlt  // 0 not less than, 1 less than
    // output wire o_bge  // 0 not greater | equal than, 1 greater | equal than
);
    wire temp_brlt_s, temp_brlt_u;
    brcmp cmp (
        .i_rs1(i_rs1),
        .i_rs2(i_rs2),
        .o_breq(o_breq),
        .o_brlt_s(temp_brlt_s),
        .o_brlt_u(temp_brlt_u)
    );
    helper_mux mux (
        .i_a(temp_brlt_s),
        .i_b(temp_brlt_u),
        .i_sel(i_brun),
        .o_res(o_brlt)
    );  
endmodule

module helper_mux (
    input wire i_a,
    input wire i_b,
    input wire i_sel,
    output wire o_res
);
    assign o_res = (i_sel) ? i_b : i_a;
endmodule

module brcmp (
    input wire [`DATA_WIDTH-1:0] i_rs1,
    input wire [`DATA_WIDTH-1:0] i_rs2,
    // input wire i_brun, //0 signed, 1 unsigned
    // beq // 0 not equal, 1 equal
    // blt, bltu // 0 not less than, 1 less than
    output wire o_breq, o_brlt_s, o_brlt_u
);

    //beq
    assign o_breq = ($signed(i_rs1) == $signed(i_rs2)) ? 1 : 0;
    //blt signed
    assign o_brlt_s = ($signed(i_rs1) < $signed(i_rs2)) ? 1 : 0;
    //blt unsigned
    assign o_brlt_u = (i_rs1 < i_rs2) ? 1 : 0;
endmodule

