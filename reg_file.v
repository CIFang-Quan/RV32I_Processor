// this file is register file for single cycle processor.
// ISA based on RV32I

//`include "definitions.v"
`default_nettype none
`timescale 1ns/1ns

module Reg_file (
    input wire i_clk,
    input wire i_rst,
    input wire i_rw,
    input wire [$clog2(`NUM_REGISTER)-1:0] i_rd_addr,
    input wire [`DATA_WIDTH-1:0] i_rd,
    input wire [$clog2(`NUM_REGISTER)-1:0] i_rs1_addr,     
    input wire [$clog2(`NUM_REGISTER)-1:0] i_rs2_addr,
    output wire [`DATA_WIDTH-1:0] o_rs1,     
    output wire [`DATA_WIDTH-1:0] o_rs2,
    output wire [`DATA_WIDTH-1:0] o_all_regs [31:0]
);

    reg [`DATA_WIDTH-1:0] registers [0:`NUM_REGISTER-1];
    integer i;

    initial begin
        for (i = 0; i < `NUM_REGISTER; i = i + 1) begin
            registers[i] = 0;  // Initialize each memory location to 0
        end
    end

    // x0 is hardwired to 0, if try to read x0 it will return 0
    assign o_rs1 = (i_rs1_addr==5'b0) ? 32'b0 : registers[i_rs1_addr];
    assign o_rs2 = (i_rs2_addr==5'b0) ? 32'b0 : registers[i_rs2_addr];

    genvar j;
    generate
        for (j = 0; j < 32; j = j + 1) begin
            assign o_all_regs[j] = registers[j];
        end
    endgenerate


    always @(posedge i_clk or posedge i_rst) begin
        // reset remain empty
        // need to figure out when need reset
        if (i_rst) begin
            for (i = 1; i < 32; i = i + 1) begin
                registers[i] <= 32'b0;
            end
        end else if (i_rw && i_rd_addr != 5'b0) begin
            registers[i_rd_addr] <= i_rd;
        end
    end
endmodule
// this file is register file for single cycle processor.