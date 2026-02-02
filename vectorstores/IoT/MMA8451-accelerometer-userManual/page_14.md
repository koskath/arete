<a id='c6b14f04-cfac-4966-854b-f1f88b6dbb6e'></a>

mma.getRange()

<a id='a0e42bfb-d042-45dd-a10a-711aba543248'></a>

Which returns 1 for ±2g, 2 for ±4g and 3 for ±8g

<a id='d7eacc58-a295-4afa-b629-a1c513a80e37'></a>

Read Raw Count Data
You can read the raw counts data with

<a id='648eebb8-a89f-466c-9750-65f83cd5d72e'></a>

```
mma.read();
```

<a id='9984c523-9da1-4cbb-b418-870d574bde8f'></a>

The x, y and z data is then available in **mma.x**, **mma.y** and **mma.z**
All three are read in one transaction.

<a id='3fe55a4e-288d-477f-a409-414ec8175fc1'></a>

Reading Normalized Adafruit_Sensor data
We recommend using the Adafruit_Sensor interface which allows reading into an
event structure. First create a new event structure

<a id='78091f38-0344-46d4-9ad0-3cec2809e925'></a>

sensors_event_t event;

<a id='ac0ae868-e9f9-4646-b3e4-de365618d754'></a>

Then read the event whenever you want

```
mma.getEvent(&amp;event);
```

<a id='2ab87a4b-b881-46be-9158-52218b553c71'></a>

The normalized SI unit data is available in `event.acceleration.x`, `event.acceleration.y` and `event.acceleration.z`

<a id='7b8fb58b-5310-4efd-8e94-9f49979f7637'></a>

## Read Orientation

The sensor has built in tilt/orientation detection. You can read the current orientation with

```
mma.getOrientation();
```

<a id='396108dd-ab54-4854-8aa8-10c6eab9c269'></a>

The return value ranges from 0 to 7
* 0: Portrait Up Front
* 1: Portrait Up Back
* 2: Portrait Down Front
* 3: Portrait Down Back
* 4: Landscape Right Front
* 5: Landscape Right Back
* 6: Landscape Left Front
* 7: Landscape Left Back

<a id='b2993155-e912-4c01-b0c1-ff60d577e29a'></a>

© Adafruit Industries

<a id='28024783-d857-47fd-be23-1ec49dc89590'></a>

Page 14 of 21