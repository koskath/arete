<a id='af2e06d6-a592-4db5-b861-b49151ecda0c'></a>

AD9860/AD9862

<a id='2bc948e7-c379-4815-9ee6-995ca3b2bbde'></a>

Conversion is initiated by writing a logic high to one or both of the Start register bits, Register D34 B0 (StartA) and D34 B3 (StartB). When the conversion is complete, the straight binary, 10-bit output data of the AUX ADC is written to one of four reserved locations in the register map depending on which auxiliary ADC and which multiplexed input is selected. Because the auxiliary ADCs output 10 bits, two register addresses are needed for each data location.

<a id='021b79e2-2635-4c33-b388-83548a511a08'></a>

Initiating a conversion or retrieving data can also be accomplished either through the standard Serial Port Interface by reading and writing to the appropriate registers or through a dedicated Auxiliary Serial Port Interface (AUX SPI). The AUX SPI can be configured to allow fast access and control of either one of the auxiliary ADCs and is available so that the SPI is not tied up retrieving auxiliary ADC data.

<a id='e1ccd738-0784-4cda-8915-d52f470e4d02'></a>

The AUX SPI can be enabled and configured by setting register AUX ADC CTRL. Setting register use pins high enables the AUX SPI port. Setting register Sel BnotA low connects auxiliary ADC A to the AUX SPI port, while setting it high connects auxiliary ADC B to the AUX SPI port. As mentioned above, setting the appropriate Select bit selects which of the multiplexed input is connected to the auxiliary ADC.

<a id='77443934-40a5-4c3c-8e5d-97eb1028c2d7'></a>

The AUX SPI consists of a chip select pin (AUX_SPI_csb),
a clock pin (AUX_SPI_clk), and a data output pin (AUX_SPI_do).
A conversion is initiated by pulsing the AUX_SPI_csb pin low.
When the conversion is complete, the data pin, AUX_SPI_do,
previously a logic low, will go high. At this point, the user supplies
an external clock, previously tied low, no data is present on the
first rising edge. The data output bit is updated on the falling
edge of the clock pulse and is settled and can be latched on the
next clock rising edge. The data arrives serially, MSB first. The
AUX SPI runs up to a rate of 16 MHz.

<a id='11e92c20-cbed-4d7c-980c-c0d842fabff0'></a>

## AUX DAC
The AD9860/AD9862 has three 8-bit voltage output auxiliary DACs, AUX DACs. The AUX DACs are available for supplying various control voltages throughout the system such as a VCXO voltage control or external VGA gain control and can typically sink or source up to 1 mA.

<a id='da1f0691-d5a3-47b3-88ec-d6a08d1d1b26'></a>

An internal voltage reference buffer provides a full-scale voltage reference for both of the AUX DACs equal to the supply voltage for the AUX DACs. The straight binary input codes are written to the appropriate registers. If the Slave Mode register bit is high, slave mode enabled, the AUX DAC(s) update will occur when the appropriate update register is written to. Otherwise, the update will occur at the conclusion of the data being written to the register. Typical maximum settling time for the auxiliary DAC is around 6 s.

<a id='f583e2c9-7e39-456e-9709-51a0702c7907'></a>

Other optional controls include an invert register control and a
power down option. The invert register control, i.e., instead of
hexFF being high and hex00 being low, hex00 is high, and hexFF
will be minimum setting.

<a id='1acf71b8-468c-480d-82fa-25e7f260c6ff'></a>

## Sigma-Delta
A 12-bit sigma-delta (SD) output is available to provide an additional control voltage. The SD control word is written to Registers D42, 43; SD [11:4] are the 8 MSBs and SD [3:0] are the 4 LSBs. The 12-bit word is processed by a sigma-delta modulator and produces 1-bit data at an oversampled rate equal to 1/8 of the receive ADC's sampling rate (up to 8 MSPS). The 1-bit data then feeds a 1-bit DAC. The 1-bit DAC exhibits perfect linearity. An external low-pass filter at the output should be used to low-pass filter the pulse modulated data to produce a linear output control voltage.

<a id='5ccca1ba-6e70-4d59-aed9-5a3cc0ba3444'></a>

REV. 0

<a id='e51776f7-cfa7-4bc9-a132-82a44f2ed9df'></a>

-31-