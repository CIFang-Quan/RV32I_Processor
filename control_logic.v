// this file is for control logic of RV32I 
// single cycle processor 
// it will generate control signals for ALU, MUX, and dMEM, brcmp

//`include "definitions.v"
`default_nettype none
`timescale 1ns/1ns

module Control_logic (
    input wire [31:0] i_inst,
    input wire i_breq,
    input wire i_brlt,
    output reg o_pcsel,
    output reg o_reg_w,
    output reg [2:0] o_imm_sel,
    output reg o_op1_sel,
    output reg o_op2_sel,
    output reg o_brun,
    output reg [3:0] o_alu_ctrl,
    output reg o_mem_r,
    output reg o_mem_w,
    output reg [1:0] o_wb_sel
);
    wire [6:0] opcode;
    wire [2:0] funct3;
    wire [6:0] funct7; 
    assign opcode = i_inst[6:0];
    assign funct3 = i_inst[14:12];
    assign funct7 = i_inst[31:25];



    always @(*) begin
        // just avoid latches
        o_pcsel = 1'b0;    // by deafult pc+4
        o_mem_r = 1'b0;    // no need to read from dmem
        o_mem_w = 1'b0;    // no need write to dmem
        o_reg_w = 1'b0;    // no need to write to rd
        o_imm_sel = `IMM_NOP; // no immediate
        o_alu_ctrl = `OP_ALU_NOP; // no operation
        o_op1_sel = 1'b0; // rs1
        o_op2_sel = 1'b1; // rs2
        o_brun = 1'b0; // unsigned compare
        o_wb_sel = 2'b00; // write data from dmem to rd
        case (opcode)
            `OP_LUI: begin // LUI
                o_pcsel = 1'b0;        // by deafult pc+4
                o_mem_r = 1'b0;    // no need to read from dmem
                o_mem_w = 1'b0;    // no need to write to dmem
                o_reg_w = 1'b1;    // write to rd
                o_wb_sel = 2'b11; // write immeidate number to rd
                o_imm_sel = `IMM_U_TYPE; // U-type immediate
                o_alu_ctrl = `OP_ALU_NOP; // no operation
            end
            `OP_AUIPC: begin // AUIPC
                o_pcsel = 1'b0;        // by deafult pc+4
                o_op1_sel = 1'b1; // current pc
                o_op2_sel = 1'b0; // immeidate number
                o_mem_r = 1'b0;    // no need to read from dmem
                o_mem_w = 1'b0;    // no need to write to dmem
                o_reg_w = 1'b1;    // write to rd
                o_wb_sel = 2'b01; // write pc+imm to rd
                o_imm_sel = `IMM_U_TYPE; // U-type immediate
                o_alu_ctrl = `OP_ALU_ADD; // pc + imm use add operation
            end
            `OP_JAL: begin // JAL
                o_pcsel = 1'b1;        // not pc+4 instead address after alu computation
                o_op1_sel = 1'b1; // current pc
                o_op2_sel = 1'b0; // immeidate number 
                o_mem_r = 1'b0;    // no need to read from dmem
                o_mem_w = 1'b0;    // no need to write to dmem
                o_reg_w = 1'b1;    // write pc+4 to rd
                o_wb_sel = 2'b10; // write pc+4 to rd
                o_imm_sel = `IMM_J_TYPE; // J-type immediate
                o_alu_ctrl = `OP_ALU_ADD; // pc + imm use add operation
            end
            `OP_JALR: begin // JALR
                o_pcsel = 1'b1;        // not pc+4 instead address after alu computation
                o_op1_sel = 1'b0;  // rs1 
                o_op2_sel = 1'b0; // immeidate number
                o_mem_r = 1'b0;    // no need to read from dmem
                o_mem_w = 1'b0;    // no need to write to dmem
                o_reg_w = 1'b1;    // write pc+4 to rd
                o_wb_sel = 2'b10; // write pc+4 to rd
                o_imm_sel = `IMM_I_TYPE; // I-type immediate
                o_alu_ctrl = `OP_ALU_ADD; // pc + imm use add operation
            end 
            `OP_BRANCH: begin // B-type  
                o_op1_sel = 1'b1; // current pc
                o_op2_sel = 1'b0; // immeidate number
                o_mem_r = 1'b0;    // no need to read from dmem
                o_mem_w = 1'b0;    // no need to write to dmem
                o_reg_w = 1'b0;    // write pc+4 to rd
                o_imm_sel = `IMM_B_TYPE; // B-type immediate
                o_alu_ctrl = `OP_ALU_ADD; // pc + imm use add operation
                case (funct3)
                    3'b000: begin // BEQ
                        if (i_breq) begin
                            o_pcsel = 1'b1;
                        end
                    end
                    3'b001: begin // BNE
                        if (~i_breq) begin
                            o_pcsel = 1'b1;
                        end
                    end
                    3'b100: begin // BLT
                        if (i_brlt) begin
                            o_pcsel = 1'b1;
                        end
                    end
                    3'b101: begin // BGE
                        if (~i_brlt) begin
                            o_pcsel = 1'b1;
                        end
                    end
                    3'b110: begin // BLTU
                        o_brun = 1'b1;// unsigned compare
                        if (i_brlt) begin
                            o_pcsel = 1'b1;
                        end
                    end
                    3'b111: begin // BGEU
                        o_brun = 1'b1;// unsigned compare
                        if (~i_brlt) begin
                            o_pcsel = 1'b1;
                        end
                    end
                    default: begin
                        //just avoid latches
                        //TODO: implement default case
                    end
                endcase
            end
            //load & store only support lw,sw
            `OP_LOAD: begin // I-type load
                o_pcsel = 1'b0;    // by deafult pc+4
                o_op1_sel = 1'b0; // rs1
                o_op2_sel = 1'b0; // immeidate number
                o_mem_r = 1'b1;    // read from dmem
                o_mem_w = 1'b0;    // no need to write to dmem
                o_reg_w = 1'b1;    // write to rd
                o_wb_sel = 2'b00; // write data from dmem to rd
                o_imm_sel = `IMM_I_TYPE; // I-type immediate
                o_alu_ctrl = `OP_ALU_ADD; // rs1 + imm use add operation
            end
            `OP_STORE: begin // S-type store
                o_pcsel = 1'b0;    // by deafult pc+4
                o_op1_sel= 1'b0; // rs1
                o_op2_sel = 1'b0; // immeidate number
                o_mem_r = 1'b0;    // no need to read from dmem
                o_mem_w = 1'b1;    // write to dmem
                o_reg_w = 1'b0;    // no need to write to rd
                o_imm_sel = `IMM_S_TYPE; // S-type immediate
                o_alu_ctrl = `OP_ALU_ADD; // rs1 + imm use add operation
            end
            `OP_ALUI: begin // I-type ALU
                o_pcsel = 1'b0;    // by deafult pc+4
                o_op1_sel= 1'b0; // rs1
                o_op2_sel = 1'b0; // immeidate number
                o_mem_r = 1'b0;    // no need to read from dmem
                o_mem_w = 1'b0;    // no need write to dmem
                o_reg_w = 1'b1;    // write to rd
                o_wb_sel = 2'b01; // write data from ALU to rd
                o_imm_sel = `IMM_I_TYPE; // I-type immediate
                case (funct3)
                    3'b000: begin // ADDI
                        o_alu_ctrl = `OP_ALU_ADD;
                    end
                    3'b010: begin // SLTI
                        o_alu_ctrl = `OP_ALU_SLT;
                    end
                    3'b011: begin // SLTIU
                        o_alu_ctrl = `OP_ALU_SLTU;
                    end
                    3'b100: begin // XORI
                        o_alu_ctrl = `OP_ALU_XOR;
                    end
                    3'b110: begin // ORI
                        o_alu_ctrl = `OP_ALU_OR;
                    end
                    3'b111: begin // ANDI
                        o_alu_ctrl = `OP_ALU_AND;
                    end
                    3'b001: begin // SLLI
                        o_alu_ctrl = `OP_ALU_SLL;
                    end
                    3'b101: begin // SR?I
                        if (funct7[5]) begin
                            o_alu_ctrl = `OP_ALU_SRA; // SRAI
                        end else begin
                            o_alu_ctrl = `OP_ALU_SRL; // SRLI
                        end
                    end
                    default: begin
                        o_alu_ctrl = `OP_ALU_NOP;
                    end
                endcase
            end
            `OP_ALU: begin // R-type ALU
                o_pcsel = 1'b0;    // by deafult pc+4
                o_op1_sel= 1'b0; // rs1
                o_op2_sel = 1'b1; // rs2
                o_mem_r = 1'b0;    // no need to read from dmem
                o_mem_w = 1'b0;    // no need write to dmem
                o_reg_w = 1'b1;    // write to rd
                o_wb_sel = 2'b01; // write data from ALU to rd
                o_imm_sel = `IMM_NOP; // no immediate
                case (funct3)
                    3'b000: begin // ADD/SUB
                        if (funct7[5]) begin
                            o_alu_ctrl = `OP_ALU_SUB; // SUB
                        end else begin
                            o_alu_ctrl = `OP_ALU_ADD; // ADD
                        end
                    end
                    3'b001: begin // SLL
                        o_alu_ctrl = `OP_ALU_SLL;
                    end
                    3'b010: begin // SLT
                        o_alu_ctrl = `OP_ALU_SLT;
                    end
                    3'b011: begin // SLTU
                        o_alu_ctrl = `OP_ALU_SLTU;
                        //brunsigned = 1'b1;
                    end
                    3'b100: begin // XOR
                        o_alu_ctrl = `OP_ALU_XOR;
                    end
                    3'b101: begin // SRL/SRA
                        if (funct7[5]) begin
                            o_alu_ctrl = `OP_ALU_SRA; // SRA
                        end else begin
                            o_alu_ctrl = `OP_ALU_SRL; // SRL
                        end
                    end
                    3'b110: begin // OR
                        o_alu_ctrl = `OP_ALU_OR;
                    end
                    3'b111: begin // AND
                        o_alu_ctrl = `OP_ALU_AND;
                    end
                    default: begin
                        o_alu_ctrl = `OP_ALU_NOP;
                    end
                endcase
            end
            `OP_FENCE: begin // FENCE
                //TODO: implement FENCE
            end
            `OP_SYSTEM: begin // SYSTEM
                //TODO: implement SYSTEM
            end
            default: begin
                // just avoid latches
                //TODO: implement default case
            end
        endcase
    end
endmodule