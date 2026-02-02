<a id='e4afb298-2acb-49c3-bfc0-1a8088c16269'></a>

VL53L1X

<a id='53fb5717-8d6e-4621-a2a5-dea7cb9a1be9'></a>

Functional description

<a id='eb269ac1-87fc-46ec-a231-0b88c6d8fe25'></a>

## 2.3 Customer manufacturing calibration flow

The VL53L1X driver includes calibration functions. To benefit from device full performances, it is recommended they be run once at the customer production line.

Device calibration allows part-to-part parameter variations and cover glass presence that may affect device performances to be compensated.

Calibration data stored in the host have to be loaded into the VL53L1X at each startup using a dedicated driver function.

Three calibration steps are needed: RefSPAD, offset and crosstalk.

RefSPAD and crosstalk calibrations have to be performed whenever the customer adds a protective cover glass on top of the VL53L1X module.

Offset calibration has to be performed in all situations. It allows reflow and cover glass effects to be compensated.

The detailed procedure is provided in the VL53L1X API user manual (UM2356).

<a id='25e5ace5-35f4-4f78-b8ec-4b130ced003d'></a>

## 2.4 Ranging description

The VL53L1X software driver proposes turnkey solution to allow fast implementation and easy ranging in all customer applications:

**Autonomous ranging mode** is the default configuration that offers the optimized VL53L1X functionalities.

*   Ranging is continuous, with a programmable delay between two ranging operations (called an inter-measurement period). Ranging duration (timing budget) is also programmable.
*   The user can set distance thresholds (below, above, inside, or outside the user-defined thresholds). An interrupt is raised only when threshold conditions are met.
*   ROI size and position are programmable: the user may chose a custom FoV from 4x4 SPADs (minimum size) up to 16x16 SPADs (full FoV).
*   A clear interrupt is mandatory to allow the next ranging data to be updated.

If the ranging distance cannot be measured (in the case of no target or a weak signal), a corresponding range status is generated and can be read by the host.

The VL53L1X software driver provides turnkey functions to read output results after the measurement. The main values reported are:

*   Ranging distance in mm
*   Return signal rate
*   Ambient signal rate
*   Range status

<a id='00906155-622e-462c-8986-878dfa09fd3f'></a>

Range status and output measurement definitions are provided in the VL53L1X API user
manual (UM2356).

<a id='978dbac2-9640-44a9-a22d-22fdf5c23792'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold, blue font, with a horizontal line beneath it.::>

<a id='9d4662fd-f981-43f5-8f1f-1bcd71437ba7'></a>

DocID031281 Rev 3

<a id='d32b8073-cdd0-46ae-8691-54ceabbce94f'></a>

9/35