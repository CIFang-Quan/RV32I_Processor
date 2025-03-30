// this file is for dmem 
// dmem is a memory that store/load data
// it only support read/write operation

//`include "definitions.v"
`default_nettype none
`timescale 1ns/1ns

module Dmem (
    input wire i_clk,
    input wire i_rst,
    input wire i_st,
    input wire i_ld,
    //input wire write_enable,
    input wire [`DATA_WIDTH-1:0] i_data,
    input wire [`ADDR_WIDTH-1:0] i_addr,
    output reg [`DATA_WIDTH-1:0] o_data
);
    // just for test purpose
    reg [`DATA_WIDTH-1:0] mem[0:1023];
    // reg [`DATA_WIDTH-1:0] mem[0:(1<<(`ADDR_WIDTH-2))-1]; // 2^32 byte
   
    // init dmem all 0
    integer i;
    initial begin
        for (i = 0; i < 1024; i = i + 1) begin
            mem[i] = 32'b0;
        end
        // $readmemh("data.txt", mem);
    end
    // sync write and sync read X
    // always @(posedge clk or posedge rst) begin
    //     if (rst) begin
    //         output_data <= 32'b0;
    //     end else begin
    //         if (store) 
    //             mem[addr[31:2]] <= input_data; 
                
    //         if (load) 
    //             output_data <= mem[addr[31:2]];
    //         else 
    //             output_data <= 32'b0;
    //     end
    // end
    // Synchronous write, asynchronous read
    always @(posedge i_clk or posedge i_rst) begin
        if (i_rst) begin
            // Reset logic
            for (i = 0; i < 1024; i = i + 1) begin
            mem[i] = 32'b0;
        end
        end else begin
            if (i_st) 
                mem[i_addr >> 2] <= i_data; 
        end
    end
    // Asynchronous read - outside the clocked always block
    always @* begin
        if (i_ld)
            o_data = mem[i_addr >> 2];
        else
            o_data = 32'b0;
    end
endmodule