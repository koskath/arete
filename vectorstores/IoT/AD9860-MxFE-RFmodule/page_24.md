<a id='a4a2353b-acb0-46c8-8099-011ecaed73bf'></a>

AD9860/AD9862

For the Normal Operation mode, the Tx timing is based on a clock derived from the DLL output, while the Rx clock is unaffected by the DLL setting.

<a id='0bb37949-9001-4b74-b018-fa08a685cbbc'></a>

The Alternative Operation mode, timing utilizes the output of
the DLL to generate both Rx and Tx clocks. It also sets default
operation of the DLL to 4× mode.

<a id='f6a91e2e-f6ad-4168-b80d-a9b22c237f6a'></a>

Normal Operation is typically recommended because the Rx ADC is more sensitive to the jitter and noise that the DLL may gener- ate, so its performance may degrade. The Mode/TxBlank pin logic level at power up or RESET defines in which mode the device powers up. If Mode/TxBlank is low at power up, the Normal Operation mode is configured. Otherwise, the Alternative Operation mode is configured.

<a id='e08c6693-7740-40d3-94a2-38dddd7ba580'></a>

**Rx Path (Normal Operation)**
The ADC sampling rate, the Rx data output rate, and the rate of
CLKOUT1 (clock used to latch output data) are the parameters
of interest for the receive path data. These parameters in addition
to the data bandwidth are related to CLKIN by decimation filters,
divide by two circuits, data multiplexer logic and retiming latches.
The Rx path timing can be broken into two separate relation-
ships: the ADC sample rate relative to the input clock, CLKIN
and the output data rate relative to CLKOUT1.

<a id='bbf780e4-df05-4417-a822-61874aa7a284'></a>

The ADCs sample rate relative to CLKIN is controlled by the
ADC Div2 register and the sample rate can be equal to or one half
of the input clock rate.

<a id='013db6e2-2b58-4287-95eb-861f7e9f6eab'></a>

The output data relative to CLKOUT1 has many configurations providing a flexible interface. The different options are shown in Figure 8. Table Ia and Ib describe the setup required to obtain the desired data timing. RxSync is available when the Rx data is decimated and multiplexed to identify which channel data is present at the output bus.

<a id='4ff1cc47-b87d-47ad-8cb5-63e7e5b14f46'></a>

The Rx data (unless re-timed using the Rx Retime register) is timed relative to the CLKOUT1 pin output. The Rx output data can be decimated (halving the data rate) or both channels can be multiplexed onto the channel A data bus (doubling the data rate).

<a id='d66a6402-a6e8-4406-9a2f-3436334f9025'></a>

Decimation enables oversampling while maintaining a slower external data transfer rate and provides superior suppression of out of band signals and noise. Multiplexing enables fewer digital output bits to be used to transfer data from the Rx path to the digital ASIC collecting the data.

<a id='80d3ceca-9e77-4e74-916a-8193866a61ad'></a>

When Mux Mode is enabled with an output data rate equal to CLKOUT1 (Timing No. 3 in Figure 9) then the RxSync pin is required to identify which channel's output data is on the output data bus. RxSync output is aligned with the output data, and by default a logic low indicates data from Rx Channel B is currently on the output data bus. If RxSync is logic high, then data from Rx Channel A is currently on the output data bus. The Inv RxSync register can be used to switch this notation.

<a id='ba10500d-b4c4-48d8-a0d1-4966bddd2610'></a>

The CLKOUT1 pin outputs a clock at the frequency of CLKIN or CLKIN/2 depending on the voltage level applied to the CLKSEL pin. If a logic low is applied to CLKSEL, CLKOUT1 will run at half the CLKIN rate, if CLKSEL is set to logic high CLKOUT1 outputs a clock equal to CLKIN.

<a id='1c67e942-243a-4290-93bf-0043aafab997'></a>

This timing flexibility along with the invert option for CLKOUT1,
controlled by the Inv 1 register allow for various methods of latch-
ing data from the Rx path to the digital ASIC, which will process
the data. These options are shown in Table Ia and Ib along with
a timing diagram in Figure 9. Not shown is the option to invert
CLKOUT1, controlled by the Inv 1 register. For this mode, relative
timing remains the same except the opposite edges of CLKOUT1
would be used.

<a id='3130494f-54ba-49e0-baf5-386877249687'></a>

<::block diagram: Dual Tx Timing Block Diagram, Alternative Operation::>ADC DIV2 block. Input is CLKIN (A). Output is B. Operations: 0: B = A, 1: B = A/2. An output line from this block indicates "ADC SAMPLE RATE (NOT TO EXCEED 64MHz)". An arrow points from ADC DIV2 (B) to DLL MULT (B).DLL MULT block. Input is B. Output is C. Operations: 00: C = B, 01: C = 2 × B, 10: C = 4 × B. An output line from this block indicates "DLL OUTPUT RATE (NOT TO EXCEED 128MHz)". An arrow points from DLL MULT (C) to CLKOUT2 DIV (C).CLKOUT2 DIV block. Input is C. Output is D. Operations: 00: D = C, 01: D = C/2, 10: D = C/4. An output line from this block indicates "CLKOUT2". An arrow points from CLKOUT2 DIV (D) to 2 EDGES (D).2 EDGES block. Input is D. Output is E. Operations: 0: E = D, 1: E = 2 × D. An output line from this block indicates "INPUT Tx DATA RATE". An arrow points from 2 EDGES (E) to DUAL CHANNEL FACTOR (E).DUAL CHANNEL FACTOR block. Input is E. Output is F. Operation: F = E/2. An arrow points from DUAL CHANNEL FACTOR (F) to INTERP (F). An output line from F before INTERP indicates "INPUT Tx DATA RATE EACH CHANNEL".INTERP block. Input is F. Output is G. Operations: 00: G = F, 01: G = 2 × F, 10: G = 4 × F. An output line from this block indicates "TxDAC UPDATE RATE EACH CHANNEL (CANNOT EXCEED DLL OUTPUT RATE)".

<a id='1c5adaaa-b3f1-4783-bbb7-2c050fcf9ba0'></a>

<::A timing diagram showing three waveforms. The top waveform is a square wave labeled f_CLKOUT2. Below it is "Tx DATA TIMING No. 1" with f_Tx = CLKOUT2, represented by a series of eye patterns. Below that is "Tx DATA TIMING No. 2" with f_Tx = 2 × CLKOUT2, also represented by eye patterns, but with transitions occurring twice as frequently. Vertical lines indicate timing relationships between the signals. Horizontal double-headed arrows with labels f_Tx1, f_Tx2, f_Tx3, and f_Tx4 denote specific timing intervals between transitions. Figure 12. Tx Timing Diagram::>

<a id='d116bbb6-6feb-461e-ad75-848e62807ce3'></a>

-26-

<a id='68e75879-92dd-4a47-b67b-ffd9b51281e9'></a>

REV. 0