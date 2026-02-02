<a id='16549b38-af38-4033-81c1-385a79d69d32'></a>

## AD9860/AD9862

default, this bit is low, setting up the DLL in "slow" mode. This
bit must be set high for DLL output frequencies over 64 MHz.

<a id='e61054e0-d9aa-4d5e-af46-68ce83871502'></a>

## REGISTER 25: CLKOUT

### BIT 7, 6: CLKOUT2 Divide Factor
These bits control what rate the CLKOUT2 Pin will operate at relative to the DLL output rate. The DLL output rate can be output directly or divided by 2, 4, or 8. Bit 7 is the MSB and Bit 6 is the LSB.

<a id='2a4ef36f-5b2d-477c-97f7-d58b2d6b64a8'></a>

MSB, LSB

00 (Default)
01
10
11

Relative CLKOUT2 Frequency

Equals DLL output rate
Equals DLL output rate divided by 2
Equals DLL output rate divided by 4
Equals DLL output rate divided by 8

<a id='74ffba52-b3fb-4845-967a-c3e2f5e2a2ec'></a>

BIT 5, 1: Inv 2/Inv 1
The output clocks from CLKOUT1 and CLKOUT2 can be
inverted by setting the appropriate one of these bits high.

<a id='39dc0430-62fa-41ca-998d-851b4b18bd2e'></a>

**BIT 4, 0: Dis 2/Dis 1**
The output clocks from CLKOUT1 and CLKOUT2 can be
disabled and a logic low output is forced by setting the appro-
priate one of these bits high.

<a id='0dcc29ec-0381-4c40-9b91-e0ddf09c7294'></a>

**REGISTER 26–33: AUXILIARY ADC A2/A1/B2/B1**
**AUX ADC A2, A1, B2, B1 Data**
These registers are read only registers that are used for read back of the 10-bit auxiliary ADC. The 10 bits are broken into a two registers, one containing the upper eight bits and the other containing the lower two bits.

<a id='7c33e531-58ea-46b6-b98c-b07d4595b767'></a>

REGISTER 34: AUX ADC CONTROL
BIT 7: Aux SPI (Enable)
One of the Auxiliary ADCs can be controlled through an dedi-
cated Auxiliary Serial Port. Setting this bit high enables this mode.

<a id='d6696ae8-4108-4437-a798-26aef9cb3e44'></a>

BIT 6: Sel BnotA
If the auxiliary Serial port is used, this bit selects which Auxiliary
ADC, A or B, will be using the dedicated Auxiliary Serial port.
The Auxiliary Serial port by default (low setting) controls Auxil-
iary ADC A. Setting this bit high will allow the Auxiliary Serial
Port to control Auxiliary ADC B.

<a id='2b366432-f504-4076-8127-b9adf38ad19d'></a>

BIT 5, 2: Refsel B/A
By default, the auxiliary ADCs use an external reference applied to
the AUX_REF pin. This voltage will act as the full-scale reference
for the selected auxiliary ADC. Either auxiliary ADC can use an
internally generated reference, which is a buffered version of the
analog supply voltage. To enable use of the internal reference for
either of the auxiliary ADCs, the respective Refsel register should
be set high.

<a id='c8b29c19-8bee-4bcf-b2db-f52ef5a8e911'></a>

**BIT 4, 1: Select B/A**
These bits select which of the two inputs will be connected to the respective auxiliary ADC. By default (setting low), the AUX_ADC_A2 pin is connected to Auxiliary ADC A and AUX_ADC_B2 pin is connected to Auxiliary ADC B. Setting the respective bit high will connect the AUX_ADC_A1 pin to Auxiliary ADC A and/or AUX_ADC_B1 pin to Auxiliary ADC B.

<a id='b2370f7f-68a3-4cf4-ae1c-d63303a2e096'></a>

BIT 3, 0: Start B/A
Setting a high bit to either of these registers initiates a conversion
of the respective auxiliary ADC, A or B. The register bit always
reads back a low.

<a id='cdf9c050-e2ba-464d-8d25-6066d8fa9230'></a>

**REGISTER 35: AUX ADC CLOCK**

**BIT 0: CLK/4**

By default (setting low), the auxiliary ADCs are run at the receive ADC conversion rate divided by 2. Setting this bit high will run

<a id='342edaa0-a653-437d-9ffe-5448432a74b2'></a>

the Auxiliary ADCs with a clock that is 1/4 of the receive ADC conversion rate. The conversion rate of the auxiliary ADCs should be less than 20 MHz.

<a id='18317e53-5c03-4704-af9c-21948d6ca71a'></a>

**REGISTER 36, 37, 38: AUX DAC A/B/C**
**Auxiliary DAC A, B, and C Output Control Word**
Three 8-bit, straight binary words are used to control the output of three on-chip auxiliary DACs. The auxiliary DAC output changes take effect immediately after any of the serial write is completed. The DAC output control words have default values of 0. The smaller programmed output controlled words corre-spond to lower DAC output levels.

<a id='73ca8fdc-c9bb-4183-a649-ed8504284c82'></a>

## REGISTER 39: AUX DAC UPDATE
### BIT 7: Slave Enable
A low setting (default) updates the auxiliary DACs after the respective register is written to. To synchronize the auxiliary DAC outputs to each other, a slave mode can be enabled by setting this bit high and then setting a high to the appropriate update registers.

<a id='57cf65b3-ab2a-4b4d-867e-ea3c679a9c91'></a>

BIT 2/1/0: Update C, B, and A
Setting a high bit to any of these registers initiates an update of the respective Auxiliary DAC, A, B, or C, when Slave mode is enabled using the Slave Enable register. The register bit is a one shot and always reads back a low. Note: be sure to keep the Slave Enable bit high when using the auxiliary DAC synchronization option.

<a id='a4df16df-4fe8-44ef-b770-d42ceb348709'></a>

REGISTER 40: AUX DAC POWER-DOWN
BIT 2/1/0: Power Down C, B, and A
Setting any of these bits high will power down the appropriate
auxiliary DAC. By default, these bits are low and the auxiliary
DACs are enabled.

<a id='f7206853-c093-4c6d-8d27-4ae70fe9b3d5'></a>

**REGISTER 41: AUX DAC CONTROL**
**BIT 4, 2, 0: Inv C, B, and A**
Setting any of these bits high will invert the appropriate Auxiliary DAC control word setting. By default, these bits are low and the output control word is decoded as noninverted, straight binary.

<a id='ed2f6f10-1e4f-42d8-b3bb-c334b090fea0'></a>

## REGISTER 42/43: SIGDELT (SIGMA-DELTA)

### Sigma-Delta Output Control Word
A 12-bit straight binary word is used to control the output of an on-chip sigma-delta converter. The sigma-delta output changes take effect immediately after any serial write is completed. The sigma-delta output control words have default values of 0. The smaller programmed output controlled words correspond to lower integrated sigma-delta output levels.

<a id='21f5a0a4-d5e6-429d-9304-c3bfa620ddf9'></a>

**REGISTER 49,50 : RX LOW POWER MODE**
Setting these bits will scale down the bias current to the ADC
analog block when the device is operated at lower speeds. By
default, these bits are low and the bias is at a nominal setting.

<a id='6d2b753b-4704-4a0e-92ee-2eee7df70dd0'></a>

For ADC operation at or below 32 MSPS, Register 49 can be set to 0x03 and Register 50 can be set to 0xEC; this will reduce Rx AVDD power consumption by about 30% relative to nominal.

<a id='313cc789-5858-4e22-89ff-7dd6b5d2c5c2'></a>

For ADC operation at or below 16 MSPS, Register 49 can be set
to 0x03 and Register 50 can be set to 0x9E; this will reduce Rx
AVDD power consumption by about 60% relative to nominal.

<a id='d65280ca-1e52-4e23-bc25-ab88b2169002'></a>

**REGISTER 63: CHIP ID**
**BIT 7–0: Rev ID**
This read only register indicates the revision of the AD9860/AD9862.

<a id='33096183-845a-40a0-8eb2-e9f230bb64e6'></a>

**Reserved Registers**
Reserved registers are held for future development and should never be written to.

<a id='cae44f95-5ff9-4e28-b860-523e74aa506f'></a>

-16-

<a id='1f3e7af0-5cdc-428d-9079-7305f4be8991'></a>

REV. 0