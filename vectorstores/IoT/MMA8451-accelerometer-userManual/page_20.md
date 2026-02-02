<a id='47a2024d-05d0-4174-97e3-4f7e4656d87c'></a>

print("Portrait, down, front")
elif orientation == adafruit_mma8451.PL_PDB:
    print("Portrait, down, back")
elif orientation == adafruit_mma8451.PL_LRF:
    print("Landscape, right, front")
elif orientation == adafruit_mma8451.PL_LRB:
    print("Landscape, right, back")
elif orientation == adafruit_mma8451.PL_LLF:
    print("Landscape, left, front")
elif orientation == adafruit_mma8451.PL_LLB:
    print("Landscape, left, back")
time.sleep(1.0)

<a id='999c17c6-8fe7-4f7d-85a6-76069d5fdc4e'></a>

# Python Docs

[Python Docs](https://adafru.it/C5i)

<a id='d70d5627-dc7e-44dc-8602-0b0a7aad8db7'></a>

# Downloads

## Datasheet & Files

* [MMA8451-Q Datasheet](https://adafru.it/dLO)
* [Fritzing object in Adafruit Fritzing library](https://adafru.it/aP3)
* [EagleCAD PCB files on GitHub](https://adafru.it/pIF)

<a id='6df27988-5065-47d3-9f3b-a15136eb3166'></a>

Schematics
<::
```schematic
U2 Voltage Regulator (MEC5225-3.3)
- Input (+5V) to IN and EN pins, with 10uF capacitor (C1) to GND.
- Output (+3V3) from OUT pin, with 10uF capacitor (C2) to GND.
- GND pin connected to ground.

Level Shifters (88128)
- Two identical level shifters.
- Each shifter has +3V3, SCL 3.3V, SDA 3.3V, and GND on one side.
- Each shifter has +5V, SCL 5.0V, SDA 5.0V, and GND on the other side.
- SCL 3.3V and SDA 3.3V from the level shifters connect to U1.
- SCL 5.0V and SDA 5.0V from the level shifters connect to JP1.

U1 MMA845x Accelerometer
- VDD and VDDD connected to +3V3, with 0.1uF capacitor (C3) from +3V3 to GND.
- GND connected to ground.
- SCL and SDA connected to the SCL 3.3V and SDA 3.3V lines from the level shifters.
- INT1 and INT2 pins are connected to each other and to JP1.
- BYP pin connected to GND via a capacitor (C4).
- NC pins are not connected.
- VDD 2-3.6V is noted.

JP1 Header
- Pins for SDA, SCL, INT1, INT2, +5V, and GND.
- SDA and SCL pins connected to the SCL 5.0V and SDA 5.0V lines from the level shifters.
- INT1 and INT2 pins connected to the INT1/INT2 lines from U1.
- +5V and GND pins are available.
```
: schematic::>
ISSUE
DRAUN
KTOWN
CHECKED
>CHECKED
DATE
>DATE
ADAFRUIT INDUSTRIES
TITLE
DATE
not saved!
FILE: MMA845_REV-B
2013
REV
A
DRG NO
>DRGNO
PAGE: 1/1

<a id='0f655fb3-9861-4d92-8791-0c9b1118c14d'></a>

<table id="19-1">
<tr><td id="19-2"></td><td id="19-3"></td><td id="19-4">(red abstract pattern)</td><td id="19-5">(red abstract pattern)</td></tr>
<tr><td id="19-6"></td><td id="19-7"></td><td id="19-8">(red circular pattern)</td><td id="19-9">(red circular pattern)</td></tr>
<tr><td id="19-a">ISSUE</td><td id="19-b">ADAFRUIT INDUSTRIES</td><td id="19-c" colspan="2">2013 (icon)</td></tr>
</table>
<table id="19-d">
<tr><td id="19-e">DRALN KTOWN</td><td id="19-f" rowspan="3" colspan="2">TITLE REV A DATE not saved! DRG NO &gt;DRGNO</td></tr>
<tr><td id="19-g">CHECKED &gt;CHECKED</td></tr>
<tr><td id="19-h" rowspan="2">DATE &gt;DATE</td></tr>
<tr><td id="19-i">FILE: MMA845_REV-B</td><td id="19-j">PAGE: 1/1</td></tr>
</table>

<a id='bf8d096e-bd51-4fa4-a4c5-2ec943a29f72'></a>

Fabrication print
Dimensions are in Inches

<a id='f639dd57-d9b2-4a82-901c-2fbc7c8c68f0'></a>

© Adafruit Industries

<a id='7106f12b-1a20-4420-88ce-af9691ebdac9'></a>

Page 20 of 21