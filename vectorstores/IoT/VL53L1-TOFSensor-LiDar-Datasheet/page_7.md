<a id='d89be6e2-6d1a-4c72-bb24-49de5b01f86d'></a>

VL53L1X

<a id='35d66566-7589-4ba7-9527-d6c18abd4611'></a>

Functional description

<a id='10945ba7-5a8d-427a-b4df-dd2c8a2eafa3'></a>

2 Functional description

<a id='8af50796-3490-4dd1-a530-180bafec6d6d'></a>

## 2.1 System functional description

Figure 4 shows the system level functional description. The host customer application controls the VL53L1X device using an API (application programming interface). The API implementation is delivered to the customer as a driver (Bare C code).

<a id='c8f5f7da-f4e2-4275-9143-df84543f6246'></a>

The driver shares with the customer application a set of high-level functions that allow control of the VL53L1X like initialization, ranging start/stop, and setting the system accuracy.

<a id='ccb93e89-85e5-4614-9324-71d617d25d60'></a>

The driver enables fast development of end user applications without the complication of direct multiple register access. The driver is structured in a way that it can be compiled on any kind of platform through a good hardware abstraction layer.

<a id='bcc544f0-d80c-4e68-92aa-428ee4ecd987'></a>

A detailed description of the driver is available in the VL53L1X API user manual (UM2356).

<a id='f6bb6be8-839c-4731-835b-2cc5ff775f22'></a>

Figure 4. VL53L1X system functional description

<::
HOST
  User Application <-> VL53L1X driver
VL53L1X driver --> VL53L1X (via I2C)
: diagram::>

<a id='f574b4c7-bd5b-4dc6-8d30-ddf9127686cf'></a>

<::logo: STMicroelectronics
ST
A stylized blue 'ST' logo with a horizontal line underneath.::>

<a id='6fe24bed-3cbe-4da4-9c58-7752cbbaded0'></a>

DocID031281 Rev 3

<a id='c7360eef-4477-4af3-a836-cbcf5429695b'></a>

7/35