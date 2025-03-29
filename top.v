// `include "definitions.vh"
// `include "pc_adder.v"
// `include "imem.v"
// `include "control_logic.v"
// `include "immgen.v"
// `include "reg_file.v"
// `include "alu.v"
// `include "dmem.v"
// `include "mux2.v"
// `include "mux4.v"
// `include "branch_compar.v"
`default_nettype none
`timescale 1ns/1ns

module top(
    input wire clk,
    input wire rst,
    output wire [`DATA_WIDTH-1:0] debug
);
    wire [`ADDR_WIDTH-1:0] o_pcreg;
    wire [`ADDR_WIDTH-1:0] o_pcadder;

    wire [`INST_WIDTH-1:0] o_imem;

    wire [`DATA_WIDTH-1:0] o_regfile_rd1;
    wire [`DATA_WIDTH-1:0] o_regfile_rd2;

    wire [`DATA_WIDTH-1:0] o_immgen;
    wire [`DATA_WIDTH-1:0] o_op1sel;
    wire [`DATA_WIDTH-1:0] o_op2sel;
    wire [`DATA_WIDTH-1:0] o_alu;
    
    wire [`DATA_WIDTH-1:0] o_dmem;

    wire [`DATA_WIDTH-1:0] o_wbsel;

    wire decode_pcsel;
    wire decode_regw;
    wire [2:0] decode_immsel;
    wire decode_op1sel;
    wire decode_op2sel;
    wire decode_brun;
    wire [3:0] decode_aluctrl;
    wire decode_dmemr;
    wire decode_dmemw;
    wire [1:0] decode_wbsel;

    wire decode_breq;
    wire decode_brlt;

    reg [`ADDR_WIDTH-1:0] PC;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            PC <= 32'h00000000;
        end 
        else begin 
            if (decode_pcsel) begin
                PC <= o_alu;
            end 
            else begin
                PC <= o_pcadder;
            end
        end
    end
    assign o_pcreg = PC;

    Pc_adder pc_adder (
        .i_pc(o_pcreg),
        .o_pc_next(o_pcadder)
    );

    Imem imem (
        .i_pc(o_pcreg),
        .o_inst(o_imem)
    );

    Reg_file reg_file(
        .i_clk(clk),
        .i_rst(rst),
        .i_rw(decode_regw),
        .i_rd_addr(o_imem[11:7]),
        .i_rd(o_wbsel),
        .i_rs1_addr(o_imem[19:15]),
        .i_rs2_addr(o_imem[24:20]),
        .o_rs1(o_regfile_rd1),
        .o_rs2(o_regfile_rd2)
    );

    Immgen immgen(
        .i_imm_ctrl(decode_immsel),
        .i_inst(o_imem),
        .o_imm(o_immgen)
    );

    Mux2 op1sel(
        .i_a(o_regfile_rd1),
        .i_b(o_pcreg),
        .i_sel(decode_op1sel),
        .o_res(o_op1sel)
    );

    Mux2 op2sel(
        .i_a(o_immgen),
        .i_b(o_regfile_rd2),
        .i_sel(decode_op2sel),
        .o_res(o_op2sel)
    );

    Alu alu(
        .i_alu_ctrl(decode_aluctrl),
        .i_a(o_op1sel),
        .i_b(o_op2sel),
        .o_res(o_alu)
    );

    Brcmptop brcmp(
        .i_rs1(o_regfile_rd1),
        .i_rs2(o_regfile_rd2),
        .i_brun(decode_brun),
        .o_breq(decode_breq),
        .o_brlt(decode_brlt)
    );

    Dmem dmem(
        .i_clk(clk),
        .i_rst(rst),
        .i_st(decode_dmemw),
        .i_ld(decode_dmemr),
        .i_data(o_regfile_rd2),
        .i_addr(o_alu),
        .o_data(o_dmem)
    );

    Mux4 wbsel(
        .i_a(o_dmem),
        .i_b(o_alu),
        .i_c(o_pcadder),
        .i_d(o_immgen),
        .i_sel(decode_wbsel),
        .o_res(o_wbsel)
    );

    Control_logic control_logic(
        .i_inst(o_imem),
        .i_breq(decode_breq),
        .i_brlt(decode_brlt),
        .o_pcsel(decode_pcsel),
        .o_reg_w(decode_regw),
        .o_imm_sel(decode_immsel),
        .o_op1_sel(decode_op1sel),
        .o_op2_sel(decode_op2sel),
        .o_brun(decode_brun),
        .o_alu_ctrl(decode_aluctrl),
        .o_mem_r(decode_dmemr),
        .o_mem_w(decode_dmemw),
        .o_wb_sel(decode_wbsel)
    );

endmodule