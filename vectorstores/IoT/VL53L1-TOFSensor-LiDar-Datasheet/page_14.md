<a id='3ff4618a-660e-4502-935e-976fda24eec8'></a>

Functional description

<a id='9e50dac0-eb21-4d6c-9fb9-65d167fd422a'></a>

VL53L1X

<a id='7f382d3e-05d7-463f-94e6-226f4ef09631'></a>

## 2.8 Sensing array optical center
VL53L1X module includes a lens that focus the photons on the 16x16 SPADs sensing array.
The sensing array optical center specification takes into account the part-to-part variation in production.

<a id='9371f592-8a7c-4dcf-9247-c72ea7f4d036'></a>

The optical center is defined by coordinates (Xo and Yo).

<a id='19edb4b0-0b45-48e6-980a-b390a426d586'></a>

The optical center is measured for each part during a factory test at STMicroelectronics. The coordinates are stored in the VL53L1X non-volatile memory and are readable by the customer through the software driver in the application. This helps optimize design alignment with the camera and ranging performances in the application.

<a id='230aee5c-734d-4e16-9525-f0fa5dbbd987'></a>

The green array in *Figure 10: Optical center specification* gives the possible location of the optical center.

<a id='93e9164e-f429-477e-8086-2d5f7f4ce52f'></a>

Table 5. Optical center specification
<table id="13-1">
<tr><td id="13-2">Parameter</td><td id="13-3">Min.</td><td id="13-4">Typ.</td><td id="13-5">Max.</td><td id="13-6">Unit</td></tr>
<tr><td id="13-7">Xo offset</td><td id="13-8">-2</td><td id="13-9">0</td><td id="13-a">2</td><td id="13-b" rowspan="2">SPAD</td></tr>
<tr><td id="13-c">Yo offset</td><td id="13-d">-2</td><td id="13-e">0</td><td id="13-f">2</td></tr>
</table>

<a id='7717f608-bc4b-45a2-adb7-f7dae43a0b68'></a>

Figure 10. Optical center specification<::A 2D coordinate system with a grid. The x-axis and y-axis intersect at the origin. A light green square is centered at the origin, extending from -2 to 2 on both the x and y axes. The four corners of the square are labeled with their coordinates: top-left (-2, 2), top-right (2, 2), bottom-left (-2, -2), and bottom-right (2, -2). Each label has an arrow pointing to its respective corner.: diagram::>

<a id='d51119ff-c0a9-4814-885f-ca0386d780b0'></a>

For more details please refer to VL53L1X API user manual (UM2356)

<a id='9e742850-9391-423f-8264-907472131a88'></a>

14/35

<a id='b134c4dd-5e92-48f9-9285-745685007901'></a>

DocID031281 Rev 3

<a id='972f56b4-bd7a-459a-87a7-90c2ece51727'></a>

<::logo: STMicroelectronics
ST
The logo features a stylized blue 'ST' symbol above a thin horizontal line.::>