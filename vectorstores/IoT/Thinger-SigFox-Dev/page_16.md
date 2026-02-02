<a id='a581d503-220a-418e-bd55-93d49be59153'></a>

SmartEverything Boards
option SmartEverything Fox (via Atmel-ICE): [ ]
option SmartEverything Fox (Native USB Port): [x]
option SmartEverything Fox3 (via Atmel-ICE): [ ]
option SmartEverything Fox3 (Native USB Port): [ ]
option SmartEverything Lion (via Atmel-ICE): [ ]
option SmartEverything Lion (Native USB Port): [ ]
option SmartEverything Dragonfly (via Atmel-ICE): [ ]
option SmartEverything Dragonfly (Native USB Port): [ ]
option Analog ADI (via Atmel-ICE): [ ]
option Analog ADI (Native USB Port): [ ]
option SmartTutto (via Atmel-ICE): [ ]
option SmartTutto (Native USB Port): [ ]

<a id='fd901831-dbd7-477f-96ea-8020d66b7f2a'></a>

## Pushing data to Sigfox

Now it is time to write a simple sketch to send our sensor readings to Sigfox. The provided sample sketch will basically initialize, in the setup, the Sigfox Modem, the sensors, and the USB Serial port for some debugging. Then, in the loop, our sketch will read both the temperature and humidity and will transmit the data to Sigfox. It will also check if the transmission is OK to blink a green LED on success or a red LED otherwise. After that, it will sleep for 10 minutes, as we mentioned in the introduction, Sigfox will allow only 140 messages a day.

<a id='c2f11895-7c12-4c75-b30f-8568ae75dd28'></a>

Before presenting the code, **remember** that in the callback we have defined in the Sigfox, we established a payload config that is expecting to receive two floats representing both temperature and humidity. So, our payload must match this definition:

<a id='fba392f3-a3e5-4a25-a141-3641e50757a5'></a>

temp::float:32:little-endian hum::float:32:little-endian

<a id='9d259d97-69c0-40ea-817d-1c4a588cb945'></a>

16