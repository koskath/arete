<a id='73329e44-c4e7-480d-a810-0654894da652'></a>

--- 

AD9860/AD9862

<a id='4cacc85e-0594-4f1d-bde5-dbe430cbc6cf'></a>

Table I. Rx Data Timing Table

<a id='e371ed75-86cb-42df-9efb-83be3c7e8f6b'></a>

Table Ia. CLKSEL Set Logic Low

<table id="24-1">
<tr><td id="24-2">CLKSEL</td><td id="24-3">ADC Div 2</td><td id="24-4">Decimate</td><td id="24-5">Multiplex</td><td id="24-6">See Figure 8 for Relative Timing</td></tr>
<tr><td id="24-7" rowspan="8">Low</td><td id="24-8" rowspan="4">No Div</td><td id="24-9" rowspan="2">No Decimation</td><td id="24-a">No Mux</td><td id="24-b">Timing No. 4 Rx Data = 2 × CLKOUT1 CLKOUT1 = 1/2 × CLKIN</td></tr>
<tr><td id="24-c">Mux</td><td id="24-d">Not Allowed</td></tr>
<tr><td id="24-e" rowspan="2">Decimation</td><td id="24-f">No Mux</td><td id="24-g">Timing No. 3 Rx Data = 2 × CLKOUT1 CLKOUT1 = 1/2 × CLKIN</td></tr>
<tr><td id="24-h">Mux</td><td id="24-i">Timing No. 4 Rx Data (MUXED) = 2 × CLKOUT1 CLKOUT1 = 1/2 × CLKIN</td></tr>
<tr><td id="24-j" rowspan="4">Div</td><td id="24-k" rowspan="2">NoDecimation</td><td id="24-l">No Mux</td><td id="24-m">Timing No. 3 Rx Data = CLKOUT1 CLKOUT1 = 1/2 × CLKIN</td></tr>
<tr><td id="24-n">Mux</td><td id="24-o">Timing No. 4 Rx Data(MUXED) = 2 × CLKOUT1 CLOUT1 = 1/2 × CLKIN</td></tr>
<tr><td id="24-p" rowspan="2">Decimation</td><td id="24-q">No Mux</td><td id="24-r">Timing No. 2 Rx Data = 1/2 × CLKOUT1 CLOUT1 = 1/2 × CLKIN</td></tr>
<tr><td id="24-s">Mux</td><td id="24-t">Timing No. 3 Rx Data(MUXED) = CLKOUT1 CLKOUT1 = 1/2 × CLKIN</td></tr>
</table>

<a id='3b6c5d0e-e776-4e08-b163-0346f92bad40'></a>

Table Ib. CLKSEL Set Logic High
<table id="24-u">
<tr><td id="24-v">CLKSEL</td><td id="24-w">ADC Div 2</td><td id="24-x">Decimate</td><td id="24-y">Multiplex</td><td id="24-z">See Figure 8 for Relative Timing</td></tr>
<tr><td id="24-A" rowspan="8">High</td><td id="24-B" rowspan="4">No Div</td><td id="24-C" rowspan="2">No Decimation</td><td id="24-D">No Mux</td><td id="24-E">Timing No. 3 Rx Data = CLKOUT1 CLKOUT1 = CLKIN</td></tr>
<tr><td id="24-F">Mux</td><td id="24-G">Timing No. 4 Rx Data(MUXED) = 2 × CLKOUT1 CLKOUT1 = CLKIN</td></tr>
<tr><td id="24-H" rowspan="2">Decimation</td><td id="24-I">No Mux</td><td id="24-J">Timing No. 2 Rx Data = 1/2 × CLKOUT1 CLKOUT1 = CLKIN</td></tr>
<tr><td id="24-K">Mux</td><td id="24-L">Timing No. 3 Rx Data(MUXED) = CLKOUT1 CLKOUT1 = CLKIN</td></tr>
<tr><td id="24-M" rowspan="4">Div</td><td id="24-N" rowspan="2">No Decimation</td><td id="24-O">No Mux</td><td id="24-P">Timing No. 2 Rx Data = 1/2 × CLKOUT1 CLKOUT1 = CLKIN</td></tr>
<tr><td id="24-Q">Mux</td><td id="24-R">Timing No. 3 Rx Data(MUXED) = CLKOUT1 CLOUT1 = CLKIN</td></tr>
<tr><td id="24-S" rowspan="2">Decimation</td><td id="24-T">No Mux</td><td id="24-U">Timing No. 1 Rx Data = 1/4 × CLKOUT1 CLOUT1 = CLKIN</td></tr>
<tr><td id="24-V">Mux</td><td id="24-W">Timing No. 2 Rx Data (MUXED) = 1/2 × CLKOUT1 CLKOUT1 = CLKIN</td></tr>
</table>

<a id='42cb4dce-8254-4a3b-9038-2c5aede39f90'></a>

<::Timing diagram: A timing diagram showing fCLKOUT1 as a square wave clock signal. Below it are four Rx DATA TIMING signals, each with a different frequency relative to CLKOUT. Rx DATA TIMING No. 1 has fRx = CLKOUT ÷ 4, showing one data period (represented by an 'X' transition) over four clock cycles. Rx DATA TIMING No. 2 has fRx = CLKOUT ÷ 2, showing one data period over two clock cycles. Rx DATA TIMING No. 3 has fRx = CLKOUT, showing one data period per clock cycle. Rx DATA TIMING No. 4 has fRx = 2 × CLKOUT, showing two data periods per clock cycle. Vertical lines indicate timing relationships between the signals. Timing parameters tRx1, tRx2, and tRx3 are shown at the bottom, measuring delays and durations relative to the transitions.::>Figure 9. Rx Timing Diagram

<a id='977fc1e4-28e8-4a2e-96eb-2be34fe76073'></a>

<::Block Diagram: Single Tx Timing, Alternative Operation::> CLKIN (input) connects to an 'ADC DIV2' block. Input to ADC DIV2 is labeled 'A'. Inside the block: 0: B = A, 1: B = A/2. The output of ADC DIV2, labeled 'B', connects to a 'DLL MULT' block. Inside the DLL MULT block: 00: C = B, 01: C = B/2, 10: C = B/4. The output of DLL MULT, labeled 'C', connects to a 'CLKOUT2 DIV' block. Inside the CLKOUT2 DIV block: 00: D = C, 01: D = C/2, 10: D = C/4. The output of CLKOUT2 DIV, labeled 'D', connects to an 'INTERP' block. Inside the INTERP block: 00: E = D, 01: E = 2 x D, 10: E = 4 x D. The output of INTERP is labeled 'E' and goes to 'TxDAC UPDATE RATE SINGLE CHANNEL (CANNOT EXCEED DLL OUTPUT RATE)'. There are also outputs from the main signal path: - From CLKIN, an output labeled 'ADC SAMPLE RATE (NOT TO EXCEED 64MHz)'. - From the output of ADC DIV2 (B), an output labeled 'DLL OUTPUT RATE (NOT TO EXCEED 128MHz)'. - From the output of DLL MULT (C), an output labeled 'CLKOUT2'. - From the output of CLKOUT2 DIV (D), an output labeled 'INPUT Tx DATA RATE (SINGLE CHANNEL)'. Figure 10. Single Tx Timing Block Diagram, Alternative Operation

<a id='cdae84f0-6b82-4ba0-9f8f-48508c8255da'></a>

REV. 0

<a id='f490a056-eff6-46b1-b7b3-3e44ce82c4fc'></a>

-25-